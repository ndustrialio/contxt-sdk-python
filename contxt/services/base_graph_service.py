from typing import Optional

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from contxt.auth import Auth
from contxt.services.api import ApiEnvironment, ConfiguredApi


class BaseGraphService(ConfiguredApi):

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://ndustrial.api.ndustrial.io/graphql",
            client_id="vtiZlMRo4apDvThTRiH7kLifQXWUdi9j",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://ndustrial.api.staging.ndustrial.io/graphql",
            client_id="vhGxildn8hRRWZj49y18BGtbjTkFHcTG",
        ),
    )

    org_id_slugs = {
        "18d8b68e-3e59-418e-9f23-47b7cd6bdd6b": "genan",
        "02efa741-a96f-4124-a463-ae13a704b8fc": "lineage",
        "2fe29680-fc3d-4888-9e9b-44be1e59c22c": "sfnt",
        "5209751f-ea46-4b3e-a5dd-b8d03311b791": "ndustrial",
    }

    def __init__(self, auth: Auth, env: str):
        super().__init__(env, auth)
        self.token_provider = auth.get_token_provider(self.client_id)
        self.url = self.base_url

    def _get_endpoint(self, org_id: Optional[str] = None):
        org_slug = self.org_id_slugs.get(org_id, None)  # type: ignore
        if org_slug is None:
            raise Exception("No valid mapping of Organization ID to Nionic tenant")
        split = self.url.split("ndustrial.api")
        self.url = (split[0] + org_slug + ".api" + split[1]).rstrip("/")
        return HTTPEndpoint(self.url, {"Authorization": f"Bearer {self.token_provider.access_token}"})

    def run(self, op: Operation, org_id: Optional[str] = None):
        data = self._get_endpoint(org_id)(op)

        if "errors" in data:
            print(data)
            raise Exception(data["errors"][0]["message"])

        return data
