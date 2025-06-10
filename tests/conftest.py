"""This file contains pytest fixtures available to all tests."""

import pytest
from pathlib import Path


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
