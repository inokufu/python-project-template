import shutil
import subprocess
from pathlib import Path

import pytest


class TestCommands:
    """Tests for the commands in generated projects."""

    @staticmethod
    def run_make_command(
        project_dir: Path, command: str, expected_returncode: int = 0
    ) -> subprocess.CompletedProcess:
        """Run a make command in the generated project.

        Args:
            project_dir: Path to the generated project
            command: The make command to run
            expected_returncode: Expected return code (0 for success)

        Returns:
            The completed process object from running the command

        Raises:
            AssertionError: If the command fails with an unexpected return code
        """
        # Run the make command
        result = subprocess.run(
            ["make", command],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == expected_returncode, (
            f"Command 'make {command}' failed with code {result.returncode}: {result.stderr}"
        )

        return result

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_check_uv(self, generated_project: Path) -> None:
        """Test that 'make check-uv' works."""
        self.run_make_command(generated_project, "check-uv")

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_install(self, generated_project: Path) -> None:
        """Test that 'make install' works."""
        self.run_make_command(generated_project, "install")

        assert (generated_project / ".venv").is_dir()
        assert (generated_project / "uv.lock").is_file()

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_init(self, generated_project: Path) -> None:
        """Test that 'make init' works."""
        self.run_make_command(generated_project, "init")

        assert (generated_project / ".git" / "hooks" / "pre-commit").is_file()

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_precommit(self, generated_project: Path) -> None:
        """Test that 'make precommit' works after initialization."""
        self.run_make_command(generated_project, "init")
        self.run_make_command(generated_project, "precommit")

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_test(self, generated_project: Path) -> None:
        """Test that 'make test' works on a freshly generated project."""
        self.run_make_command(generated_project, "test")

        assert (generated_project / "coverage.xml").is_file()

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_diff_cover_without_remote(self, generated_project: Path) -> None:
        """Test that 'make diff-cover' skips when there is no origin/main to compare."""
        # Only its existence is checked when there is nothing to compare
        (generated_project / "coverage.xml").touch()
        result = self.run_make_command(generated_project, "diff-cover")

        assert "No origin/main" in result.stdout

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_build(self, generated_project: Path) -> None:
        """Test that 'make build' works."""
        self.run_make_command(generated_project, "build")

        dist = generated_project / "dist"
        assert list(dist.glob("*.whl"))
        assert list(dist.glob("*.tar.gz"))

    @pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
    def test_make_docs(self, generated_project: Path) -> None:
        """Test that 'make docs' works."""
        self.run_make_command(generated_project, "docs")

        assert (generated_project / "site" / "index.html").is_file()
