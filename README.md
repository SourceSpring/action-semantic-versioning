# Version Updater Action

![SourceSpring](https://img.shields.io/badge/SourceSpring-%23232323?style=for-the-badge&logo=SourceSpring&logoColor=white)
![Version](https://img.shields.io/github/v/release/SourceSpring/action-semantic-versioning?style=flat-square)
![Commit Activity](https://img.shields.io/badge/commit%20activity-55%2Fmonth-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-93%25-yellowgreen?style=flat-square)
![Discussions](https://img.shields.io/badge/discussions-158%20total-blue?style=flat-square)
![Chat](https://img.shields.io/discord/123456789012345678?label=chat&color=brightgreen&style=flat-square)

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/SourceSpring/action-semantic-versioning/main.yml?branch=main&label=Version%20Updater)
![GitHub Last Commit](https://img.shields.io/github/last-commit/SourceSpring/action-semantic-versioning)
![GitHub Issues](https://img.shields.io/github/issues/SourceSpring/action-semantic-versioning)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/SourceSpring/action-semantic-versioning)
![GitHub License](https://img.shields.io/github/license/SourceSpring/action-semantic-versioning)

[![Used by](https://img.shields.io/badge/Used%20by-23.2k-blue)](https://github.com/SourceSpring/action-semantic-versioning/network/dependents)
![GitHub Forks](https://img.shields.io/github/forks/SourceSpring/action-semantic-versioning?style=social)
![GitHub Stars](https://img.shields.io/github/stars/SourceSpring/action-semantic-versioning?style=social)

---

## 📦 Overview

The **Version Updater Action** is a powerful GitHub Action designed to automate version management in `XML` (e.g., `pom.xml`) and `TOML` (e.g., `pyproject.toml`) files. It simplifies workflows by finding, updating, and exporting version-related variables into the `GITHUB_ENV` environment, making them readily available for downstream tasks.

---

## ✅ Key Features

- **File Support**: Reads and updates versions in `pom.xml` (Maven) or `pyproject.toml` (Python).
- **Version Incrementing**: Supports `major`, `minor`, and `patch` version increments.
- **Custom Versioning**: Allows setting a specific version manually.
- **Environment Exports**: Automatically sets the following variables in `GITHUB_ENV`:
  - `artifact-version-id`: The updated version number.
  - `artifact-name`: The artifact name.
  - `artifact-full-id`: A combination of artifact name and version.

---

## 📥 Inputs

| Input         | Required | Description                                                        |
|---------------|----------|--------------------------------------------------------------------|
| `file_path`   | ✅       | Path to the XML or TOML file (e.g., `pom.xml` or `pyproject.toml`). |
| `artifact_id` | ✅       | The artifact name to search for in the file.                       |
| `increment`   | ❌       | Version part to increment: `major`, `minor`, or `patch`.           |
| `set_version` | ❌       | Custom version to set instead of incrementing (e.g., `1.2.3`).     |

> **Note**: Either `increment` or `set_version` can be used, but not both simultaneously.

---

## ✅ Outputs

The action exports the following variables to `GITHUB_ENV` for use in subsequent steps:

| Environment Variable  | Description                                |
|-----------------------|--------------------------------------------|
| `artifact-version-id` | The updated version number (e.g., `1.0.1`).|
| `artifact-name`       | The artifact name (e.g., `my-project`).    |
| `artifact-full-id`    | Combined artifact name and version (e.g., `my-project-1.0.1`). |

---

## 🚀 Usage Example

Below is an example GitHub workflow that uses the Version Updater Action to increment the `patch` version in a `pyproject.toml` file.

```yaml
name: Update Artifact Version

on:
  push:
    branches: [main]

jobs:
  version-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Update Version
        uses: SourceSpring/action-semantic-versioning@v1
        with:
          file_path: "./pyproject.toml"
          artifact_id: "action-semantic-versioning"
          increment: "patch"

      - name: Display Updated Version
        run: |
          echo "Updated Version: $artifact-version-id"
          echo "Artifact Name: $artifact-name"
          echo "Full ID: $artifact-full-id"
