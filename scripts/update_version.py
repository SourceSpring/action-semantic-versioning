import argparse
import sys
import os
from typing import Optional
import xml.etree.ElementTree as ET
import toml
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

NAMESPACE = {'m': 'http://maven.apache.org/POM/4.0.0'}

def parse_xml(file_path: str) -> ET.ElementTree:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    try:
        return ET.parse(file_path)
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse {file_path}: {e}")

def parse_toml(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return toml.load(f)
    except toml.TomlDecodeError as e:
        raise ValueError(f"Failed to parse {file_path}: {e}")

def find_version(file_path: str, artifact_id: str) -> Optional[str]:
    _, ext = os.path.splitext(file_path.lower())
    if ext == '.xml':
        tree = parse_xml(file_path)
        root = tree.getroot()
        has_namespace = root.tag.startswith(f"{{{NAMESPACE['m']}}}")
        if has_namespace:
            version_elem = root.find(f".//m:artifactId[.='{artifact_id}']/../m:version", NAMESPACE)
        else:
            version_elem = root.find(f".//artifactId[.='{artifact_id}']/../version")
        return version_elem.text if version_elem is not None else None

    elif ext == '.toml':
        data = parse_toml(file_path)
        project = data.get('project', {})
        if project.get('name') != artifact_id:
            raise ValueError(f"Artifact name '{project.get('name')}' doesn't match '{artifact_id}'")
        return project.get('version')

    raise ValueError(f"Unsupported file type: {ext}. Use '.xml' or '.toml'")

def update_version(file_path: str, artifact_id: str, new_version: str) -> None:
    _, ext = os.path.splitext(file_path.lower())
    if ext == '.xml':
        tree = parse_xml(file_path)
        root = tree.getroot()
        has_namespace = root.tag.startswith(f"{{{NAMESPACE['m']}}}")
        if has_namespace:
            ET.register_namespace('', NAMESPACE['m'])
            version_elem = root.find(f".//m:artifactId[.='{artifact_id}']/../m:version", NAMESPACE)
        else:
            version_elem = root.find(f".//artifactId[.='{artifact_id}']/../version")

        if version_elem is not None:
            version_elem.text = new_version
            tree.write(file_path, encoding='utf-8', xml_declaration=True, method='xml')

    elif ext == '.toml':
        data = parse_toml(file_path)
        data['project']['version'] = new_version
        with open(file_path, 'w', encoding='utf-8') as f:
            toml.dump(data, f)

def increment_version(version: str, part: str) -> str:
    major, minor, patch = map(int, version.split('.'))
    if part == 'major':
        return f"{major + 1}.0.0"
    elif part == 'minor':
        return f"{major}.{minor + 1}.0"
    elif part == 'patch':
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError("Invalid part. Use 'major', 'minor', or 'patch'")

def main():
    parser = argparse.ArgumentParser(description="Find and update package version in XML or TOML")
    parser.add_argument("file_path", help="Path to the XML or TOML file")
    parser.add_argument("artifact_id", help="Artifact ID to find or update")
    parser.add_argument("--increment", choices=["major", "minor", "patch"], help="Part of version to increment")
    parser.add_argument("--set-version", help="Custom version to set")
    args = parser.parse_args()

    file_path = args.file_path
    artifact_id = args.artifact_id
    part_to_increment = args.increment
    custom_version = args.set_version

    try:
        current_version = find_version(file_path, artifact_id)
        if not current_version:
            logger.error(f"Version not found for '{artifact_id}'")
            sys.exit(1)
        logger.info(f"Current Version: {current_version} (Artifact: {artifact_id})")

        if custom_version:
            new_version = custom_version
            logger.info(f"Using provided custom version: {new_version}")
        elif part_to_increment:
            new_version = increment_version(current_version, part_to_increment)
            logger.info(f"Incremented Version: {new_version}")
        else:
            logger.info("No --increment or --set-version provided; no version update will be performed.")
            return

        with open(os.getenv('GITHUB_ENV', '/dev/null'), 'a', encoding='utf-8') as env_file:
            env_vars = {
                'artifact-version-id': new_version,
                'artifact-name': artifact_id,
                'artifact-full-id': f"{artifact_id}-{new_version}"
            }
            for key, value in env_vars.items():
                env_file.write(f"{key}={value}\n")
                logger.info(f"Set {key}: {value}")
                print(f"{key}={value}")

        update_version(file_path, artifact_id, new_version)
        logger.info(f"Updated {file_path} successfully")

    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
