try:
    from pkg_resources import get_distribution  # implicit dependency on setuptools

    __version__ = get_distribution("contxt-sdk").version
except Exception:
    __version__ = "unknown"
