from sgqlc.operation import Operation

from contxt.services.base_graph_service import BaseGraphService, SchemaMissingException

try:
    from contxt.schemas.nionic.nionic_schema import nionic as schema
    from contxt.schemas.nionic.nionic_schema import Facility
except ImportError:
    raise SchemaMissingException('[ERROR] Schema is not generated for GraphQL -- run `contxt init` to '
                                 'initialize then re-run the command')

from contxt.utils.config import ContxtEnvironmentConfig


class NionicService(BaseGraphService):

    def __init__(self, contxt_env: ContxtEnvironmentConfig):
        super().__init__(contxt_env)

    def get_facilities(self):
        op = Operation(schema.Query)

        facilities = op.facilities()
        query = facilities.nodes()

        query.id()
        query.name()

        data = self.run(op)

        facilities = (op + data).facilities

        return facilities
