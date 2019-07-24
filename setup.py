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

# Import readme (make sure its declared in MANIFEST.in)
try:
    with open(os.path.join(here, "README.md")) as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = about["__description__"]


class PublishCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Remove old builds
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        # Build
        self.status("Building distribution...")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        # Upload
        self.status("Uploading to PyPI...")
        os.system("twine upload dist/*")

        # Tag
        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push origin v{0}".format(about["__version__"]))

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
    # Python requirement
    python_requires=">=3.6.0",
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["contxt=contxt.__main__:main"]},
    install_requires=[
        # Requirements
        "argcomplete",
        "auth0-python>=3",
        "dash-core-components",
        "dash-html-components",
        "dash",
        "inflect",
        "jwt",
        "pandas",
        "plotly",
        "python-dateutil",
        "python-jose-cryptodome",
        "pytz",
        "requests",
        "setuptools",
        "tabulate",
        "tqdm",
        "tzlocal",
    ],
    extras_require={
        # Optional requirements
        "dev": ["black", "flake8", "isort", "mypy", "pytest"]
    },
    include_package_data=True,
    license=about["__license__"],
    classifiers=[
        # Trove classifiers: https://pypi.org/pypi?:action=list_classifiers
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        # $ python setup.py publish
        # NOTE: requires twine ($ pip install twine)
        "publish": PublishCommand
    },
)
