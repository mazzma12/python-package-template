"""Tests for cookiecutter template generation."""

import shutil
import subprocess
import sys
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


class TestTemplateGeneration:
    """Test cookiecutter template generation with different configurations."""

    def test_default_generation(self, temp_dir, template_dir):
        """Test template generation with default values."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Template generation failed: " + result.stderr

        project_dir = temp_dir / "alpacasay"
        assert project_dir.exists(), "Project directory was not created"

        # Check core files exist
        assert (project_dir / "pyproject.toml").exists()
        assert (project_dir / "README.md").exists()
        assert (project_dir / ".gitignore").exists()
        assert (project_dir / "src" / "alpacasay" / "__init__.py").exists()
        assert (project_dir / "src" / "alpacasay" / "cli.py").exists()
        assert (project_dir / "tests" / "test_cli.py").exists()

        # Check default optional files exist (all enabled by default)
        assert (project_dir / "LICENSE").exists()
        assert (project_dir / "docs" / "index.md").exists()
        assert (project_dir / "mkdocs.yml").exists()
        assert (project_dir / "Dockerfile").exists()
        assert (project_dir / "docker-compose.yml").exists()
        assert (project_dir / ".github" / "workflows" / "code-quality.yml").exists()
        assert (project_dir / ".github" / "workflows" / "publish.yml").exists()
        assert (project_dir / ".pre-commit-config.yaml").exists()

    def test_minimal_generation(self, temp_dir, template_dir):
        """Test template generation with minimal features."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
                "package_name=minimal_package",
                "project_name=Minimal Package",
                "project_description=A minimal test package",
                "author_name=Test Author",
                "author_email=test@example.com",
                "github_username=testuser",
                "version=0.1.0",
                "python_version=3.11",
                "minimum_python_version=3.11",
                "include_license=none",
                "include_docs=n",
                "include_docker=n",
                "include_publishing=n",
                "include_github_actions=n",
                "include_pre_commit=n",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Minimal generation failed: " + result.stderr

        project_dir = temp_dir / "minimal_package"
        assert project_dir.exists()

        # Check core files exist
        assert (project_dir / "pyproject.toml").exists()
        assert (project_dir / "README.md").exists()
        assert (project_dir / ".gitignore").exists()
        assert (project_dir / "src" / "minimal_package" / "__init__.py").exists()

        # Check optional files are absent
        assert not (project_dir / "LICENSE").exists()
        assert not (project_dir / "docs").exists()
        assert not (project_dir / "mkdocs.yml").exists()
        assert not (project_dir / "Dockerfile").exists()
        assert not (project_dir / "docker-compose.yml").exists()
        assert not (project_dir / ".github" / "workflows").exists()
        assert not (project_dir / ".pre-commit-config.yaml").exists()

    def test_docs_only_generation(self, temp_dir, template_dir):
        """Test template generation with docs only."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
                "package_name=docs_package",
                "project_name=Docs Package",
                "project_description=A package with docs only",
                "author_name=Test Author",
                "author_email=test@example.com",
                "github_username=testuser",
                "version=0.1.0",
                "python_version=3.11",
                "minimum_python_version=3.11",
                "include_license=none",
                "include_docs=y",
                "include_docker=n",
                "include_publishing=n",
                "include_github_actions=n",
                "include_pre_commit=n",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Docs-only generation failed: " + result.stderr

        project_dir = temp_dir / "docs_package"
        assert project_dir.exists()

        # Check docs files exist
        assert (project_dir / "docs" / "index.md").exists()
        assert (project_dir / "docs" / "api.md").exists()
        assert (project_dir / "mkdocs.yml").exists()

        # Check other optional files are absent
        assert not (project_dir / "LICENSE").exists()
        assert not (project_dir / "Dockerfile").exists()
        assert not (project_dir / ".github" / "workflows").exists()

    def test_docker_only_generation(self, temp_dir, template_dir):
        """Test template generation with Docker only."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
                "package_name=docker_package",
                "project_name=Docker Package",
                "project_description=A package with Docker only",
                "author_name=Test Author",
                "author_email=test@example.com",
                "github_username=testuser",
                "version=0.1.0",
                "python_version=3.11",
                "minimum_python_version=3.11",
                "include_license=none",
                "include_docs=n",
                "include_docker=y",
                "include_publishing=n",
                "include_github_actions=n",
                "include_pre_commit=n",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Docker-only generation failed: " + result.stderr

        project_dir = temp_dir / "docker_package"
        assert project_dir.exists()

        # Check Docker files exist
        assert (project_dir / "Dockerfile").exists()
        assert (project_dir / "docker-compose.yml").exists()
        assert (project_dir / ".dockerignore").exists()

        # Check other optional files are absent
        assert not (project_dir / "LICENSE").exists()
        assert not (project_dir / "docs").exists()
        assert not (project_dir / ".github" / "workflows").exists()

    def test_github_actions_only_generation(self, temp_dir, template_dir):
        """Test template generation with GitHub Actions only."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
                "package_name=ci_package",
                "project_name=CI Package",
                "project_description=A package with CI only",
                "author_name=Test Author",
                "author_email=test@example.com",
                "github_username=testuser",
                "version=0.1.0",
                "python_version=3.11",
                "minimum_python_version=3.11",
                "include_license=none",
                "include_docs=n",
                "include_docker=n",
                "include_publishing=n",
                "include_github_actions=y",
                "include_pre_commit=n",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, (
            "GitHub Actions generation failed: " + result.stderr
        )

        project_dir = temp_dir / "ci_package"
        assert project_dir.exists()

        # Check GitHub Actions files exist
        assert (project_dir / ".github" / "workflows" / "code-quality.yml").exists()

        # Check publishing workflow is absent when publishing disabled
        assert not (project_dir / ".github" / "workflows" / "publish.yml").exists()

    def test_publishing_with_github_actions(self, temp_dir, template_dir):
        """Test template generation with publishing and GitHub Actions."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "--output-dir",
                str(temp_dir),
                "package_name=publishing_package",
                "project_name=Publishing Package",
                "project_description=A package with publishing",
                "author_name=Test Author",
                "author_email=test@example.com",
                "github_username=testuser",
                "version=0.1.0",
                "python_version=3.11",
                "minimum_python_version=3.11",
                "include_license=MIT",
                "include_docs=n",
                "include_docker=n",
                "include_publishing=y",
                "include_github_actions=y",
                "include_pre_commit=n",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Publishing generation failed: " + result.stderr

        project_dir = temp_dir / "publishing_package"
        assert project_dir.exists()

        # Check both CI and publishing workflows exist
        assert (project_dir / ".github" / "workflows" / "code-quality.yml").exists()
        assert (project_dir / ".github" / "workflows" / "publish.yml").exists()
