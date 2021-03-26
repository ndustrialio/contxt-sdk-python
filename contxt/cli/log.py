import logging

from click import echo, style

VERBOSITY = {0: "error", 1: "info", 2: "debug"}


class ClickHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            echo(self.format(record), err=True)
        except Exception:
            self.handleError(record)


class ClickFormattter(logging.Formatter):
    STYLES = {
        "debug": dict(fg="blue"),
        "info": dict(fg="green"),
        "warning": dict(fg="yellow"),
        "error": dict(fg="red"),
        "critical": dict(fg="red"),
        "exception": dict(fg="bright_red"),
    }

    def format(self, record: logging.LogRecord) -> str:
        if not record.exc_info:
            msg = record.getMessage()
            level = record.levelname.lower()
            if level in self.STYLES:
                prefix = style(f"{level.capitalize()}: ", **self.STYLES[level])  # type: ignore
                msg = "\n".join(prefix + x for x in msg.splitlines())
            return msg
        return super().format(record)


def init(level: int) -> None:
    logger = logging.getLogger()
    handler = ClickHandler()
    handler.formatter = ClickFormattter()
    log_level = getattr(logging, VERBOSITY.get(level, "error").upper())
    logger.setLevel(log_level)
    logger.handlers = [handler]
    logger.propagate = False
