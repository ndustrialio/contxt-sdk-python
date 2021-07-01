import sgqlc.types
import sgqlc.types.relay


control_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
control_schema -= sgqlc.types.relay.Node
control_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class ControlEventLogsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'EVENT_TIME_ASC', 'EVENT_TIME_DESC', 'BY_USER_ID_ASC', 'BY_USER_ID_DESC', 'BY_EDGE_NODE_ID_ASC', 'BY_EDGE_NODE_ID_DESC', 'CONTROL_EVENT_ID_ASC', 'CONTROL_EVENT_ID_DESC', 'PREVIOUS_STATE_ASC', 'PREVIOUS_STATE_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'LABEL_ASC', 'LABEL_DESC', 'EVENT_TYPE_ASC', 'EVENT_TYPE_DESC', 'DATA_ASC', 'DATA_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ControlEventMetricsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'CONTROL_EVENT_ID_ASC', 'CONTROL_EVENT_ID_DESC', 'PROJECT_SUCCESS_METRIC_ID_ASC', 'PROJECT_SUCCESS_METRIC_ID_DESC', 'PROJECTED_IMPACT_AMOUNT_ASC', 'PROJECTED_IMPACT_AMOUNT_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ControlEventStatesOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'STATE_ASC', 'STATE_DESC', 'RULES_ASC', 'RULES_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ControlEventsControlledComponentsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'CONTROL_EVENT_ID_ASC', 'CONTROL_EVENT_ID_DESC', 'CONTROLLABLE_COMPONENT_ID_ASC', 'CONTROLLABLE_COMPONENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ControlEventsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'START_TIME_ASC', 'START_TIME_DESC', 'END_TIME_ASC', 'END_TIME_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'TYPE_ASC', 'TYPE_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ControllableComponentsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'SLUG_ASC', 'SLUG_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'LABEL_ASC', 'LABEL_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'CONTROLLED_BY_EDGE_NODE_CLIENT_ID_ASC', 'CONTROLLED_BY_EDGE_NODE_CLIENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class Cursor(sgqlc.types.Scalar):
    __schema__ = control_schema


class Datetime(sgqlc.types.Scalar):
    __schema__ = control_schema


class EdgeNodesOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'CLIENT_ID_ASC', 'CLIENT_ID_DESC', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class FacilitiesOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class FacilityProjectsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'ENROLLMENT_STATUS_ASC', 'ENROLLMENT_STATUS_DESC')


class FacilityUsersOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'USER_ID_ASC', 'USER_ID_DESC', 'ROLE_ASC', 'ROLE_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = control_schema


class OrganizationsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ProjectSuccessMetricsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'NAME_ASC', 'NAME_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'UNITS_ASC', 'UNITS_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ProjectTypesOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ProjectsOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'PROJECT_TYPE_ID_ASC', 'PROJECT_TYPE_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


String = sgqlc.types.String

class UUID(sgqlc.types.Scalar):
    __schema__ = control_schema


class UsersOrderBy(sgqlc.types.Enum):
    __schema__ = control_schema
    __choices__ = ('NATURAL', 'FIRST_NAME_ASC', 'FIRST_NAME_DESC', 'LAST_NAME_ASC', 'LAST_NAME_DESC', 'EMAIL_ASC', 'EMAIL_DESC', 'PHONE_NUMBER_ASC', 'PHONE_NUMBER_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')



########################################################################
# Input Objects
########################################################################
class ChangeEventStateInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_id', 'to_state', 'comment', 'changed_by_user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    to_state = sgqlc.types.Field(sgqlc.types.non_null('ControlEventStateInput'), graphql_name='toState')
    comment = sgqlc.types.Field(String, graphql_name='comment')
    changed_by_user_id = sgqlc.types.Field(String, graphql_name='changedByUserId')


class ControlEventCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'facility_id', 'created_at', 'updated_at', 'project_id', 'type', 'current_state')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    type = sgqlc.types.Field(String, graphql_name='type')
    current_state = sgqlc.types.Field(String, graphql_name='currentState')


class ControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'facility_id', 'created_at', 'updated_at', 'project_id', 'type', 'current_state')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')


class ControlEventLogCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'control_event_id', 'previous_state', 'current_state', 'label', 'event_type', 'data')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    event_time = sgqlc.types.Field(Datetime, graphql_name='eventTime')
    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')
    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')
    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    previous_state = sgqlc.types.Field(String, graphql_name='previousState')
    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    label = sgqlc.types.Field(String, graphql_name='label')
    event_type = sgqlc.types.Field(String, graphql_name='eventType')
    data = sgqlc.types.Field(JSON, graphql_name='data')


class ControlEventLogPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'control_event_id', 'previous_state', 'current_state', 'label', 'event_type', 'data')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    event_time = sgqlc.types.Field(Datetime, graphql_name='eventTime')
    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')
    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')
    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    previous_state = sgqlc.types.Field(String, graphql_name='previousState')
    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    label = sgqlc.types.Field(String, graphql_name='label')
    event_type = sgqlc.types.Field(String, graphql_name='eventType')
    data = sgqlc.types.Field(JSON, graphql_name='data')


class ControlEventMetricCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at')
    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(UUID, graphql_name='projectSuccessMetricId')
    projected_impact_amount = sgqlc.types.Field(Float, graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')
    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventMetricPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at')
    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(UUID, graphql_name='projectSuccessMetricId')
    projected_impact_amount = sgqlc.types.Field(Float, graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'facility_id', 'created_at', 'updated_at', 'project_id', 'type', 'current_state')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    type = sgqlc.types.Field(String, graphql_name='type')
    current_state = sgqlc.types.Field(String, graphql_name='currentState')


class ControlEventProposalInputRecordInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('starttime', 'endtime', 'facilityid', 'projectid')
    starttime = sgqlc.types.Field(Datetime, graphql_name='starttime')
    endtime = sgqlc.types.Field(Datetime, graphql_name='endtime')
    facilityid = sgqlc.types.Field(Int, graphql_name='facilityid')
    projectid = sgqlc.types.Field(String, graphql_name='projectid')


class ControlEventStateCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(String, graphql_name='state')
    rules = sgqlc.types.Field(JSON, graphql_name='rules')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventStateInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    rules = sgqlc.types.Field(JSON, graphql_name='rules')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventStatePatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(String, graphql_name='state')
    rules = sgqlc.types.Field(JSON, graphql_name='rules')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventsControlledComponentCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'controllable_component_id', 'created_at', 'updated_at')
    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControlEventsControlledComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'controllable_component_id', 'created_at', 'updated_at')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControllableComponentCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    label = sgqlc.types.Field(String, graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')
    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControllableComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')
    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ControllableComponentPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    label = sgqlc.types.Field(String, graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')
    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class CreateControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field(sgqlc.types.non_null(ControlEventInput), graphql_name='controlEvent')


class CreateControlEventMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_metric')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_metric = sgqlc.types.Field(sgqlc.types.non_null(ControlEventMetricInput), graphql_name='controlEventMetric')


class CreateControlEventsControlledComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_events_controlled_component')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_events_controlled_component = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsControlledComponentInput), graphql_name='controlEventsControlledComponent')


class CreateControllableComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    controllable_component = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentInput), graphql_name='controllableComponent')


class CreateEdgeNodeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    edge_node = sgqlc.types.Field(sgqlc.types.non_null('EdgeNodeInput'), graphql_name='edgeNode')


class CreateFacilityInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility = sgqlc.types.Field(sgqlc.types.non_null('FacilityInput'), graphql_name='facility')


class CreateFacilityProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_project = sgqlc.types.Field(sgqlc.types.non_null('FacilityProjectInput'), graphql_name='facilityProject')


class CreateFacilityUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_user = sgqlc.types.Field(sgqlc.types.non_null('FacilityUserInput'), graphql_name='facilityUser')


class CreateOrganizationInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInput'), graphql_name='organization')


class CreateProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('ProjectInput'), graphql_name='project')


class CreateProjectSuccessMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_success_metric = sgqlc.types.Field(sgqlc.types.non_null('ProjectSuccessMetricInput'), graphql_name='projectSuccessMetric')


class CreateProjectTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_type = sgqlc.types.Field(sgqlc.types.non_null('ProjectTypeInput'), graphql_name='projectType')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field(sgqlc.types.non_null('UserInput'), graphql_name='user')


class DeleteControlEventByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteControlEventByStartTimeAndFacilityIdAndProjectIdAndTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'start_time', 'facility_id', 'project_id', 'type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class DeleteControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteControlEventLogByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteControlEventLogInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteControlEventMetricByControlEventIdAndProjectSuccessMetricIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_id', 'project_success_metric_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')


class DeleteControlEventStateByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteControlEventStateInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')


class DeleteControllableComponentByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteControllableComponentBySlugAndFacilityIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'slug', 'facility_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')


class DeleteControllableComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteEdgeNodeByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteEdgeNodeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'client_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')


class DeleteFacilityByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteFacilityInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class DeleteFacilityUserByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteFacilityUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteOrganizationByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteOrganizationInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteProjectByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class DeleteProjectSuccessMetricByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteProjectSuccessMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class DeleteProjectTypeByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteProjectTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class DeleteUserByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')


class EdgeNodeCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'project_id', 'created_at', 'updated_at')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class EdgeNodeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'project_id', 'created_at', 'updated_at')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class EdgeNodePatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'project_id', 'created_at', 'updated_at')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityProjectCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    enrollment_status = sgqlc.types.Field(String, graphql_name='enrollmentStatus')


class FacilityProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    enrollment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='enrollmentStatus')


class FacilityUserCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    role = sgqlc.types.Field(String, graphql_name='role')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class FacilityUserPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    role = sgqlc.types.Field(String, graphql_name='role')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class OrganizationCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class OrganizationInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class OrganizationPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    project_type_id = sgqlc.types.Field(String, graphql_name='projectTypeId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    project_type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectTypeId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    project_type_id = sgqlc.types.Field(String, graphql_name='projectTypeId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectSuccessMetricCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    units = sgqlc.types.Field(String, graphql_name='units')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectSuccessMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    units = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='units')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectSuccessMetricPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    units = sgqlc.types.Field(String, graphql_name='units')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectTypeCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProjectTypePatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class ProposeControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'proposed_event', 'components_to_control')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    proposed_event = sgqlc.types.Field(sgqlc.types.non_null(ControlEventProposalInputRecordInput), graphql_name='proposedEvent')
    components_to_control = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ControllableComponentInput)), graphql_name='componentsToControl')


class RawControlEventInputRecordInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('starttime', 'endtime', 'facilityid', 'projectid', 'type', 'metrics')
    starttime = sgqlc.types.Field(Datetime, graphql_name='starttime')
    endtime = sgqlc.types.Field(Datetime, graphql_name='endtime')
    facilityid = sgqlc.types.Field(Int, graphql_name='facilityid')
    projectid = sgqlc.types.Field(String, graphql_name='projectid')
    type = sgqlc.types.Field(String, graphql_name='type')
    metrics = sgqlc.types.Field(sgqlc.types.list_of('RawControlEventMetricInputRecordInput'), graphql_name='metrics')


class RawControlEventMetricInputRecordInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('name', 'projectimpactamount')
    name = sgqlc.types.Field(String, graphql_name='name')
    projectimpactamount = sgqlc.types.Field(Float, graphql_name='projectimpactamount')


class SetControlEventsInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_input')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    event_input = sgqlc.types.Field(sgqlc.types.non_null(RawControlEventInputRecordInput), graphql_name='eventInput')


class UpdateControlEventByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventPatch), graphql_name='patch')


class UpdateControlEventByStartTimeAndFacilityIdAndProjectIdAndTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'start_time', 'facility_id', 'project_id', 'type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventPatch), graphql_name='patch')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class UpdateControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateControlEventLogByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogPatch), graphql_name='patch')


class UpdateControlEventLogInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateControlEventMetricByControlEventIdAndProjectSuccessMetricIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'control_event_id', 'project_success_metric_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventMetricPatch), graphql_name='patch')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')


class UpdateControlEventStateByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStatePatch), graphql_name='patch')


class UpdateControlEventStateInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStatePatch), graphql_name='patch')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')


class UpdateControllableComponentByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')


class UpdateControllableComponentBySlugAndFacilityIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'slug', 'facility_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')


class UpdateControllableComponentInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateEdgeNodeByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodePatch), graphql_name='patch')


class UpdateEdgeNodeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'client_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodePatch), graphql_name='patch')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')


class UpdateFacilityByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityPatch), graphql_name='patch')


class UpdateFacilityInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class UpdateFacilityUserByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityUserPatch), graphql_name='patch')


class UpdateFacilityUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityUserPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateOrganizationByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(OrganizationPatch), graphql_name='patch')


class UpdateOrganizationInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(OrganizationPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateProjectByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectPatch), graphql_name='patch')


class UpdateProjectInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class UpdateProjectSuccessMetricByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricPatch), graphql_name='patch')


class UpdateProjectSuccessMetricInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricPatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')


class UpdateProjectTypeByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectTypePatch), graphql_name='patch')


class UpdateProjectTypeInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectTypePatch), graphql_name='patch')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class UpdateUserByNodeIdInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null('UserPatch'), graphql_name='patch')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null('UserPatch'), graphql_name='patch')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')


class UserCondition(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class UserInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    phone_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phoneNumber')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')


class UserPatch(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



########################################################################
# Output Objects and Interfaces
########################################################################
class ChangeEventStatePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'facility', 'project', 'control_event_state_by_current_state', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_edge = sgqlc.types.Field('ControlEventsEdge', graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null('ControlEventLogsConnection'), graphql_name='controlEventLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null('ControlEventLogsConnection'), graphql_name='controlEventLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventControlledComponentsManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventControlledComponentsManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventControlledComponentsManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    control_events_controlled_components = sgqlc.types.Field(sgqlc.types.non_null('ControlEventsControlledComponentsConnection'), graphql_name='controlEventsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    control_event_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null('ControlEventLogsConnection'), graphql_name='controlEventLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventLogsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventLog')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventLogsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventLogsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventLog', graphql_name='node')


class ControlEventMetric(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at', 'control_event', 'project_success_metric')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')
    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')


class ControlEventMetricsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ControlEventMetric)), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventMetricsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventMetricsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(ControlEventMetric, graphql_name='node')


class ControlEventProjectSuccessMetricsByControlEventMetricControlEventIdAndProjectSuccessMetricIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectSuccessMetric')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventProjectSuccessMetricsByControlEventMetricControlEventIdAndProjectSuccessMetricIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventProjectSuccessMetricsByControlEventMetricControlEventIdAndProjectSuccessMetricIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projected_impact_amount', 'created_at', 'updated_at')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='node')
    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')


class ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    control_event_logs = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    control_event_logs = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    control_event_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    control_event_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateFacilitiesByControlEventCurrentStateAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateFacilitiesByControlEventCurrentStateAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateFacilitiesByControlEventCurrentStateAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')
    control_events = sgqlc.types.Field(sgqlc.types.non_null('ControlEventsConnection'), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateProjectsByControlEventCurrentStateAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateProjectsByControlEventCurrentStateAndProjectIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateProjectsByControlEventCurrentStateAndProjectIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')
    control_events = sgqlc.types.Field(sgqlc.types.non_null('ControlEventsConnection'), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateUsersByControlEventLogCurrentStateAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateUsersByControlEventLogCurrentStateAndByUserIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateUsersByControlEventLogCurrentStateAndByUserIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    control_event_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStateUsersByControlEventLogPreviousStateAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateUsersByControlEventLogPreviousStateAndByUserIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStateUsersByControlEventLogPreviousStateAndByUserIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    control_event_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventStatesConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStatesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventStatesEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')


class ControlEventUsersByControlEventLogControlEventIdAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventUsersByControlEventLogControlEventIdAndByUserIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventUsersByControlEventLogControlEventIdAndByUserIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    control_event_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventsControlledComponent(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'controllable_component_id', 'created_at', 'updated_at', 'control_event', 'controllable_component')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')


class ControlEventsControlledComponentsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ControlEventsControlledComponent)), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventsControlledComponentsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControlEventsControlledComponentsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(ControlEventsControlledComponent, graphql_name='node')


class ControlEventsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')


class ControllableComponentControlEventsManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentControlEventsManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControllableComponentControlEventsManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    control_events_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsControlledComponentsConnection), graphql_name='controlEventsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )


class ControllableComponentsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ControllableComponentsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')


class CreateControlEventMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_metric', 'query', 'control_event', 'project_success_metric', 'control_event_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_metric = sgqlc.types.Field(ControlEventMetric, graphql_name='controlEventMetric')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    control_event_metric_edge = sgqlc.types.Field(ControlEventMetricsEdge, graphql_name='controlEventMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )


class CreateControlEventPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'facility', 'project', 'control_event_state_by_current_state', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateControlEventsControlledComponentPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_events_controlled_component', 'query', 'control_event', 'controllable_component', 'control_events_controlled_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_events_controlled_component = sgqlc.types.Field(ControlEventsControlledComponent, graphql_name='controlEventsControlledComponent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    control_events_controlled_component_edge = sgqlc.types.Field(ControlEventsControlledComponentsEdge, graphql_name='controlEventsControlledComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )


class CreateControllableComponentPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateEdgeNodePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'query', 'organization', 'project', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project = sgqlc.types.Field('Project', graphql_name='project')
    edge_node_edge = sgqlc.types.Field('EdgeNodesEdge', graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateFacilityPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    facility_edge = sgqlc.types.Field('FacilitiesEdge', graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateFacilityProjectPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_project', 'query', 'facility', 'project', 'facility_project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_project = sgqlc.types.Field('FacilityProject', graphql_name='facilityProject')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    facility_project_edge = sgqlc.types.Field('FacilityProjectsEdge', graphql_name='facilityProjectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )


class CreateFacilityUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    user = sgqlc.types.Field('User', graphql_name='user')
    facility_user_edge = sgqlc.types.Field('FacilityUsersEdge', graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateOrganizationPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization_edge = sgqlc.types.Field('OrganizationsEdge', graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateProjectPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    project_edge = sgqlc.types.Field('ProjectsEdge', graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateProjectSuccessMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_success_metric_edge = sgqlc.types.Field('ProjectSuccessMetricsEdge', graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateProjectTypePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project_type_edge = sgqlc.types.Field('ProjectTypesEdge', graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class CreateUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')
    query = sgqlc.types.Field('Query', graphql_name='query')
    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteControlEventLogPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_log', 'deleted_control_event_log_node_id', 'query', 'by_user', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'control_event_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_log = sgqlc.types.Field('ControlEventLog', graphql_name='controlEventLog')
    deleted_control_event_log_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventLogNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_log_edge = sgqlc.types.Field(ControlEventLogsEdge, graphql_name='controlEventLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteControlEventMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_metric', 'deleted_control_event_metric_node_id', 'query', 'control_event', 'project_success_metric', 'control_event_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_metric = sgqlc.types.Field(ControlEventMetric, graphql_name='controlEventMetric')
    deleted_control_event_metric_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventMetricNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    control_event_metric_edge = sgqlc.types.Field(ControlEventMetricsEdge, graphql_name='controlEventMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )


class DeleteControlEventPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'deleted_control_event_node_id', 'query', 'facility', 'project', 'control_event_state_by_current_state', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    deleted_control_event_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteControlEventStatePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_state', 'deleted_control_event_state_node_id', 'query', 'control_event_state_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventState')
    deleted_control_event_state_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventStateNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event_state_edge = sgqlc.types.Field(ControlEventStatesEdge, graphql_name='controlEventStateEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteControllableComponentPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'deleted_controllable_component_node_id', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    deleted_controllable_component_node_id = sgqlc.types.Field(ID, graphql_name='deletedControllableComponentNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteEdgeNodePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'deleted_edge_node_node_id', 'query', 'organization', 'project', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    deleted_edge_node_node_id = sgqlc.types.Field(ID, graphql_name='deletedEdgeNodeNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project = sgqlc.types.Field('Project', graphql_name='project')
    edge_node_edge = sgqlc.types.Field('EdgeNodesEdge', graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteFacilityPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'deleted_facility_node_id', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    deleted_facility_node_id = sgqlc.types.Field(ID, graphql_name='deletedFacilityNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    facility_edge = sgqlc.types.Field('FacilitiesEdge', graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteFacilityUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'deleted_facility_user_node_id', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    deleted_facility_user_node_id = sgqlc.types.Field(ID, graphql_name='deletedFacilityUserNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    user = sgqlc.types.Field('User', graphql_name='user')
    facility_user_edge = sgqlc.types.Field('FacilityUsersEdge', graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteOrganizationPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'deleted_organization_node_id', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    deleted_organization_node_id = sgqlc.types.Field(ID, graphql_name='deletedOrganizationNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization_edge = sgqlc.types.Field('OrganizationsEdge', graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteProjectPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'deleted_project_node_id', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    deleted_project_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    project_edge = sgqlc.types.Field('ProjectsEdge', graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteProjectSuccessMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'deleted_project_success_metric_node_id', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    deleted_project_success_metric_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectSuccessMetricNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_success_metric_edge = sgqlc.types.Field('ProjectSuccessMetricsEdge', graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteProjectTypePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'deleted_project_type_node_id', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    deleted_project_type_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectTypeNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project_type_edge = sgqlc.types.Field('ProjectTypesEdge', graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class DeleteUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'deleted_user_node_id', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')
    deleted_user_node_id = sgqlc.types.Field(ID, graphql_name='deletedUserNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    control_event_logs = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'controllable_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')
    controllable_components = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentsConnection), graphql_name='controllableComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNodeUsersByControlEventLogByEdgeNodeIdAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeUsersByControlEventLogByEdgeNodeIdAndByUserIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodeUsersByControlEventLogByEdgeNodeIdAndByUserIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    control_event_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNodesConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EdgeNodesEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')


class FacilitiesConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilitiesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilitiesEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')


class FacilityControlEventStatesByControlEventFacilityIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityControlEventStatesByControlEventFacilityIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityControlEventStatesByControlEventFacilityIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_events_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEventsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'controllable_components_by_controlled_by_edge_node_client_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    controllable_components_by_controlled_by_edge_node_client_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentsConnection), graphql_name='controllableComponentsByControlledByEdgeNodeClientId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )


class FacilityProject(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status', 'facility', 'project')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    enrollment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='enrollmentStatus')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')


class FacilityProjectsByControlEventFacilityIdAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsByControlEventFacilityIdAndProjectIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityProjectsByControlEventFacilityIdAndProjectIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')
    control_events = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')
    facility_projects = sgqlc.types.Field(sgqlc.types.non_null('FacilityProjectsConnection'), graphql_name='facilityProjects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(FacilityProjectCondition, graphql_name='condition', default=None)),
))
    )


class FacilityProjectsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FacilityProject)), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityProjectsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(FacilityProject, graphql_name='node')


class FacilityUsersConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FacilityUser')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityUsersEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityUsersEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('FacilityUser', graphql_name='node')


class FacilityUsersManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityUsersManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FacilityUsersManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_users')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    facility_users = sgqlc.types.Field(sgqlc.types.non_null(FacilityUsersConnection), graphql_name='facilityUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityUserCondition, graphql_name='condition', default=None)),
))
    )


class Mutation(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('create_control_event_metric', 'create_control_event', 'create_control_events_controlled_component', 'create_controllable_component', 'create_edge_node', 'create_facility', 'create_facility_project', 'create_facility_user', 'create_organization', 'create_project_success_metric', 'create_project_type', 'create_project', 'create_user', 'update_control_event_log_by_node_id', 'update_control_event_log', 'update_control_event_metric_by_control_event_id_and_project_success_metric_id', 'update_control_event_state_by_node_id', 'update_control_event_state', 'update_control_event_by_node_id', 'update_control_event', 'update_control_event_by_start_time_and_facility_id_and_project_id_and_type', 'update_controllable_component_by_node_id', 'update_controllable_component', 'update_controllable_component_by_slug_and_facility_id', 'update_edge_node_by_node_id', 'update_edge_node', 'update_facility_by_node_id', 'update_facility', 'update_facility_user_by_node_id', 'update_facility_user', 'update_organization_by_node_id', 'update_organization', 'update_project_success_metric_by_node_id', 'update_project_success_metric', 'update_project_type_by_node_id', 'update_project_type', 'update_project_by_node_id', 'update_project', 'update_user_by_node_id', 'update_user', 'delete_control_event_log_by_node_id', 'delete_control_event_log', 'delete_control_event_metric_by_control_event_id_and_project_success_metric_id', 'delete_control_event_state_by_node_id', 'delete_control_event_state', 'delete_control_event_by_node_id', 'delete_control_event', 'delete_control_event_by_start_time_and_facility_id_and_project_id_and_type', 'delete_controllable_component_by_node_id', 'delete_controllable_component', 'delete_controllable_component_by_slug_and_facility_id', 'delete_edge_node_by_node_id', 'delete_edge_node', 'delete_facility_by_node_id', 'delete_facility', 'delete_facility_user_by_node_id', 'delete_facility_user', 'delete_organization_by_node_id', 'delete_organization', 'delete_project_success_metric_by_node_id', 'delete_project_success_metric', 'delete_project_type_by_node_id', 'delete_project_type', 'delete_project_by_node_id', 'delete_project', 'delete_user_by_node_id', 'delete_user', 'change_event_state', 'propose_control_event', 'set_control_events')
    create_control_event_metric = sgqlc.types.Field(CreateControlEventMetricPayload, graphql_name='createControlEventMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControlEventMetricInput), graphql_name='input', default=None)),
))
    )
    create_control_event = sgqlc.types.Field(CreateControlEventPayload, graphql_name='createControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControlEventInput), graphql_name='input', default=None)),
))
    )
    create_control_events_controlled_component = sgqlc.types.Field(CreateControlEventsControlledComponentPayload, graphql_name='createControlEventsControlledComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControlEventsControlledComponentInput), graphql_name='input', default=None)),
))
    )
    create_controllable_component = sgqlc.types.Field(CreateControllableComponentPayload, graphql_name='createControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControllableComponentInput), graphql_name='input', default=None)),
))
    )
    create_edge_node = sgqlc.types.Field(CreateEdgeNodePayload, graphql_name='createEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    create_facility = sgqlc.types.Field(CreateFacilityPayload, graphql_name='createFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityInput), graphql_name='input', default=None)),
))
    )
    create_facility_project = sgqlc.types.Field(CreateFacilityProjectPayload, graphql_name='createFacilityProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityProjectInput), graphql_name='input', default=None)),
))
    )
    create_facility_user = sgqlc.types.Field(CreateFacilityUserPayload, graphql_name='createFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityUserInput), graphql_name='input', default=None)),
))
    )
    create_organization = sgqlc.types.Field(CreateOrganizationPayload, graphql_name='createOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_project_success_metric = sgqlc.types.Field(CreateProjectSuccessMetricPayload, graphql_name='createProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    create_project_type = sgqlc.types.Field(CreateProjectTypePayload, graphql_name='createProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectTypeInput), graphql_name='input', default=None)),
))
    )
    create_project = sgqlc.types.Field(CreateProjectPayload, graphql_name='createProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectInput), graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(CreateUserPayload, graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    update_control_event_log_by_node_id = sgqlc.types.Field('UpdateControlEventLogPayload', graphql_name='updateControlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_control_event_log = sgqlc.types.Field('UpdateControlEventLogPayload', graphql_name='updateControlEventLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventLogInput), graphql_name='input', default=None)),
))
    )
    update_control_event_metric_by_control_event_id_and_project_success_metric_id = sgqlc.types.Field('UpdateControlEventMetricPayload', graphql_name='updateControlEventMetricByControlEventIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventMetricByControlEventIdAndProjectSuccessMetricIdInput), graphql_name='input', default=None)),
))
    )
    update_control_event_state_by_node_id = sgqlc.types.Field('UpdateControlEventStatePayload', graphql_name='updateControlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventStateByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_control_event_state = sgqlc.types.Field('UpdateControlEventStatePayload', graphql_name='updateControlEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventStateInput), graphql_name='input', default=None)),
))
    )
    update_control_event_by_node_id = sgqlc.types.Field('UpdateControlEventPayload', graphql_name='updateControlEventByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_control_event = sgqlc.types.Field('UpdateControlEventPayload', graphql_name='updateControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventInput), graphql_name='input', default=None)),
))
    )
    update_control_event_by_start_time_and_facility_id_and_project_id_and_type = sgqlc.types.Field('UpdateControlEventPayload', graphql_name='updateControlEventByStartTimeAndFacilityIdAndProjectIdAndType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventByStartTimeAndFacilityIdAndProjectIdAndTypeInput), graphql_name='input', default=None)),
))
    )
    update_controllable_component_by_node_id = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_controllable_component = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentInput), graphql_name='input', default=None)),
))
    )
    update_controllable_component_by_slug_and_facility_id = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentBySlugAndFacilityIdInput), graphql_name='input', default=None)),
))
    )
    update_edge_node_by_node_id = sgqlc.types.Field('UpdateEdgeNodePayload', graphql_name='updateEdgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEdgeNodeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_edge_node = sgqlc.types.Field('UpdateEdgeNodePayload', graphql_name='updateEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    update_facility_by_node_id = sgqlc.types.Field('UpdateFacilityPayload', graphql_name='updateFacilityByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_facility = sgqlc.types.Field('UpdateFacilityPayload', graphql_name='updateFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityInput), graphql_name='input', default=None)),
))
    )
    update_facility_user_by_node_id = sgqlc.types.Field('UpdateFacilityUserPayload', graphql_name='updateFacilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_facility_user = sgqlc.types.Field('UpdateFacilityUserPayload', graphql_name='updateFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityUserInput), graphql_name='input', default=None)),
))
    )
    update_organization_by_node_id = sgqlc.types.Field('UpdateOrganizationPayload', graphql_name='updateOrganizationByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_organization = sgqlc.types.Field('UpdateOrganizationPayload', graphql_name='updateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationInput), graphql_name='input', default=None)),
))
    )
    update_project_success_metric_by_node_id = sgqlc.types.Field('UpdateProjectSuccessMetricPayload', graphql_name='updateProjectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectSuccessMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_project_success_metric = sgqlc.types.Field('UpdateProjectSuccessMetricPayload', graphql_name='updateProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    update_project_type_by_node_id = sgqlc.types.Field('UpdateProjectTypePayload', graphql_name='updateProjectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectTypeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_project_type = sgqlc.types.Field('UpdateProjectTypePayload', graphql_name='updateProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectTypeInput), graphql_name='input', default=None)),
))
    )
    update_project_by_node_id = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProjectByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_project = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectInput), graphql_name='input', default=None)),
))
    )
    update_user_by_node_id = sgqlc.types.Field('UpdateUserPayload', graphql_name='updateUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_user = sgqlc.types.Field('UpdateUserPayload', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_log_by_node_id = sgqlc.types.Field(DeleteControlEventLogPayload, graphql_name='deleteControlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_log = sgqlc.types.Field(DeleteControlEventLogPayload, graphql_name='deleteControlEventLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventLogInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_metric_by_control_event_id_and_project_success_metric_id = sgqlc.types.Field(DeleteControlEventMetricPayload, graphql_name='deleteControlEventMetricByControlEventIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventMetricByControlEventIdAndProjectSuccessMetricIdInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_state_by_node_id = sgqlc.types.Field(DeleteControlEventStatePayload, graphql_name='deleteControlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventStateByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_state = sgqlc.types.Field(DeleteControlEventStatePayload, graphql_name='deleteControlEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventStateInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_by_node_id = sgqlc.types.Field(DeleteControlEventPayload, graphql_name='deleteControlEventByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_control_event = sgqlc.types.Field(DeleteControlEventPayload, graphql_name='deleteControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventInput), graphql_name='input', default=None)),
))
    )
    delete_control_event_by_start_time_and_facility_id_and_project_id_and_type = sgqlc.types.Field(DeleteControlEventPayload, graphql_name='deleteControlEventByStartTimeAndFacilityIdAndProjectIdAndType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventByStartTimeAndFacilityIdAndProjectIdAndTypeInput), graphql_name='input', default=None)),
))
    )
    delete_controllable_component_by_node_id = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_controllable_component = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentInput), graphql_name='input', default=None)),
))
    )
    delete_controllable_component_by_slug_and_facility_id = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentBySlugAndFacilityIdInput), graphql_name='input', default=None)),
))
    )
    delete_edge_node_by_node_id = sgqlc.types.Field(DeleteEdgeNodePayload, graphql_name='deleteEdgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEdgeNodeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_edge_node = sgqlc.types.Field(DeleteEdgeNodePayload, graphql_name='deleteEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    delete_facility_by_node_id = sgqlc.types.Field(DeleteFacilityPayload, graphql_name='deleteFacilityByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_facility = sgqlc.types.Field(DeleteFacilityPayload, graphql_name='deleteFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityInput), graphql_name='input', default=None)),
))
    )
    delete_facility_user_by_node_id = sgqlc.types.Field(DeleteFacilityUserPayload, graphql_name='deleteFacilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_facility_user = sgqlc.types.Field(DeleteFacilityUserPayload, graphql_name='deleteFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityUserInput), graphql_name='input', default=None)),
))
    )
    delete_organization_by_node_id = sgqlc.types.Field(DeleteOrganizationPayload, graphql_name='deleteOrganizationByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizationByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_organization = sgqlc.types.Field(DeleteOrganizationPayload, graphql_name='deleteOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizationInput), graphql_name='input', default=None)),
))
    )
    delete_project_success_metric_by_node_id = sgqlc.types.Field(DeleteProjectSuccessMetricPayload, graphql_name='deleteProjectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectSuccessMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_project_success_metric = sgqlc.types.Field(DeleteProjectSuccessMetricPayload, graphql_name='deleteProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    delete_project_type_by_node_id = sgqlc.types.Field(DeleteProjectTypePayload, graphql_name='deleteProjectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectTypeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_project_type = sgqlc.types.Field(DeleteProjectTypePayload, graphql_name='deleteProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectTypeInput), graphql_name='input', default=None)),
))
    )
    delete_project_by_node_id = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProjectByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_project = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectInput), graphql_name='input', default=None)),
))
    )
    delete_user_by_node_id = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_user = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserInput), graphql_name='input', default=None)),
))
    )
    change_event_state = sgqlc.types.Field(ChangeEventStatePayload, graphql_name='changeEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeEventStateInput), graphql_name='input', default=None)),
))
    )
    propose_control_event = sgqlc.types.Field('ProposeControlEventPayload', graphql_name='proposeControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProposeControlEventInput), graphql_name='input', default=None)),
))
    )
    set_control_events = sgqlc.types.Field('SetControlEventsPayload', graphql_name='setControlEvents', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetControlEventsInput), graphql_name='input', default=None)),
))
    )


class Node(sgqlc.types.Interface):
    __schema__ = control_schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectType')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ProjectType', graphql_name='node')
    projects = sgqlc.types.Field(sgqlc.types.non_null('ProjectsConnection'), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )


class OrganizationProjectsByEdgeNodeOrganizationIdAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationProjectsByEdgeNodeOrganizationIdAndProjectIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationProjectsByEdgeNodeOrganizationIdAndProjectIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'edge_nodes')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')
    edge_nodes = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodesConnection), graphql_name='edgeNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )


class OrganizationsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')


class PageInfo(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(Cursor, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(Cursor, graphql_name='endCursor')


class ProjectControlEventStatesByControlEventProjectIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectControlEventStatesByControlEventProjectIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectControlEventStatesByControlEventProjectIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_events_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEventsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class ProjectFacilitiesByControlEventProjectIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFacilitiesByControlEventProjectIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectFacilitiesByControlEventProjectIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')
    control_events = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')
    facility_projects = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsConnection), graphql_name='facilityProjects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(FacilityProjectCondition, graphql_name='condition', default=None)),
))
    )


class ProjectOrganizationsByEdgeNodeProjectIdAndOrganizationIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectOrganizationsByEdgeNodeProjectIdAndOrganizationIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectOrganizationsByEdgeNodeProjectIdAndOrganizationIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'edge_nodes')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')
    edge_nodes = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodesConnection), graphql_name='edgeNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )


class ProjectSuccessMetricControlEventsByControlEventMetricProjectSuccessMetricIdAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSuccessMetricControlEventsByControlEventMetricProjectSuccessMetricIdAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectSuccessMetricControlEventsByControlEventMetricProjectSuccessMetricIdAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projected_impact_amount', 'created_at', 'updated_at')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')


class ProjectSuccessMetricsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectSuccessMetric')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSuccessMetricsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectSuccessMetricsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='node')


class ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')
    projects = sgqlc.types.Field(sgqlc.types.non_null('ProjectsConnection'), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )


class ProjectTypesConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectType')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectTypesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectTypesEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ProjectType', graphql_name='node')


class Projectenrollmentstatus(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('enrollment_status', 'facility_id', 'facility_name', 'organization_id')
    enrollment_status = sgqlc.types.Field(String, graphql_name='enrollmentStatus')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    facility_name = sgqlc.types.Field(String, graphql_name='facilityName')
    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')


class ProjectenrollmentstatusesConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Projectenrollmentstatus)), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectenrollmentstatusesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectenrollmentstatusesEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(Projectenrollmentstatus, graphql_name='node')


class ProjectsConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectsEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')


class ProposeControlEventPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'facility', 'project', 'control_event_state_by_current_state', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class SetControlEventsPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'boolean', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    boolean = sgqlc.types.Field(Boolean, graphql_name='boolean')
    query = sgqlc.types.Field('Query', graphql_name='query')


class UpdateControlEventLogPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_log', 'query', 'by_user', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'control_event_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_log = sgqlc.types.Field('ControlEventLog', graphql_name='controlEventLog')
    query = sgqlc.types.Field('Query', graphql_name='query')
    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_log_edge = sgqlc.types.Field(ControlEventLogsEdge, graphql_name='controlEventLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateControlEventMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_metric', 'query', 'control_event', 'project_success_metric', 'control_event_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_metric = sgqlc.types.Field(ControlEventMetric, graphql_name='controlEventMetric')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    control_event_metric_edge = sgqlc.types.Field(ControlEventMetricsEdge, graphql_name='controlEventMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )


class UpdateControlEventPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'facility', 'project', 'control_event_state_by_current_state', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateControlEventStatePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_state', 'query', 'control_event_state_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    control_event_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventState')
    query = sgqlc.types.Field('Query', graphql_name='query')
    control_event_state_edge = sgqlc.types.Field(ControlEventStatesEdge, graphql_name='controlEventStateEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateControllableComponentPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateEdgeNodePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'query', 'organization', 'project', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project = sgqlc.types.Field('Project', graphql_name='project')
    edge_node_edge = sgqlc.types.Field(EdgeNodesEdge, graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateFacilityPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    facility_edge = sgqlc.types.Field(FacilitiesEdge, graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateFacilityUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    query = sgqlc.types.Field('Query', graphql_name='query')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    user = sgqlc.types.Field('User', graphql_name='user')
    facility_user_edge = sgqlc.types.Field(FacilityUsersEdge, graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateOrganizationPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization_edge = sgqlc.types.Field(OrganizationsEdge, graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateProjectPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    query = sgqlc.types.Field('Query', graphql_name='query')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    project_edge = sgqlc.types.Field(ProjectsEdge, graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateProjectSuccessMetricPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_success_metric_edge = sgqlc.types.Field(ProjectSuccessMetricsEdge, graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateProjectTypePayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    query = sgqlc.types.Field('Query', graphql_name='query')
    project_type_edge = sgqlc.types.Field(ProjectTypesEdge, graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UpdateUserPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')
    query = sgqlc.types.Field('Query', graphql_name='query')
    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )


class UserControlEventStatesByControlEventLogByUserIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserControlEventStatesByControlEventLogByUserIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserControlEventStatesByControlEventLogByUserIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class UserControlEventStatesByControlEventLogByUserIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserControlEventStatesByControlEventLogByUserIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserControlEventStatesByControlEventLogByUserIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    control_event_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class UserControlEventsByControlEventLogByUserIdAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserControlEventsByControlEventLogByUserIdAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserControlEventsByControlEventLogByUserIdAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    control_event_logs = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class UserEdgeNodesByControlEventLogByUserIdAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserEdgeNodesByControlEventLogByUserIdAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserEdgeNodesByControlEventLogByUserIdAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    control_event_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )


class UserFacilitiesManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserFacilitiesManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserFacilitiesManyToManyEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_users')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Facility', graphql_name='node')
    facility_users = sgqlc.types.Field(sgqlc.types.non_null(FacilityUsersConnection), graphql_name='facilityUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityUserCondition, graphql_name='condition', default=None)),
))
    )


class UsersConnection(sgqlc.types.relay.Connection):
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsersEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UsersEdge(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')


class ControlEvent(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'facility_id', 'created_at', 'updated_at', 'project_id', 'type', 'current_state', 'facility', 'project', 'control_event_state_by_current_state', 'control_events_controlled_components', 'control_event_metrics', 'control_event_logs', 'controlled_components', 'project_success_metrics_by_control_event_metric_control_event_id_and_project_success_metric_id', 'users_by_control_event_log_control_event_id_and_by_user_id', 'edge_nodes_by_control_event_log_control_event_id_and_by_edge_node_id', 'control_event_states_by_control_event_log_control_event_id_and_previous_state', 'control_event_states_by_control_event_log_control_event_id_and_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    project = sgqlc.types.Field('Project', graphql_name='project')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    control_events_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsControlledComponentsConnection), graphql_name='controlEventsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    control_event_metrics = sgqlc.types.Field(sgqlc.types.non_null(ControlEventMetricsConnection), graphql_name='controlEventMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventMetricCondition, graphql_name='condition', default=None)),
))
    )
    control_event_logs = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    controlled_components = sgqlc.types.Field(sgqlc.types.non_null(ControlEventControlledComponentsManyToManyConnection), graphql_name='controlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    project_success_metrics_by_control_event_metric_control_event_id_and_project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventProjectSuccessMetricsByControlEventMetricControlEventIdAndProjectSuccessMetricIdManyToManyConnection), graphql_name='projectSuccessMetricsByControlEventMetricControlEventIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectSuccessMetricCondition, graphql_name='condition', default=None)),
))
    )
    users_by_control_event_log_control_event_id_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventUsersByControlEventLogControlEventIdAndByUserIdManyToManyConnection), graphql_name='usersByControlEventLogControlEventIdAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes_by_control_event_log_control_event_id_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByControlEventLogControlEventIdAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_control_event_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogControlEventIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_control_event_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogControlEventIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )


class ControlEventLog(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'control_event_id', 'previous_state', 'current_state', 'label', 'event_type', 'data', 'by_user', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    event_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='eventTime')
    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')
    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')
    previous_state = sgqlc.types.Field(String, graphql_name='previousState')
    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    event_type = sgqlc.types.Field(String, graphql_name='eventType')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    control_event = sgqlc.types.Field(ControlEvent, graphql_name='controlEvent')
    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')


class ControlEventState(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at', 'control_events_by_current_state', 'control_event_logs_by_previous_state', 'control_event_logs_by_current_state', 'facilities_by_control_event_current_state_and_facility_id', 'projects_by_control_event_current_state_and_project_id', 'users_by_control_event_log_previous_state_and_by_user_id', 'edge_nodes_by_control_event_log_previous_state_and_by_edge_node_id', 'control_events_by_control_event_log_previous_state_and_control_event_id', 'control_event_states_by_control_event_log_previous_state_and_current_state', 'users_by_control_event_log_current_state_and_by_user_id', 'edge_nodes_by_control_event_log_current_state_and_by_edge_node_id', 'control_events_by_control_event_log_current_state_and_control_event_id', 'control_event_states_by_control_event_log_current_state_and_previous_state')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    rules = sgqlc.types.Field(JSON, graphql_name='rules')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    control_events_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEventsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_event_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    control_event_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    facilities_by_control_event_current_state_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateFacilitiesByControlEventCurrentStateAndFacilityIdManyToManyConnection), graphql_name='facilitiesByControlEventCurrentStateAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    projects_by_control_event_current_state_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateProjectsByControlEventCurrentStateAndProjectIdManyToManyConnection), graphql_name='projectsByControlEventCurrentStateAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    users_by_control_event_log_previous_state_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateUsersByControlEventLogPreviousStateAndByUserIdManyToManyConnection), graphql_name='usersByControlEventLogPreviousStateAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes_by_control_event_log_previous_state_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByControlEventLogPreviousStateAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    control_events_by_control_event_log_previous_state_and_control_event_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyConnection), graphql_name='controlEventsByControlEventLogPreviousStateAndControlEventId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_previous_state_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogPreviousStateAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    users_by_control_event_log_current_state_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateUsersByControlEventLogCurrentStateAndByUserIdManyToManyConnection), graphql_name='usersByControlEventLogCurrentStateAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes_by_control_event_log_current_state_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByControlEventLogCurrentStateAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    control_events_by_control_event_log_current_state_and_control_event_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyConnection), graphql_name='controlEventsByControlEventLogCurrentStateAndControlEventId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_current_state_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogCurrentStateAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )


class ControllableComponent(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at', 'facility', 'controlled_by_edge_node_client', 'control_events_controlled_components', 'control_events')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')
    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    control_events_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsControlledComponentsConnection), graphql_name='controlEventsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    control_events = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentControlEventsManyToManyConnection), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class EdgeNode(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'project_id', 'created_at', 'updated_at', 'organization', 'project', 'controllable_components_by_controlled_by_edge_node_client_id', 'control_event_logs_by_by_edge_node_id', 'facilities_by_controllable_component_controlled_by_edge_node_client_id_and_facility_id', 'users_by_control_event_log_by_edge_node_id_and_by_user_id', 'control_events_by_control_event_log_by_edge_node_id_and_control_event_id', 'control_event_states_by_control_event_log_by_edge_node_id_and_previous_state', 'control_event_states_by_control_event_log_by_edge_node_id_and_current_state')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    project = sgqlc.types.Field('Project', graphql_name='project')
    controllable_components_by_controlled_by_edge_node_client_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentsConnection), graphql_name='controllableComponentsByControlledByEdgeNodeClientId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    control_event_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    facilities_by_controllable_component_controlled_by_edge_node_client_id_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyConnection), graphql_name='facilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    users_by_control_event_log_by_edge_node_id_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeUsersByControlEventLogByEdgeNodeIdAndByUserIdManyToManyConnection), graphql_name='usersByControlEventLogByEdgeNodeIdAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    control_events_by_control_event_log_by_edge_node_id_and_control_event_id = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyConnection), graphql_name='controlEventsByControlEventLogByEdgeNodeIdAndControlEventId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_by_edge_node_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogByEdgeNodeIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_by_edge_node_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogByEdgeNodeIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )


class Facility(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at', 'organization', 'control_events', 'controllable_components', 'facility_projects', 'facility_users', 'projects_by_control_event_facility_id_and_project_id', 'control_event_states_by_control_event_facility_id_and_current_state', 'edge_nodes_by_controllable_component_facility_id_and_controlled_by_edge_node_client_id', 'projects_by_facility_project_facility_id_and_project_id', 'users')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    control_events = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    controllable_components = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentsConnection), graphql_name='controllableComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    facility_projects = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsConnection), graphql_name='facilityProjects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(FacilityProjectCondition, graphql_name='condition', default=None)),
))
    )
    facility_users = sgqlc.types.Field(sgqlc.types.non_null(FacilityUsersConnection), graphql_name='facilityUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityUserCondition, graphql_name='condition', default=None)),
))
    )
    projects_by_control_event_facility_id_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsByControlEventFacilityIdAndProjectIdManyToManyConnection), graphql_name='projectsByControlEventFacilityIdAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_facility_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(FacilityControlEventStatesByControlEventFacilityIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventFacilityIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes_by_controllable_component_facility_id_and_controlled_by_edge_node_client_id = sgqlc.types.Field(sgqlc.types.non_null(FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyConnection), graphql_name='edgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    projects_by_facility_project_facility_id_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyConnection), graphql_name='projectsByFacilityProjectFacilityIdAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(FacilityUsersManyToManyConnection), graphql_name='users', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )


class FacilityUser(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at', 'facility', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    facility = sgqlc.types.Field(Facility, graphql_name='facility')
    user = sgqlc.types.Field('User', graphql_name='user')


class Organization(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at', 'edge_nodes', 'projects', 'facilities', 'projects_by_edge_node_organization_id_and_project_id', 'project_types_by_project_organization_id_and_project_type_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    edge_nodes = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodesConnection), graphql_name='edgeNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectsConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    facilities = sgqlc.types.Field(sgqlc.types.non_null(FacilitiesConnection), graphql_name='facilities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    projects_by_edge_node_organization_id_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(OrganizationProjectsByEdgeNodeOrganizationIdAndProjectIdManyToManyConnection), graphql_name='projectsByEdgeNodeOrganizationIdAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    project_types_by_project_organization_id_and_project_type_id = sgqlc.types.Field(sgqlc.types.non_null(OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyConnection), graphql_name='projectTypesByProjectOrganizationIdAndProjectTypeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectTypeCondition, graphql_name='condition', default=None)),
))
    )


class Project(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at', 'organization', 'project_type', 'control_events', 'edge_nodes', 'facility_projects', 'project_success_metrics', 'facilities_by_control_event_project_id_and_facility_id', 'control_event_states_by_control_event_project_id_and_current_state', 'organizations_by_edge_node_project_id_and_organization_id', 'facilities_by_facility_project_project_id_and_facility_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')
    project_type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectTypeId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    control_events = sgqlc.types.Field(sgqlc.types.non_null(ControlEventsConnection), graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodesConnection), graphql_name='edgeNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    facility_projects = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsConnection), graphql_name='facilityProjects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(FacilityProjectCondition, graphql_name='condition', default=None)),
))
    )
    project_success_metrics = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricsConnection), graphql_name='projectSuccessMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectSuccessMetricCondition, graphql_name='condition', default=None)),
))
    )
    facilities_by_control_event_project_id_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectFacilitiesByControlEventProjectIdAndFacilityIdManyToManyConnection), graphql_name='facilitiesByControlEventProjectIdAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_project_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ProjectControlEventStatesByControlEventProjectIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventProjectIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    organizations_by_edge_node_project_id_and_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectOrganizationsByEdgeNodeProjectIdAndOrganizationIdManyToManyConnection), graphql_name='organizationsByEdgeNodeProjectIdAndOrganizationId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(OrganizationCondition, graphql_name='condition', default=None)),
))
    )
    facilities_by_facility_project_project_id_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyConnection), graphql_name='facilitiesByFacilityProjectProjectIdAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )


class ProjectSuccessMetric(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at', 'project', 'control_event_metrics', 'control_events_by_control_event_metric_project_success_metric_id_and_control_event_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    units = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='units')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    project = sgqlc.types.Field(Project, graphql_name='project')
    control_event_metrics = sgqlc.types.Field(sgqlc.types.non_null(ControlEventMetricsConnection), graphql_name='controlEventMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventMetricCondition, graphql_name='condition', default=None)),
))
    )
    control_events_by_control_event_metric_project_success_metric_id_and_control_event_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricControlEventsByControlEventMetricProjectSuccessMetricIdAndControlEventIdManyToManyConnection), graphql_name='controlEventsByControlEventMetricProjectSuccessMetricIdAndControlEventId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )


class ProjectType(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at', 'projects', 'organizations_by_project_project_type_id_and_organization_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectsConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    organizations_by_project_project_type_id_and_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyConnection), graphql_name='organizationsByProjectProjectTypeIdAndOrganizationId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(OrganizationCondition, graphql_name='condition', default=None)),
))
    )


class Query(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('query', 'node', 'control_event_logs', 'control_event_metrics', 'control_event_states', 'control_events', 'control_events_controlled_components', 'controllable_components', 'edge_nodes', 'facilities', 'facility_projects', 'facility_users', 'organizations', 'project_success_metrics', 'project_types', 'projects', 'users', 'control_event_log', 'control_event_metric_by_control_event_id_and_project_success_metric_id', 'control_event_state', 'control_event', 'control_event_by_start_time_and_facility_id_and_project_id_and_type', 'controllable_component', 'controllable_component_by_slug_and_facility_id', 'edge_node', 'facility', 'facility_user', 'organization', 'project_success_metric', 'project_type', 'project', 'user', 'control_events_by_edge_node_client_id', 'facility_enrollment_status_for_project', 'control_event_log_by_node_id', 'control_event_state_by_node_id', 'control_event_by_node_id', 'controllable_component_by_node_id', 'edge_node_by_node_id', 'facility_by_node_id', 'facility_user_by_node_id', 'organization_by_node_id', 'project_success_metric_by_node_id', 'project_type_by_node_id', 'project_by_node_id', 'user_by_node_id')
    query = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='query')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    control_event_logs = sgqlc.types.Field(ControlEventLogsConnection, graphql_name='controlEventLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    control_event_metrics = sgqlc.types.Field(ControlEventMetricsConnection, graphql_name='controlEventMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventMetricsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventMetricCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states = sgqlc.types.Field(ControlEventStatesConnection, graphql_name='controlEventStates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    control_events = sgqlc.types.Field(ControlEventsConnection, graphql_name='controlEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_events_controlled_components = sgqlc.types.Field(ControlEventsControlledComponentsConnection, graphql_name='controlEventsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(ControlEventsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    controllable_components = sgqlc.types.Field(ControllableComponentsConnection, graphql_name='controllableComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes = sgqlc.types.Field(EdgeNodesConnection, graphql_name='edgeNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    facilities = sgqlc.types.Field(FacilitiesConnection, graphql_name='facilities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    facility_projects = sgqlc.types.Field(FacilityProjectsConnection, graphql_name='facilityProjects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(FacilityProjectCondition, graphql_name='condition', default=None)),
))
    )
    facility_users = sgqlc.types.Field(FacilityUsersConnection, graphql_name='facilityUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityUserCondition, graphql_name='condition', default=None)),
))
    )
    organizations = sgqlc.types.Field(OrganizationsConnection, graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(OrganizationCondition, graphql_name='condition', default=None)),
))
    )
    project_success_metrics = sgqlc.types.Field(ProjectSuccessMetricsConnection, graphql_name='projectSuccessMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectSuccessMetricCondition, graphql_name='condition', default=None)),
))
    )
    project_types = sgqlc.types.Field(ProjectTypesConnection, graphql_name='projectTypes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectTypeCondition, graphql_name='condition', default=None)),
))
    )
    projects = sgqlc.types.Field(ProjectsConnection, graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    users = sgqlc.types.Field(UsersConnection, graphql_name='users', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    control_event_log = sgqlc.types.Field(ControlEventLog, graphql_name='controlEventLog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    control_event_metric_by_control_event_id_and_project_success_metric_id = sgqlc.types.Field(ControlEventMetric, graphql_name='controlEventMetricByControlEventIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('control_event_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='controlEventId', default=None)),
        ('project_success_metric_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId', default=None)),
))
    )
    control_event_state = sgqlc.types.Field(ControlEventState, graphql_name='controlEventState', args=sgqlc.types.ArgDict((
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='state', default=None)),
))
    )
    control_event = sgqlc.types.Field(ControlEvent, graphql_name='controlEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    control_event_by_start_time_and_facility_id_and_project_id_and_type = sgqlc.types.Field(ControlEvent, graphql_name='controlEventByStartTimeAndFacilityIdAndProjectIdAndType', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(Datetime), graphql_name='startTime', default=None)),
        ('facility_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='facilityId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectId', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='type', default=None)),
))
    )
    controllable_component = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    controllable_component_by_slug_and_facility_id = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('facility_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='facilityId', default=None)),
))
    )
    edge_node = sgqlc.types.Field(EdgeNode, graphql_name='edgeNode', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    facility = sgqlc.types.Field(Facility, graphql_name='facility', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    facility_user = sgqlc.types.Field(FacilityUser, graphql_name='facilityUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    project_success_metric = sgqlc.types.Field(ProjectSuccessMetric, graphql_name='projectSuccessMetric', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    project_type = sgqlc.types.Field(ProjectType, graphql_name='projectType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project = sgqlc.types.Field(Project, graphql_name='project', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    control_events_by_edge_node_client_id = sgqlc.types.Field(ControlEventsConnection, graphql_name='controlEventsByEdgeNodeClientId', args=sgqlc.types.ArgDict((
        ('clientid', sgqlc.types.Arg(String, graphql_name='clientid', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    facility_enrollment_status_for_project = sgqlc.types.Field(ProjectenrollmentstatusesConnection, graphql_name='facilityEnrollmentStatusForProject', args=sgqlc.types.ArgDict((
        ('projectid', sgqlc.types.Arg(String, graphql_name='projectid', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    control_event_log_by_node_id = sgqlc.types.Field(ControlEventLog, graphql_name='controlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    control_event_state_by_node_id = sgqlc.types.Field(ControlEventState, graphql_name='controlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    control_event_by_node_id = sgqlc.types.Field(ControlEvent, graphql_name='controlEventByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    controllable_component_by_node_id = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    edge_node_by_node_id = sgqlc.types.Field(EdgeNode, graphql_name='edgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    facility_by_node_id = sgqlc.types.Field(Facility, graphql_name='facilityByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    facility_user_by_node_id = sgqlc.types.Field(FacilityUser, graphql_name='facilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    organization_by_node_id = sgqlc.types.Field(Organization, graphql_name='organizationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    project_success_metric_by_node_id = sgqlc.types.Field(ProjectSuccessMetric, graphql_name='projectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    project_type_by_node_id = sgqlc.types.Field(ProjectType, graphql_name='projectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    project_by_node_id = sgqlc.types.Field(Project, graphql_name='projectByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    user_by_node_id = sgqlc.types.Field('User', graphql_name='userByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )


class User(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at', 'control_event_logs_by_by_user_id', 'facility_users', 'edge_nodes_by_control_event_log_by_user_id_and_by_edge_node_id', 'control_events_by_control_event_log_by_user_id_and_control_event_id', 'control_event_states_by_control_event_log_by_user_id_and_previous_state', 'control_event_states_by_control_event_log_by_user_id_and_current_state', 'facilities')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    phone_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phoneNumber')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')
    control_event_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogsConnection), graphql_name='controlEventLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventLogCondition, graphql_name='condition', default=None)),
))
    )
    facility_users = sgqlc.types.Field(sgqlc.types.non_null(FacilityUsersConnection), graphql_name='facilityUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityUserCondition, graphql_name='condition', default=None)),
))
    )
    edge_nodes_by_control_event_log_by_user_id_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(UserEdgeNodesByControlEventLogByUserIdAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByControlEventLogByUserIdAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    control_events_by_control_event_log_by_user_id_and_control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UserControlEventsByControlEventLogByUserIdAndControlEventIdManyToManyConnection), graphql_name='controlEventsByControlEventLogByUserIdAndControlEventId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_by_user_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(UserControlEventStatesByControlEventLogByUserIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogByUserIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    control_event_states_by_control_event_log_by_user_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(UserControlEventStatesByControlEventLogByUserIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventLogByUserIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    facilities = sgqlc.types.Field(sgqlc.types.non_null(UserFacilitiesManyToManyConnection), graphql_name='facilities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
control_schema.query_type = Query
control_schema.mutation_type = Mutation
control_schema.subscription_type = None

