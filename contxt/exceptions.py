class UnauthorizedException(Exception):
    pass


class OrganizationNotFoundException(Exception):
    pass


class OrganizationArgumentException(Exception):
    pass


class ChannelArgumentException(Exception):
    pass


class ChannelNotFoundException(Exception):
    pass


class WorkerConfigurationError(Exception):
    pass
