# SourceSpring Version Updater Action

## Overview

The Version Updater Action is a sophisticated GitHub Action designed to streamline version management across software projects. By supporting both XML and TOML configuration files, this action simplifies version tracking and enables automated version incrementation with minimal configuration.

## 🌟 Key Features

### Comprehensive Version Management
- **Multi-Format Support**: Seamlessly handles version updates in Maven `pom.xml` and Python `pyproject.toml` files
- **Flexible Version Incrementation**: 
  - Increment major, minor, or patch versions automatically
  - Manually set specific version numbers
- **Environment Integration**: Automatically exports version-related variables for downstream workflows

### Intelligent Version Tracking
- Automatically extracts artifact names and version information
- Provides consistent version management across different project types
- Reduces manual intervention in version bumping processes

## 📦 Installation

To integrate the Version Updater Action into your GitHub workflow, add the following configuration to your workflow file:

```yaml
- name: Update Project Version
  uses: SourceSpring/action-semantic-versioning@v1
  with:
    file_path: "./path/to/configuration/file"
    artifact_id: "your-project-name"
    increment: "patch"  # Or "minor", "major"
```

## 🔧 Configuration Options

### Required Inputs

| Parameter      | Type   | Required | Description                                           |
|---------------|--------|----------|-------------------------------------------------------|
| `file_path`   | String | ✅       | Path to version configuration file (pom.xml/pyproject.toml) |
| `artifact_id` | String | ✅       | Unique identifier for your project or artifact        |

### Optional Inputs

| Parameter      | Type   | Description                                           |
|---------------|--------|-------------------------------------------------------|
| `increment`   | String | Version segment to increment: `major`, `minor`, `patch` |
| `set_version` | String | Manually specify an exact version number               |

> **Important**: You must use either `increment` or `set_version`, but not both simultaneously.

## 📤 Exported Environment Variables

The action automatically populates the following environment variables:

| Variable            | Description                                     | Example             |
|--------------------|-------------------------------------------------|---------------------|
| `artifact-version-id` | Updated version number                          | `1.2.3`             |
| `artifact-name`    | Project or artifact name                        | `my-awesome-project`|
| `artifact-full-id` | Combined artifact name and version               | `my-awesome-project-1.2.3` |

## 🚀 Workflow Examples

### Automated Patch Version Update
```yaml
name: Automatically Update Version

on:
  push:
    branches: [main]

jobs:
  version-bump:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Increment Patch Version
        uses: SourceSpring/action-semantic-versioning@v1
        with:
          file_path: "./pyproject.toml"
          artifact_id: "my-project"
          increment: "patch"
```

### Manual Version Setting
```yaml
name: Manual Version Update

jobs:
  version-set:
    steps:
      - name: Set Specific Version
        uses: SourceSpring/action-semantic-versioning@v1
        with:
          file_path: "./pom.xml"
          artifact_id: "enterprise-app"
          set_version: "2.1.0"
```

## 🤝 Contributing

We welcome contributions! Please check our GitHub repository for guidelines on:
- Reporting issues
- Suggesting features
- Submitting pull requests

## 📄 License

This project is licensed under the terms specified in the GitHub repository.

## 🔗 Project Status

[![Build Status](https://img.shields.io/github/actions/workflow/status/SourceSpring/action-semantic-versioning/main.yml)](https://github.com/SourceSpring/action-semantic-versioning)
[![Version](https://img.shields.io/github/v/release/SourceSpring/action-semantic-versioning)](https://github.com/SourceSpring/action-semantic-versioning/releases)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)](https://github.com/SourceSpring/action-semantic-versioning)

## 📊 Community & Adoption

- **Total Dependents**: 23.2k repositories
- **Open Discussions**: 158
- **GitHub Stars**: Growing community support
