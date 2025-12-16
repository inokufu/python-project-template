import os
import subprocess
from pathlib import Path


class TestTemplate:
    """Tests for the Copier template itself."""

    @staticmethod
    def run_copier(
        src_path: str | Path | None,
        dst_path: str | Path,
        answers: dict[str, str] | None = None,
        update: bool = False,
    ) -> subprocess.CompletedProcess:
        """Run copier to generate or update a project.

        Args:
            src_path: Path to the template source
            dst_path: Path where the project will be generated
            answers: Dictionary of answers to template questions
            update: Whether to update an existing project

        Returns:
            The completed process object from running copier
        """
        if update:
            cmd = ["copier", "update", "--trust", "--defaults"]
            cwd = str(dst_path)
        else:
            cmd = [
                "copier",
                "copy",
                "--trust",
                "--defaults",
                "--overwrite",
                str(src_path),
                str(dst_path),
            ]
            cwd = None

        # Add answers as -d options
        if answers and not update:
            for key, value in answers.items():
                cmd.extend(["-d", f"{key}={value}"])

        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        return result

    @staticmethod
    def _verify_project(tmp_path: Path, answers: dict[str, str]) -> None:
        """Test generating a project."""
        package_name = answers.get("package_name")

        # Check that files exist
        for file in [
            tmp_path / "pyproject.toml",
            tmp_path / "Makefile",
            tmp_path / "tests",
            tmp_path / "LICENSE",
            tmp_path / ".editorconfig",
            tmp_path / ".gitignore",
            tmp_path / ".pre-commit-config.yaml",
            tmp_path / "src" / package_name / "__init__.py",
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
        with open(tmp_path / "pyproject.toml") as f:
            content = f.read()
            assert package_name in content
            assert answers["project_description"] in content
            assert answers["author_name"] in content
            assert answers["author_email"] in content
            assert answers["min_python_version"] in content

        # Check content of README.md
        with open(tmp_path / "docs" / "README.md") as f:
            content = f.read()
            assert answers["project_name"] in content
            assert answers["project_description"] in content
            assert answers["min_python_version"] in content

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

    def test_update_preserves_source(
        self, template_path: Path, tmp_path: Path, answers: dict[str, str]
    ) -> None:
        """Test that updating a project preserves source code."""
        # Generate initial project
        result = self.run_copier(
            src_path=template_path, dst_path=tmp_path, answers=answers
        )
        assert result.returncode == 0, f"Initial generation failed: {result.stderr}"

        # Add a custom file to the src directory
        custom_file = tmp_path / "src" / "test_project" / "custom.py"
        custom_file.write_text("# Custom source file")

        # Update the project
        os.environ["COPIER_ANSWERS_FILE"] = str(tmp_path / ".copier-answers.yml")
        self.run_copier(src_path=None, dst_path=tmp_path, update=True)

        # Check that the custom file still exists
        assert custom_file.exists()
        assert custom_file.read_text() == "# Custom source file"

    def test_special_characters(
        self, template_path: Path, tmp_path: Path, answers: dict[str, str]
    ) -> None:
        """Test generating a project with special characters in inputs."""
        # Modify answers to include special characters
        answers["project_description"] = "Test with 'quotes' and \"double quotes\""
        answers["author_name"] = "O'Connor"

        # Generate project
        result = self.run_copier(template_path, tmp_path, answers)
        assert result.returncode == 0, f"Copier failed: {result.stderr}"

        # Check content in pyproject.toml
        with open(tmp_path / "pyproject.toml") as f:
            content = f.read()
            assert "Test with 'quotes' and \"double quotes\"" in content
            assert "O'Connor" in content
