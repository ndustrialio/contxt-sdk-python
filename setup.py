#!/usr/bin/env python
# Modified from https://github.com/kennethreitz/setup.py

import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Import __version__.py
about = {}
with open(os.path.join(here, "contxt", "__version__.py")) as f:
    exec(f.read(), about)

# Import readme
with open(os.path.join(here, "README.md")) as f:
    long_description = "\n" + f.read()


class PublishCommand(Command):
    """Support `python setup.py publish`."""

    description = "Build and publish the package."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Check for twine
        try:
            import twine  # noqa: F401
        except ImportError:
            print("ERROR: Publishing requires twine (run `pip install twine`)")
            sys.exit(1)

        # Remove old builds
        print("Removing previous builds...")
        try:
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        # Build
        print("Building distribution...")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        # Upload
        print("Uploading to PyPI...")
        os.system("twine upload dist/*")

        # Tag
        print("Pushing git tags...")
        os.system(f"git tag v{about['__version__']}")
        os.system(f"git push origin v{about['__version__']}")

        sys.exit()


setup(
    # Package metadata
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    # Python requirement
    python_requires=">=3.6.0",
    packages=find_packages(include=("contxt*",)),
    entry_points={"console_scripts": ["contxt=contxt.__main__:main"]},
    install_requires=[
        # Requirements
        "argcomplete",
        "auth0-python>=3",
        "dataclasses;python_version<'3.7'",
        "pyjwt",
        "python-dateutil",
        "pytz",
        "requests",
        "tabulate",
        "tqdm",
        "tzlocal",
    ],
    extras_require={
        # Optional requirements
        "dev": ["black", "flake8", "isort", "mypy", "pytest", "twine"],
        "plotly": ["dash-core-components", "dash-html-components", "dash", "plotly"],
        "server": ["python-jose-cryptodome"],
    },
    include_package_data=True,
    classifiers=[
        # Trove classifiers: https://pypi.org/pypi?:action=list_classifiers
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        # $ python setup.py publish
        "publish": PublishCommand
    },
)
