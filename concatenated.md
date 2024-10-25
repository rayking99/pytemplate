tests/__init__.py
```py

```

docs/conf.py
```py
# docs/conf.py
import os
import sys
from datetime import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath("../src"))

# Project information
project = "jp"
copyright = f"{datetime.now().year}, jason pickup"
author = "jason pickup"

# The full version, including alpha/beta/rc tags
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",  # Automatically include docstrings
    "sphinx.ext.napoleon",  # Support for Google/NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.githubpages",  # Create .nojekyll file for GitHub Pages
    "sphinx.ext.intersphinx",  # Link to other project's documentation
    "sphinx_rtd_theme",  # Read The Docs theme
]

# Add any paths that contain templates here, relative to this directory
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The theme to use for HTML and HTML Help pages
html_theme = "sphinx_rtd_theme"

# Theme options
html_theme_options = {
    "navigation_depth": 4,
    "titles_only": False,
    "display_version": True,
}

# Add any paths that contain custom static files (such as style sheets)
html_static_path = ["_static"]

# Intersphinx mapping to other projects
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}

```

src/package/core.py
```py
"""Core functionality of my package."""

def hello_world() -> str:
    """Return a greeting.
    
    Returns:
        str: A friendly greeting
    """
    return "Hello, World!"
```

tests/test_core.py
```py
"""Tests for the core module."""

from jp.core import hello_world

def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"

```

src/tools/clone.py
```py
from glob import glob
from pathlib import Path
import shutil


def clone(src, dst, package_name, overwrite=False):
    replacements = {
        "jp": package_name,
        "JUSTPACKAGE": " ".join(map(str.capitalize, package_name.split("_"))),
        "my package": " ".join(package_name.split("_")),
        "package_description": "A package description",
        "package": package_name,
    }
    folders = glob(f"{src}/**/", recursive=True)
    # NOT __PYCACHE__ FOLDER
    folders = [folder for folder in folders if "__pycache__" not in folder]

    for folder in folders:
        # Create corresponding directory in destination
        dest_folder = folder.replace(src, dst)
        for key, value in replacements.items():
            dest_folder = dest_folder.replace(key, value)

        Path(dest_folder).mkdir(parents=True, exist_ok=True)

        files = glob(f"{folder}/*")
        for file in files:
            if Path(file).is_dir():
                continue  # Skip directories
            with open(file, "r") as f:
                content = f.read()

            for key, value in replacements.items():
                content = content.replace(key, value)

            dest_file = file.replace(src, dst)
            for key, value in replacements.items():
                dest_file = dest_file.replace(key, value)

            with open(dest_file, "w") as f:
                f.write(content)


if __name__ == "__main__":
    clone(
        # GET CURRENT DIRECTORY
        str(Path(__file__).parent.parent.parent),
        "/Users/jso/code/plain",
        "plain",
        overwrite=True,
    )

```

docs/index.rst
```rst
.. jp documentation master file

Welcome to jp's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   contributing
   changelog

Installation
-----------

To install jp, run this command in your terminal:

.. code-block:: console

   $ pip install jp

Usage
-----

Here's a simple example of how to use jp:

.. code-block:: python

   from jp import hello_world
   
   # Get a friendly greeting
   greeting = hello_world()
   print(greeting)

API Reference
------------

.. automodule:: jp.core
   :members:
   :undoc-members:
   :show-inheritance:

Contributing
-----------

We love your input! We want to make contributing to jp as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

Development Process
~~~~~~~~~~~~~~~~~

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code follows the project's style guidelines.
6. Issue that pull request!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

src/package/__init__.py
```py
"""Package module."""

__version__ = "0.1.0"

```

pyproject.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"


[project]
name = "jp"
version = "0.1.0"
authors = [
    { name = "jason pickup", email = "your.email@example.com" },
]
description = "A short description of your package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
    "isort>=5.0",
    "mypy>=1.0",
    "ruff>=0.0.1",
]

[tool.pytest.ini_options]
addopts = "-ra -q"
testpaths = [
    "tests",
]

[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.ruff]
select = ["E", "F", "B"]
ignore = []
line-length = 88

```

src/tools/concat.py
```py
from glob import glob
from pathlib import Path

package_name = "jp"
package_full_name = "JUSTPACKAGE"
authors = "jason pickup"
email = "a@b.c"
python_version_min = "3.8"

files = glob("**/*", recursive=True)
files = [Path(file) for file in files if file != "concat.py" and Path(file).is_file()]
# not if __pycache__ in the path
files = [file for file in files if "__pycache__" not in str(file)]
files = [file for file in files if Path(file).name != "concatenated.md"]
files = [file for file in files if Path(file).name != "README.md"]
files = [file for file in files if Path(file).name != "LICENSE"]
files = list(set(files))

concatenated = ""
for file in files:
    with open(file) as f:
        contents = f.read()
        try:
            path_from_root = file.relative_to(Path.cwd())
        except ValueError:
            path_from_root = file
        if file.suffix == ".md":
            # Indent each line of the Markdown content
            indented_contents = "\n".join(
                [f"    {line}" for line in contents.splitlines()]
            )
            concatenated += f"{path_from_root}\n```\n{indented_contents}\n```\n\n"
        else:
            if file.suffix == file.name:
                concatenated += f"{path_from_root}\n```\n{contents}\n```\n\n"
            else:
                concatenated += f"{path_from_root}\n```{file.suffix.replace('.', '')}\n{contents}\n```\n\n"
    concatenated = (
        concatenated.replace("jp", package_name)
        .replace("JUSTPACKAGE", package_full_name)
        .replace("jason pickup", authors)
        .replace("a@b.c", email)
        .replace("3.8", python_version_min)
    )

with open("concatenated.md", "w") as f:
    f.write(concatenated)

```

