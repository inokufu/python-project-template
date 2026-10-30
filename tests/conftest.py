"""This file contains pytest fixtures available to all tests."""

import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def template_path() -> Path:
    """Return the path to the template (current directory)."""
    return Path.cwd()


@pytest.fixture(scope="session")
def answers() -> dict[str, str]:
    """Fixed answers for template questions."""
    return {
        "project_name": "Test Project",
        "package_name": "test_project",
        "project_description": "A test project",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "min_python_version": "3.13",
    }


@pytest.fixture(scope="session")
def generated_project(
    tmp_path_factory: pytest.TempPathFactory,
    template_path: Path,
    answers: dict[str, str],
) -> Path:
    """Generate a project once and reuse it for multiple tests.

    Args:
        tmp_path_factory: Pytest factory for temporary directories
        template_path: Path to the template
        answers: Default answers for template questions

    Returns:
        Path to the generated project
    """
    project_dir = tmp_path_factory.mktemp("project")

    # Run copier to generate a project
    cmd = [
        "copier",
        "copy",
        "--trust",
        "--force",
        str(template_path),
        str(project_dir),
    ]
    for key, value in answers.items():
        cmd.extend(["-d", f"{key}={value}"])

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    assert result.returncode == 0, f"Copier failed: {result.stderr}"

    # Track files: prek only checks what git knows about
    subprocess.run(["git", "init"], cwd=project_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=project_dir, check=True)
    return project_dir
