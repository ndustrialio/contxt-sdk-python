from sgqlc.operation import Operation

from contxt.services.base_graph_service import BaseGraphService, SchemaMissingException

try:
    from contxt.schemas.foundry_graph.foundry_graph_schema import foundry_graph as schema
except ImportError:
    raise SchemaMissingException('[ERROR] Schema is not generated for GraphQL -- run `contxt init` to '
                                 'initialize then re-run the command')

from contxt.utils.config import ContxtEnvironmentConfig


class BaseService(BaseGraphService):

    def __init__(self, contxt_env: ContxtEnvironmentConfig):
        super().__init__(contxt_env)

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

        data = self.run(op)

        if slug:
            sources = (op + data).source
        else:
            sources = (op + data).sources.nodes

        return sources

    def get_channels_by_source_type(self, source_type_id: str, with_cursors: bool = True):
        op = Operation(schema.Query)

        filters = {
            'sourceTypeId': source_type_id
        }

        print(source_type_id)
        source_nodes = op.sources(condition=filters).nodes()

        source_nodes.slug()
        source_channels = source_nodes.source_channels_by_source_slug().nodes()
        source_channels.name()
        source_channels.description()
        source_channels.source_slug()

        if with_cursors:
            source_channels.cursor().channel_cursor()

        data = self.run(op)

        channels = (op + data).sources.nodes

        return channels

    def get_channels(self, source_slug: str, with_cursors: bool = True):
        op = Operation(schema.Query)

        filters = {
            'sourceSlug': source_slug
        }

        query = op.source_channels(condition=filters).nodes()

        query.name()
        query.description()
        query.source_slug()

        if with_cursors:
            query.cursor().channel_cursor()
        data = self.run(op)

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

        data = self.run(op)
        if 'errors' in data:
            print(data)
            raise Exception(data['errors'][0]['message'])

        updated_cursor = (op + data).upsert_channel_cursor.source_channel_cursor
        return updated_cursor

