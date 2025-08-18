#!/usr/bin/env python3
"""Post-generation hook to clean up optional files."""

import os
import shutil

# Get cookiecutter variables
include_license = "{{ cookiecutter.include_license }}"
include_docs = "{{ cookiecutter.include_docs }}"
include_docker = "{{ cookiecutter.include_docker }}"
include_publishing = "{{ cookiecutter.include_publishing }}"
include_github_actions = "{{ cookiecutter.include_github_actions }}"
include_pre_commit = "{{ cookiecutter.include_pre_commit }}"

def remove_file(filepath):
    """Remove a file if it exists."""
    if os.path.isfile(filepath):
        os.remove(filepath)
        print(f"Removed {filepath}")

def remove_dir(dirpath):
    """Remove a directory if it exists."""
    if os.path.isdir(dirpath):
        shutil.rmtree(dirpath)
        print(f"Removed {dirpath}")

# Remove license file if not needed
if include_license == "none":
    remove_file("LICENSE")

# Remove documentation files if not needed
if include_docs == "n":
    remove_dir("docs")
    remove_file("mkdocs.yml")

# Remove Docker files if not needed
if include_docker == "n":
    remove_file("Dockerfile")
    remove_file("docker-compose.yml")
    remove_file(".dockerignore")

# Remove GitHub Actions workflows if not needed
if include_github_actions == "n":
    remove_dir(".github/workflows")
    # Keep .github directory if it has other content
    if os.path.isdir(".github") and not os.listdir(".github"):
        remove_dir(".github")

# Remove publishing workflow if not needed
elif include_publishing == "n":
    remove_file(".github/workflows/pypi-publish.yml")
    remove_file(".github/workflows/publish.yml")

# Remove pre-commit config if not needed
if include_pre_commit == "n":
    remove_file(".pre-commit-config.yaml")

print("✅ Project generated successfully!")
print("📁 Project structure cleaned up based on your choices.")

# Print next steps
print("\n🚀 Next steps:")
print("1. cd into your project directory")
print("2. Initialize git: git init")
print("3. Install dependencies: uv sync --dev")

if include_pre_commit == "y":
    print("4. Setup pre-commit: uv run pre-commit install")

if include_docker == "y":
    print("5. Test Docker build: docker build -t {{ cookiecutter.project_slug }} .")

print("6. Test your CLI: uv run {{ cookiecutter.cli_name }} --help")
print("\n🎉 Happy coding with your new Python package!")
