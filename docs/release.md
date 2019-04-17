# Release Guide
To publish a new version of the package to [PyPI](https://pypi.org/project/contxt-sdk/), follow these steps:

1. Make sure you are on the `master` branch
1. Increment `__version__` in [`__version__.py`](https://github.com/ndustrialio/contxt-sdk-python/blob/master/contxt/__version__.py)
1. Commit the change
1. Run `python setup.py publish` (authenticating to PyPI when requested)