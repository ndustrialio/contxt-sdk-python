from sgqlc.types import Arg, Enum, Field, Input, Int, String, Type, list_of, non_null
from sgqlc.types.relay import Node


class Facility(Type, Node):
    id = Field(non_null(Int), graphql_name="id")
    name = Field(non_null(String), graphql_name="name")
    slug = Field(non_null(String), graphql_name="slug")
    address = Field(String, graphql_name="address")
    city = Field(String, graphql_name="city")
    state = Field(String, graphql_name="state")
    zip = Field(String, graphql_name="zip")
    timezone_name = Field(String, graphql_name="timezoneName")


class FacilitiesConnection(Type, Node):
    nodes = list_of(Facility)


class FacilityInput(Input):
    name = non_null(str)
    slug = non_null(str)
    timezone_name = non_null(str)


class CreateFacilityInput(Input):
    facility = Field(non_null("FacilityInput"), graphql_name="facility")


class CreateFacilityPayload(Type):
    facility = Field("Facility", graphql_name="facility")


class MetricLabel(Type):
    source_id = non_null(str)
    label = non_null(str)


class MetricDataAggregationMethod(Enum):
    __choices__ = ("AVG", "COUNT", "FIRST", "LAST", "MAX", "MEDIAN", "MIN", "SUM")


class MetricDataOrderBy(Enum):
    __choices__ = ("TIME_ASC", "TIME_DESC")


class MetricData(Type, Node):
    time = non_null(str)
    source_id = Field(non_null(str), graphql_name="sourceId")
    label = str
    data = str
    metadata = str


class MetricDataConnection(Type, Node):
    nodes = list_of(MetricData)


class Query(Type):
    facilities = Field(FacilitiesConnection)
    metric_labels = Field(non_null(list_of(non_null(MetricLabel))), graphql_name="metricLabels")
    metric_data = Field(
        MetricDataConnection,
        graphql_name="metricData",
        args={
            "source_id": Arg(non_null(str), graphql_name="sourceId", default=None),
            "label": Arg(non_null(str), graphql_name="label", default=None),
        },
    )


class Mutation(Type):
    create_facility = Field(
        CreateFacilityPayload,
        graphql_name="createFacility",
        args={"input": Arg(non_null(CreateFacilityInput))},
    )
