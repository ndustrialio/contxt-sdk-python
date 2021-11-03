from sgqlc.operation import Operation

from contxt.services.api import ApiEnvironment, EnvironmentException
from contxt.services.base_graph_service import BaseGraphService
from contxt.services.base.base_schema import base as schema

ENVS = {
    'staging': ApiEnvironment(
        name="staging",
        base_url="https://contxt-dev.staging.lineageapi.com/graphql",
        client_id="https://contxt-dev.staging.lineageapi.com/",
        auth_provider='contxt.auth0.com'
    ),
    'local': ApiEnvironment(
        name="local",
        base_url="http://localhost:3000/graphql",
        client_id="local",
        auth_required=False
    )
}


class BaseService(BaseGraphService):

    def __init__(self, client_id: str, client_secret: str, env='local'):
        if not ENVS.get(env):
            raise EnvironmentException('Environment not found')
        super().__init__(client_id=client_id, client_secret=client_secret,
                         api_environment=ENVS.get(env), service_name='base')

    def get_sources(self, slug: str = None):
        op = Operation(schema.Query)

        if slug:
            print(slug)
            query = op.sources(slug=slug)
        else:
            sources = op.sources()
            query = sources.nodes()

        query.slug()
        query.name()
        query.source_type().slug()

        data = self._get_endpoint()(op)

        if slug:
            sources = (op + data).source
        else:
            sources = (op + data).sources.nodes

        return sources

    def get_channels(self, source_slug: str, with_cursors: bool = True):
        op = Operation(schema.Query)

        filters = {
            'sourceSlug': source_slug
        }

        print(source_slug)
        query = op.source_channels(condition=filters).nodes()

        query.name()
        query.description()
        query.source_slug()

        if with_cursors:
            query.cursor().channel_cursor()

        data = self._get_endpoint()(op)

        channels = (op + data).source_channels.nodes

        return channels

    def set_channel_cursor(self, source_slug: str, channel_name: str, cursor: int):
        op = Operation(schema.Mutation)

        cursor_input = schema.UpsertChannelCursorInput()
        cursor_input_record = schema.UpsertChannelCursorInputRecordInput()
        cursor_input_record.sourceslug = source_slug
        cursor_input_record.sourcechannel = channel_name
        cursor_input_record.cursorvalue = str(cursor)

        cursor_input.upsert_input = cursor_input_record

        cursor_upsert = op.upsert_channel_cursor(input=cursor_input)

        cursor_upsert.source_channel_cursor().id()
        cursor_upsert.source_channel_cursor().channel_cursor()

        data = self._get_endpoint()(op)
        if 'errors' in data:
            print(data)
            raise Exception(data['errors'][0]['message'])

        updated_cursor = (op + data).upsert_channel_cursor.source_channel_cursor
        return updated_cursor

