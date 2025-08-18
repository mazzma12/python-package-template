"""Tests for cookiecutter template generation."""

import subprocess
import sys

import pytest


class TestTemplateGeneration:
    """Test cookiecutter template generation with different configurations."""

    def test_default_generation(self, temp_dir, template_dir):
        """Test template generation with default values."""
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter", 
            str(template_dir), 
            "--no-input",
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
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
        assert (project_dir / ".github" / "workflows" / "ci.yml").exists()
        assert (project_dir / ".github" / "workflows" / "pypi-publish.yml").exists()
        assert (project_dir / ".pre-commit-config.yaml").exists()

    def test_minimal_generation(self, temp_dir, template_dir):
        """Test template generation with minimal features."""
        # Create a minimal context file
        context_file = temp_dir / "context.json"
        context_file.write_text('''{
            "project_name": "Minimal Package",
            "package_name": "minimal_package",
            "project_description": "A minimal test package",
            "author_name": "Test Author",
            "author_email": "test@example.com", 
            "github_username": "testuser",
            "version": "0.1.0",
            "python_version": "3.11",
            "minimum_python_version": "3.11",
            "include_license": "none",
            "include_docs": "n",
            "include_docker": "n",
            "include_publishing": "n", 
            "include_github_actions": "n",
            "include_pre_commit": "n"
        }''')
        
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input",
            "--config-file", str(context_file),
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
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
        assert not (project_dir / ".github").exists()
        assert not (project_dir / ".pre-commit-config.yaml").exists()

    def test_docs_only_generation(self, temp_dir, template_dir):
        """Test template generation with docs only."""
        context_file = temp_dir / "context.json"
        context_file.write_text('''{
            "project_name": "Docs Package",
            "package_name": "docs_package",
            "project_description": "A package with docs only",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "github_username": "testuser", 
            "version": "0.1.0",
            "python_version": "3.11",
            "minimum_python_version": "3.11",
            "include_license": "none",
            "include_docs": "y",
            "include_docker": "n",
            "include_publishing": "n",
            "include_github_actions": "n", 
            "include_pre_commit": "n"
        }''')
        
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input", 
            "--config-file", str(context_file),
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
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
        assert not (project_dir / ".github").exists()

    def test_docker_only_generation(self, temp_dir, template_dir):
        """Test template generation with Docker only."""
        context_file = temp_dir / "context.json"
        context_file.write_text('''{
            "project_name": "Docker Package",
            "package_name": "docker_package",
            "project_description": "A package with Docker only",
            "author_name": "Test Author", 
            "author_email": "test@example.com",
            "github_username": "testuser",
            "version": "0.1.0",
            "python_version": "3.11",
            "minimum_python_version": "3.11",
            "include_license": "none",
            "include_docs": "n",
            "include_docker": "y",
            "include_publishing": "n",
            "include_github_actions": "n",
            "include_pre_commit": "n"
        }''')
        
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input",
            "--config-file", str(context_file), 
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
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
        assert not (project_dir / ".github").exists()

    def test_github_actions_only_generation(self, temp_dir, template_dir):
        """Test template generation with GitHub Actions only."""
        context_file = temp_dir / "context.json"
        context_file.write_text('''{
            "project_name": "CI Package",
            "package_name": "ci_package",
            "project_description": "A package with CI only",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "github_username": "testuser",
            "version": "0.1.0", 
            "python_version": "3.11",
            "minimum_python_version": "3.11",
            "include_license": "none",
            "include_docs": "n",
            "include_docker": "n",
            "include_publishing": "n",
            "include_github_actions": "y",
            "include_pre_commit": "n"
        }''')
        
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input",
            "--config-file", str(context_file),
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
        assert result.returncode == 0, "GitHub Actions generation failed: " + result.stderr
        
        project_dir = temp_dir / "ci_package"
        assert project_dir.exists()
        
        # Check GitHub Actions files exist
        assert (project_dir / ".github" / "workflows" / "ci.yml").exists()
        
        # Check publishing workflow is absent when publishing disabled
        assert not (project_dir / ".github" / "workflows" / "pypi-publish.yml").exists()

    def test_publishing_with_github_actions(self, temp_dir, template_dir):
        """Test template generation with publishing and GitHub Actions."""
        context_file = temp_dir / "context.json"
        context_file.write_text('''{
            "project_name": "Publishing Package",
            "package_name": "publishing_package",
            "project_description": "A package with publishing",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "github_username": "testuser",
            "version": "0.1.0",
            "python_version": "3.11", 
            "minimum_python_version": "3.11",
            "include_license": "MIT",
            "include_docs": "n",
            "include_docker": "n",
            "include_publishing": "y",
            "include_github_actions": "y",
            "include_pre_commit": "n"
        }''')
        
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input",
            "--config-file", str(context_file),
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
        assert result.returncode == 0, "Publishing generation failed: " + result.stderr
        
        project_dir = temp_dir / "publishing_package"
        assert project_dir.exists()
        
        # Check both CI and publishing workflows exist
        assert (project_dir / ".github" / "workflows" / "ci.yml").exists()
        assert (project_dir / ".github" / "workflows" / "pypi-publish.yml").exists()

    def test_pyproject_toml_content(self, temp_dir, template_dir):
        """Test that pyproject.toml has correct content based on options."""
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input",
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
        assert result.returncode == 0
        
        project_dir = temp_dir / "alpacasay"
        pyproject_file = project_dir / "pyproject.toml"
        pyproject_content = pyproject_file.read_text()
        
        # Check that Typer is used instead of Click
        assert "typer>=" in pyproject_content
        assert "click" not in pyproject_content.lower()
        
        # Check entry point
        assert 'alpacasay = "alpacasay.cli:app"' in pyproject_content
        
        # Check license is included
        assert 'license = { text = "MIT" }' in pyproject_content

    def test_generated_code_imports(self, temp_dir, template_dir):
        """Test that generated code uses absolute imports."""
        result = subprocess.run([
            sys.executable, "-m", "cookiecutter",
            str(template_dir),
            "--no-input", 
            "--output-dir", str(temp_dir)
        ], capture_output=True, text=True)
        
        assert result.returncode == 0
        
        project_dir = temp_dir / "alpacasay"
        
        # Check CLI imports
        cli_file = project_dir / "src" / "alpacasay" / "cli.py"
        cli_content = cli_file.read_text()
        assert "from alpacasay.alpacas import" in cli_content
        assert "from alpacasay.formatter import" in cli_content
        assert "from ." not in cli_content  # No relative imports
        
        # Check __init__.py imports
        init_file = project_dir / "src" / "alpacasay" / "__init__.py"
        init_content = init_file.read_text()
        assert "from alpacasay.alpacas import" in init_content
        assert "from alpacasay.cli import" in init_content
        assert "from alpacasay.formatter import" in init_content
        
        # Check test imports
        test_file = project_dir / "tests" / "test_cli.py"
        test_content = test_file.read_text()
        assert "from alpacasay.cli import" in test_content
        assert "from typer.testing import CliRunner" in test_content
