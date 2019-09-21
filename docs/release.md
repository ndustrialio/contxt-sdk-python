# Release Guide
To publish a new version to [PyPI](https://pypi.org/project/contxt-sdk/), follow these steps:

```bash
# Bump version (creates commit and tag)
$ make version v=[major|minor|patch|build]

# Publish (authenticating when prompted)
$ make publish
```