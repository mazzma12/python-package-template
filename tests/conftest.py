"""Test configuration for cookiecutter template tests."""

import shutil
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def template_dir():
    """Get the path to the cookiecutter template."""
    return Path(__file__).parent.parent


@pytest.fixture
def default_context():
    """Default context for template generation."""
    return {
        "project_name": "Test Package",
        "package_name": "test_package", 
        "project_description": "A test package for template validation",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "github_username": "testuser",
        "version": "0.1.0",
        "python_version": "3.11",
        "minimum_python_version": "3.11",
        "include_license": "MIT",
        "include_docs": "y",
        "include_docker": "y", 
        "include_publishing": "y",
        "include_github_actions": "y",
        "include_pre_commit": "y",
        "cli_name": "test-package",
        "project_slug": "test-package",
    }
