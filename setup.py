#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the "publish" functionality of this file, you must:
#   $ pip install twine

import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Python requirement
REQUIRES_PYTHON = ">=3.6.0"

# Requirements
REQUIRED = [
    "argcomplete",
    "auth0-python",
    "dash-core-components",
    "dash-html-components",
    "dash",
    "inflect",
    "pandas",
    "plotly",
    "pyjwt",
    "python-dateutil",
    "pytz",
    "requests",
    "setuptools",
    "tabulate",
    "tqdm",
    "tzlocal",
]

# Optional requirements
EXTRAS = {
    "dev": ["mypy", "pytest"],
}

###############################################################################

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
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of "packages":
    # py_modules=[NAME],
    entry_points={
        "console_scripts": ["contxt=contxt.__main__:main"],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=about["__license__"],
    classifiers=[
        # Trove classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        # $ python setup.py publish
        "publish": PublishCommand,
    },
)
