import sgqlc.types
import sgqlc.operation
from . import nionic_schema

_schema = nionic_schema
_schema_root = _schema.nionic_schema

__all__ = ('Operations',)


def mutation_create_facility():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='createFacility', variables=dict(name=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), slug=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), timezoneName=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_create_facility = _op.create_facility(input={'facility': {'name': sgqlc.types.Variable('name'), 'slug': sgqlc.types.Variable('slug'), 'timezoneName': sgqlc.types.Variable('timezoneName')}})
    _op_create_facility_facility = _op_create_facility.facility()
    _op_create_facility_facility.id()
    return _op


class Mutation:
    create_facility = mutation_create_facility()


def query_facilities():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='facilities')
    _op_facilities = _op.facilities()
    _op_facilities_nodes = _op_facilities.nodes()
    _op_facilities_nodes.id()
    _op_facilities_nodes.name()
    _op_facilities_nodes.slug()
    _op_facilities_nodes.address()
    _op_facilities_nodes.city()
    _op_facilities_nodes.state()
    _op_facilities_nodes.zip()
    _op_facilities_nodes.timezone_name()
    return _op


def query_metric_labels():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='metricLabels')
    _op_source_labels = _op.source_labels()
    _op_source_labels.source_id()
    _op_source_labels.label()
    return _op


def query_main_services():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='mainServices', variables=dict(facilityId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.Int))))
    _op_main_services = _op.main_services(filter={'facilityId': {'equalTo': sgqlc.types.Variable('facilityId')}})
    _op_main_services_nodes = _op_main_services.nodes()
    _op_main_services_nodes.id()
    _op_main_services_nodes.facility_id()
    _op_main_services_nodes.name()
    _op_main_services_nodes.type()
    _op_main_services_nodes_usage = _op_main_services_nodes.usage()
    _op_main_services_nodes_usage.id()
    _op_main_services_nodes_usage.data_source_name()
    _op_main_services_nodes_usage.name()
    _op_main_services_nodes_usage.alias()
    _op_main_services_nodes_usage.data_type()
    _op_main_services_nodes_demand = _op_main_services_nodes.demand()
    _op_main_services_nodes_demand.id()
    _op_main_services_nodes_demand.data_source_name()
    _op_main_services_nodes_demand.name()
    _op_main_services_nodes_demand.alias()
    _op_main_services_nodes_demand.data_type()
    _op_main_services_nodes.created_at()
    _op_main_services_nodes.updated_at()
    return _op


class Query:
    facilities = query_facilities()
    main_services = query_main_services()
    metric_labels = query_metric_labels()


class Operations:
    mutation = Mutation
    query = Query
