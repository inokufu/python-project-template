import subprocess
import tomllib
from pathlib import Path

import pytest
import yaml


class TestTemplate:
    """Tests for the Copier template itself."""

    @staticmethod
    def run_copier(
        src_path: str | Path,
        dst_path: str | Path,
        answers: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess:
        """Run copier to generate a project.

        Args:
            src_path: Path to the template source
            dst_path: Path where the project will be generated
            answers: Dictionary of answers to template questions

        Returns:
            The completed process object from running copier
        """
        cmd = [
            "copier",
            "copy",
            "--trust",
            "--defaults",
            "--overwrite",
            str(src_path),
            str(dst_path),
        ]

        # Add answers as -d options
        if answers:
            for key, value in answers.items():
                cmd.extend(["-d", f"{key}={value}"])

        return subprocess.run(cmd, capture_output=True, text=True, check=False)

    @staticmethod
    def _verify_project(tmp_path: Path, answers: dict[str, str]) -> None:
        """Test generating a project."""
        package_name = answers["package_name"]
        min_python_version = answers["min_python_version"]

        # Check that files exist
        for file in [
            tmp_path / "pyproject.toml",
            tmp_path / "Makefile",
            tmp_path / "mkdocs.yml",
            tmp_path / "LICENSE",
            tmp_path / ".copier-answers.yml",
            tmp_path / ".editorconfig",
            tmp_path / ".env.example",
            tmp_path / ".gitignore",
            tmp_path / ".pre-commit-config.yaml",
            tmp_path / ".python-version",
            tmp_path / "src" / package_name / "__init__.py",
            tmp_path / "src" / package_name / "__main__.py",
            tmp_path / "tests" / "conftest.py",
            tmp_path / ".github" / "zizmor.yml",
            tmp_path / ".github" / "ISSUE_TEMPLATE" / "bug.md",
            tmp_path / ".github" / "ISSUE_TEMPLATE" / "feature_request.md",
            tmp_path / ".github" / "ISSUE_TEMPLATE" / "question.md",
            tmp_path / ".github" / "PULL_REQUEST_TEMPLATE.md",
            tmp_path / ".github" / "workflows" / "ci.yml",
            tmp_path / "docs" / "CHANGELOG.md",
            tmp_path / "docs" / "CODE_OF_CONDUCT.md",
            tmp_path / "docs" / "CONTRIBUTING.md",
            tmp_path / "docs" / "README.md",
            tmp_path / "docs" / "SECURITY.md",
        ]:
            assert file.exists(), f"File {file} does not exist"

        # Check content of pyproject.toml
        with (tmp_path / "pyproject.toml").open("rb") as f:
            pyproject = tomllib.load(f)

        assert pyproject["project"]["name"] == package_name
        assert pyproject["project"]["description"] == answers["project_description"]
        assert pyproject["project"]["authors"] == [
            {"name": answers["author_name"], "email": answers["author_email"]}
        ]
        assert pyproject["project"]["requires-python"] == f">= {min_python_version}"
        assert pyproject["tool"]["ruff"]["target-version"] == "py{}".format(
            min_python_version.replace(".", "")
        )

        # Check content of mkdocs.yml
        with (tmp_path / "mkdocs.yml").open() as f:
            mkdocs = yaml.safe_load(f)

        assert mkdocs["site_name"] == answers["project_name"]

        # Check content of README.md
        readme = (tmp_path / "docs" / "README.md").read_text()

        assert readme.startswith(f"# {answers['project_name']}\n")
        assert f"\n{answers['project_description']}\n" in readme
        assert f"- Python {min_python_version} or higher\n" in readme

        # Check content of .python-version
        assert (tmp_path / ".python-version").read_text().strip() == min_python_version

    def test_default_generation(self, template_path: Path, tmp_path: Path) -> None:
        """Test generating a project with default answers (see copier.yaml)."""
        result = self.run_copier(
            src_path=template_path, dst_path=tmp_path, answers=None
        )
        assert result.returncode == 0, f"Copier failed: {result.stderr}"

        default_answers = {
            "project_name": "Python project",
            "package_name": "python_project",
            "project_description": "A Python project",
            "author_name": "Inokufu",
            "author_email": "contact@inokufu.com",
            "min_python_version": "3.14",
        }
        self._verify_project(tmp_path=tmp_path, answers=default_answers)

    def test_custom_generation(
        self, template_path: Path, tmp_path: Path, answers: dict[str, str]
    ) -> None:
        """Test generating a project with custom answers (see conftest.py)."""
        result = self.run_copier(
            src_path=template_path, dst_path=tmp_path, answers=answers
        )
        assert result.returncode == 0, f"Copier failed: {result.stderr}"

        self._verify_project(tmp_path=tmp_path, answers=answers)

    def test_special_characters(
        self, template_path: Path, tmp_path: Path, answers: dict[str, str]
    ) -> None:
        """Test that special characters in answers produce valid generated files."""
        special_answers = answers | {
            "project_name": 'Test "quoted" project',
            "project_description": "Test with 'quotes' and \"double quotes\"",
            "author_name": "O'C\\onnor",
        }

        # Generate project
        result = self.run_copier(template_path, tmp_path, special_answers)
        assert result.returncode == 0, f"Copier failed: {result.stderr}"

        # Check that pyproject.toml parses and holds the answers verbatim
        with (tmp_path / "pyproject.toml").open("rb") as f:
            pyproject = tomllib.load(f)

        description = special_answers["project_description"]
        assert pyproject["project"]["description"] == description
        assert (
            pyproject["project"]["authors"][0]["name"] == special_answers["author_name"]
        )

        # Check that mkdocs.yml parses and holds the answers verbatim
        with (tmp_path / "mkdocs.yml").open() as f:
            mkdocs = yaml.safe_load(f)

        assert mkdocs["site_name"] == special_answers["project_name"]

    def test_invalid_package_name(self, template_path: Path, tmp_path: Path) -> None:
        """Test that a package name which is not an identifier is rejected."""
        result = self.run_copier(
            src_path=template_path,
            dst_path=tmp_path,
            answers={"package_name": "123abc"},
        )

        assert result.returncode != 0
        assert "valid Python identifier" in result.stderr

    @pytest.mark.parametrize("version", ["3.14.3", "3.9", "2.7", "abc"])
    def test_invalid_python_version(
        self, template_path: Path, tmp_path: Path, version: str
    ) -> None:
        """Test that an unsupported Python version is rejected."""
        result = self.run_copier(
            src_path=template_path,
            dst_path=tmp_path,
            answers={"min_python_version": version},
        )

        assert result.returncode != 0
        assert "must be 3.10 or higher" in result.stderr
