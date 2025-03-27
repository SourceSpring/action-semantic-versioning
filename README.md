# Version Updater Action

![Version Updater](https://img.shields.io/github/actions/workflow/status/SourceSpring/action-semantic-versioning/main.yml?branch=main)

![Used By](https://img.shields.io/github/dependents-repo/YOUR_USERNAME/YOUR_REPOSITORY)

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
