try:
    from importlib.metadata import version

    __version__ = version("contxt-sdk")
except Exception:
    __version__ = "unknown"
