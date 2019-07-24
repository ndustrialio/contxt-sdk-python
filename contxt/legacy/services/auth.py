from contxt.legacy.services import POST, ApiRequest, Service
from contxt.utils import make_logger

CONFIGS_BY_ENVIRONMENT = {
    "production": {
        "base_url": "https://contxtauth.com",
        "audience": "75wT048QcpE7ujwBJPPjr263eTHl4gEX",
    }
}

logger = make_logger(__name__)


class AuthConfigurationError(Exception):
    pass


class ContxtAuthService(Service):
    """
    Service to interact with our Contxt Auth API.
    """

    def __init__(
        self, access_token, client_id=None, client_secret=None, environment="production"
    ):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception("Invalid environment specified")

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        # can imply if access_token is none, then we need to use
        # client_id/client_secret to get tokens
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

        if self.access_token is None:
            logger.info("Implying machine-based authentication")

            if self.client_id is None or self.client_secret is None:
                raise AuthConfigurationError(
                    "Misconfiguration authentication. When implying machine-based "
                    "authentication client_id and client_secret must be provided"
                )

        super().__init__(base_url=self.env["base_url"], access_token=access_token)

    def get_new_token_for_audience(self, audience):

        if not self.client_id:
            body = {"audiences": [audience]}

            response = self.execute(
                POST(uri="token")
                .body(body)
                .content_type(ApiRequest.URLENCODED_CONTENT_TYPE),
                execute=True,
            )

            return response["access_token"]

        else:

            body = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "audience": audience,
                "grant_type": "client_credentials",
            }

            response = self.execute(
                POST(uri="oauth/token")
                .body(body)
                .content_type(ApiRequest.URLENCODED_CONTENT_TYPE)
                .authorize(False),
                execute=True,
            )

            return response["access_token"]
