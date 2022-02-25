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

    def get_users(self):
        op = Operation(schema.Query)

        users = op.users()
        users.nodes().id()
        users.nodes().first_name()
        users.nodes().last_name()
        users.nodes().created_at()
        users.nodes().is_robot()
        users.nodes().description()
        users.nodes().edge_nodes().nodes().client_id()

        data = self.run(op)

        return (op + data).users.nodes

    def my_roles(self):
        op = Operation(schema.Query)

        roles = op.my_roles()
        roles.nodes().role_name()

        data = self.run(op)

        return (op + data).my_roles.nodes

    def grant_role(self, user_id: str, role: str):
        op = Operation(schema.Mutation)

        grant_input = schema.GrantUserRoleInput()
        grant_input.user_id = user_id
        grant_input.role_name = role

        grant_user_role = op.grant_user_role(input=grant_input)

        grant_user_role.client_mutation_id()

        self.run(op)

        return True

    def create_robot_user(self, description: str):
        op = Operation(schema.Mutation)

        robot_input = schema.CreateRobotUserInput()
        robot_input.description = description

        create_robot_user = op.create_robot_user(input=robot_input)

        create_robot_user.user().id()
        create_robot_user.user().first_name()
        create_robot_user.user().last_name()
        create_robot_user.user().description()

        data = self.run(op)

        return (op + data).create_robot_user.user

    def get_sources(self, slug: str = None, source_type_id: str = None):
        op = Operation(schema.Query)

        filters = {}
        if slug:
            filters['slug'] = slug
        if source_type_id:
            filters['source_type_id'] = source_type_id

        sources = op.sources(condition=filters)
        query = sources.nodes()
        query.slug()
        query.name()
        query.source_type().slug()

        data = self.run(op)

        return (op + data).sources.nodes

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

    def create_source_type(self, slug: str, name: str) -> schema.SourceType:
        op = Operation(schema.Mutation)

        type_input = schema.CreateSourceTypeInput()
        type_record = schema.SourceTypeInput()
        type_record.slug = slug
        type_record.name = name

        type_input.source_type = type_record

        create_source_type = op.create_source_type(input=type_input)

        create_source_type.source_type().slug()
        create_source_type.source_type().name()

        data = self.run(op)

        return (op + data).create_source_type.source_type

    def create_source(self, slug: str, name: str, source_type_id: str) -> schema.Source:
        op = Operation(schema.Mutation)

        source_input = schema.CreateSourceInput()
        source_input_record = schema.SourceInput()
        source_input_record.slug = slug
        source_input_record.name = name
        source_input_record.source_type_id = source_type_id

        source_input.source = source_input_record

        create_source = op.create_source(input=source_input)

        create_source.source().slug()
        create_source.source().name()
        create_source.source().source_type_id()

        data = self.run(op)

        return (op + data).create_source.source

    def create_source_channel(self, name: str, source_slug: str, description: str = None) -> schema.SourceChannel:
        op = Operation(schema.Mutation)

        channel_input = schema.CreateSourceChannelInput()
        channel_input_record = schema.SourceChannelInput()
        channel_input_record.name = name
        channel_input_record.source_slug = source_slug
        channel_input_record.description = description

        channel_input.source_channel = channel_input_record

        create_channel = op.create_source_channel(input=channel_input)

        create_channel.source_channel().name()
        create_channel.source_channel().source_slug()
        create_channel.source_channel().description()

        data = self.run(op)

        return (op + data).create_source_channel.source_channel

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

