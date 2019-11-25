from pkg_resources import get_distribution

try:
    __version__ = get_distribution(__package__).version
except Exception:
    __version__ = "unknown"
