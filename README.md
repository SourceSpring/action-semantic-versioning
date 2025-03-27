# Version Updater Action

![SourceSpring](https://img.shields.io/badge/SourceSpring-%23232323?style=for-the-badge&logo=SourceSpring&logoColor=white)

![Backers](https://img.shields.io/badge/backers-162-brightgreen?style=flat-square)
![Sponsors](https://img.shields.io/badge/sponsors-33-brightgreen?style=flat-square)
![Commit Activity](https://img.shields.io/badge/commit%20activity-55%2Fmonth-blue?style=flat-square)
![Discussions](https://img.shields.io/badge/discussions-158%20total-blue?style=flat-square)
![Daily Tests](https://img.shields.io/badge/daily%20tests-failing-red?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-93%25-yellowgreen?style=flat-square)
![Chat](https://img.shields.io/discord/123456789012345678?label=chat&color=brightgreen&style=flat-square)
![Version Updater](https://img.shields.io/github/actions/workflow/status/SourceSpring/action-semantic-versioning/main.yml?branch=main) 
![GitHub last commit](https://img.shields.io/github/last-commit/SourceSpring/action-semantic-versioning) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/SourceSpring/action-semantic-versioning) 
![GitHub issues](https://img.shields.io/github/issues/SourceSpring/action-semantic-versioning) 
![GitHub pull requests](https://img.shields.io/github/issues-pr/SourceSpring/action-semantic-versioning) 
![GitHub forks](https://img.shields.io/github/forks/SourceSpring/action-semantic-versioning?style=social) 
![GitHub stars](https://img.shields.io/github/stars/SourceSpring/action-semantic-versioning?style=social) 
![GitHub license](https://img.shields.io/github/license/SourceSpring/action-semantic-versioning) 
[![Used by](https://img.shields.io/badge/Used%20by-23.2k-blue)](https://github.com/SourceSpring/action-semantic-versioning/network/dependents) 


## 🚀 Project Badges

| Badge | Description |
|-------|------------|


## 📦 Description

A GitHub Action to find and update version numbers in `XML` or `TOML` files.
And export useful version variables into the `GITHUB_ENV` environment.

---

## ✅ Features

- Reads and updates version in `pom.xml` or `pyproject.toml`
- Supports version incrementing (`major`, `minor`, `patch`)
- Allows setting a custom version
- Automatically exports:
  - `artifact-version-id`
  - `artifact-name`
  - `artifact-full-id`

---

## 📥 Inputs

| Input         | Required | Description                                                        |
| ------------- | -------- | ------------------------------------------------------------------ |
| `file_path`   | ✅       | Path to the XML or TOML file (e.g., `pom.xml` or `pyproject.toml`) |
| `artifact_id` | ✅       | The artifact name to search for in the file                        |
| `increment`   | ❌       | Version part to increment: `major`, `minor`, or `patch`            |
| `set_version` | ❌       | Custom version to set instead of incrementing                      |

---

## ✅ Outputs (via GITHUB_ENV)

| Environment Variable  | Description                                |
| --------------------- | ------------------------------------------ |
| `artifact-version-id` | The updated version number                 |
| `artifact-name`       | The artifact name                          |
| `artifact-full-id`    | A combination of artifact name and version |

---

## 🚀 Usage Example

```yaml
name: Update Artifact Version

on:
  push:
    branches: [main]

jobs:
  version-update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run version updater
        uses: your-username/your-repo-name@v1
        with:
          file_path: "./pyproject.toml"
          artifact_id: "action-semantic-versioning"
          increment: "patch"
```
