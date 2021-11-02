import sgqlc.types
import sgqlc.types.relay


control_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
control_schema -= sgqlc.types.relay.Node
control_schema -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class ControlEventLogsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ControlEventLog`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `EVENT_TIME_ASC`None
    * `EVENT_TIME_DESC`None
    * `BY_USER_ID_ASC`None
    * `BY_USER_ID_DESC`None
    * `BY_EDGE_NODE_ID_ASC`None
    * `BY_EDGE_NODE_ID_DESC`None
    * `CONTROL_EVENT_ID_ASC`None
    * `CONTROL_EVENT_ID_DESC`None
    * `PREVIOUS_STATE_ASC`None
    * `PREVIOUS_STATE_DESC`None
    * `CURRENT_STATE_ASC`None
    * `CURRENT_STATE_DESC`None
    * `LABEL_ASC`None
    * `LABEL_DESC`None
    * `EVENT_TYPE_ASC`None
    * `EVENT_TYPE_DESC`None
    * `DATA_ASC`None
    * `DATA_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('BY_EDGE_NODE_ID_ASC', 'BY_EDGE_NODE_ID_DESC', 'BY_USER_ID_ASC', 'BY_USER_ID_DESC', 'CONTROL_EVENT_ID_ASC', 'CONTROL_EVENT_ID_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'DATA_ASC', 'DATA_DESC', 'EVENT_TIME_ASC', 'EVENT_TIME_DESC', 'EVENT_TYPE_ASC', 'EVENT_TYPE_DESC', 'ID_ASC', 'ID_DESC', 'LABEL_ASC', 'LABEL_DESC', 'NATURAL', 'PREVIOUS_STATE_ASC', 'PREVIOUS_STATE_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ControlEventStatesOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ControlEventState`.

    Enumeration Choices:

    * `NATURAL`None
    * `STATE_ASC`None
    * `STATE_DESC`None
    * `RULES_ASC`None
    * `RULES_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'RULES_ASC', 'RULES_DESC', 'STATE_ASC', 'STATE_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ControlEventsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ControlEvent`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `START_TIME_ASC`None
    * `START_TIME_DESC`None
    * `END_TIME_ASC`None
    * `END_TIME_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `CURRENT_STATE_ASC`None
    * `CURRENT_STATE_DESC`None
    * `EVENT_PROPOSAL_ID_ASC`None
    * `EVENT_PROPOSAL_ID_DESC`None
    * `CONTROLLABLE_COMPONENT_ID_ASC`None
    * `CONTROLLABLE_COMPONENT_ID_DESC`None
    * `STATE_MACHINE_ID_ASC`None
    * `STATE_MACHINE_ID_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CONTROLLABLE_COMPONENT_ID_ASC', 'CONTROLLABLE_COMPONENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'END_TIME_ASC', 'END_TIME_DESC', 'EVENT_PROPOSAL_ID_ASC', 'EVENT_PROPOSAL_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'START_TIME_ASC', 'START_TIME_DESC', 'STATE_MACHINE_ID_ASC', 'STATE_MACHINE_ID_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ControllableComponentsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ControllableComponent`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `SLUG_ASC`None
    * `SLUG_DESC`None
    * `FACILITY_ID_ASC`None
    * `FACILITY_ID_DESC`None
    * `LABEL_ASC`None
    * `LABEL_DESC`None
    * `DESCRIPTION_ASC`None
    * `DESCRIPTION_DESC`None
    * `CONTROLLED_BY_EDGE_NODE_CLIENT_ID_ASC`None
    * `CONTROLLED_BY_EDGE_NODE_CLIENT_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `IS_SCHEDULABLE_ASC`None
    * `IS_SCHEDULABLE_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CONTROLLED_BY_EDGE_NODE_CLIENT_ID_ASC', 'CONTROLLED_BY_EDGE_NODE_CLIENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'ID_ASC', 'ID_DESC', 'IS_SCHEDULABLE_ASC', 'IS_SCHEDULABLE_DESC', 'LABEL_ASC', 'LABEL_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SLUG_ASC', 'SLUG_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class Cursor(sgqlc.types.Scalar):
    '''A location in a connection that can be used for resuming
    pagination.
    '''
    __schema__ = control_schema


class Datetime(sgqlc.types.Scalar):
    '''A point in time as described by the [ISO
    8601](https://en.wikipedia.org/wiki/ISO_8601) standard. May or may
    not include a timezone.
    '''
    __schema__ = control_schema


class EdgeNodesOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `EdgeNode`.

    Enumeration Choices:

    * `NATURAL`None
    * `CLIENT_ID_ASC`None
    * `CLIENT_ID_DESC`None
    * `ORGANIZATION_ID_ASC`None
    * `ORGANIZATION_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `FACILITY_ID_ASC`None
    * `FACILITY_ID_DESC`None
    * `LAST_FETCH_TIME_ASC`None
    * `LAST_FETCH_TIME_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CLIENT_ID_ASC', 'CLIENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'LAST_FETCH_TIME_ASC', 'LAST_FETCH_TIME_DESC', 'NATURAL', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class EventProposalLogsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `EventProposalLog`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `EVENT_TIME_ASC`None
    * `EVENT_TIME_DESC`None
    * `BY_USER_ID_ASC`None
    * `BY_USER_ID_DESC`None
    * `BY_EDGE_NODE_ID_ASC`None
    * `BY_EDGE_NODE_ID_DESC`None
    * `PREVIOUS_STATE_ASC`None
    * `PREVIOUS_STATE_DESC`None
    * `CURRENT_STATE_ASC`None
    * `CURRENT_STATE_DESC`None
    * `LABEL_ASC`None
    * `LABEL_DESC`None
    * `EVENT_TYPE_ASC`None
    * `EVENT_TYPE_DESC`None
    * `DATA_ASC`None
    * `DATA_DESC`None
    * `EVENT_PROPOSAL_ID_ASC`None
    * `EVENT_PROPOSAL_ID_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('BY_EDGE_NODE_ID_ASC', 'BY_EDGE_NODE_ID_DESC', 'BY_USER_ID_ASC', 'BY_USER_ID_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'DATA_ASC', 'DATA_DESC', 'EVENT_PROPOSAL_ID_ASC', 'EVENT_PROPOSAL_ID_DESC', 'EVENT_TIME_ASC', 'EVENT_TIME_DESC', 'EVENT_TYPE_ASC', 'EVENT_TYPE_DESC', 'ID_ASC', 'ID_DESC', 'LABEL_ASC', 'LABEL_DESC', 'NATURAL', 'PREVIOUS_STATE_ASC', 'PREVIOUS_STATE_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class EventProposalMetricsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `EventProposalMetric`.

    Enumeration Choices:

    * `NATURAL`None
    * `PROJECT_SUCCESS_METRIC_ID_ASC`None
    * `PROJECT_SUCCESS_METRIC_ID_DESC`None
    * `PROJECTED_IMPACT_AMOUNT_ASC`None
    * `PROJECTED_IMPACT_AMOUNT_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `ACTUAL_IMPACT_AMOUNT_ASC`None
    * `ACTUAL_IMPACT_AMOUNT_DESC`None
    * `CONTROLLABLE_COMPONENT_ID_ASC`None
    * `CONTROLLABLE_COMPONENT_ID_DESC`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `EVENT_PROPOSAL_ID_ASC`None
    * `EVENT_PROPOSAL_ID_DESC`None
    * `CALCULATION_METADATA_ASC`None
    * `CALCULATION_METADATA_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('ACTUAL_IMPACT_AMOUNT_ASC', 'ACTUAL_IMPACT_AMOUNT_DESC', 'CALCULATION_METADATA_ASC', 'CALCULATION_METADATA_DESC', 'CONTROLLABLE_COMPONENT_ID_ASC', 'CONTROLLABLE_COMPONENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'EVENT_PROPOSAL_ID_ASC', 'EVENT_PROPOSAL_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECTED_IMPACT_AMOUNT_ASC', 'PROJECTED_IMPACT_AMOUNT_DESC', 'PROJECT_SUCCESS_METRIC_ID_ASC', 'PROJECT_SUCCESS_METRIC_ID_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class EventProposalsControlledComponentsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `EventProposalsControlledComponent`.

    Enumeration Choices:

    * `NATURAL`None
    * `EVENT_PROPOSAL_ID_ASC`None
    * `EVENT_PROPOSAL_ID_DESC`None
    * `CONTROLLABLE_COMPONENT_ID_ASC`None
    * `CONTROLLABLE_COMPONENT_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `STATE_DEFINITION_ASC`None
    * `STATE_DEFINITION_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CONTROLLABLE_COMPONENT_ID_ASC', 'CONTROLLABLE_COMPONENT_ID_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'EVENT_PROPOSAL_ID_ASC', 'EVENT_PROPOSAL_ID_DESC', 'NATURAL', 'STATE_DEFINITION_ASC', 'STATE_DEFINITION_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class EventProposalsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `EventProposal`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `PROJECT_ID_ASC`None
    * `PROJECT_ID_DESC`None
    * `FACILITY_ID_ASC`None
    * `FACILITY_ID_DESC`None
    * `START_TIME_ASC`None
    * `START_TIME_DESC`None
    * `END_TIME_ASC`None
    * `END_TIME_DESC`None
    * `TYPE_ASC`None
    * `TYPE_DESC`None
    * `CURRENT_STATE_ASC`None
    * `CURRENT_STATE_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'END_TIME_ASC', 'END_TIME_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'START_TIME_ASC', 'START_TIME_DESC', 'TYPE_ASC', 'TYPE_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class FacilitiesOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `Facility`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `NAME_ASC`None
    * `NAME_DESC`None
    * `ORGANIZATION_ID_ASC`None
    * `ORGANIZATION_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class FacilityProjectsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `FacilityProject`.

    Enumeration Choices:

    * `NATURAL`None
    * `FACILITY_ID_ASC`None
    * `FACILITY_ID_DESC`None
    * `PROJECT_ID_ASC`None
    * `PROJECT_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `ENROLLMENT_STATUS_ASC`None
    * `ENROLLMENT_STATUS_DESC`None
    * `AUTO_APPROVE_ASC`None
    * `AUTO_APPROVE_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('AUTO_APPROVE_ASC', 'AUTO_APPROVE_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'ENROLLMENT_STATUS_ASC', 'ENROLLMENT_STATUS_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'NATURAL', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class FacilityUsersOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `FacilityUser`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `FACILITY_ID_ASC`None
    * `FACILITY_ID_DESC`None
    * `USER_ID_ASC`None
    * `USER_ID_DESC`None
    * `ROLE_ASC`None
    * `ROLE_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'FACILITY_ID_ASC', 'FACILITY_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'ROLE_ASC', 'ROLE_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'USER_ID_ASC', 'USER_ID_DESC')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    '''A JavaScript object encoded in the JSON format as specified by
    [ECMA-404](http://www.ecma-
    international.org/publications/files/ECMA-ST/ECMA-404.pdf).
    '''
    __schema__ = control_schema


class OrganizationsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `Organization`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `NAME_ASC`None
    * `NAME_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ProjectAgentsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ProjectAgent`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `PROJECT_ID_ASC`None
    * `PROJECT_ID_DESC`None
    * `USER_ID_ASC`None
    * `USER_ID_DESC`None
    * `ROLE_ASC`None
    * `ROLE_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'ROLE_ASC', 'ROLE_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'USER_ID_ASC', 'USER_ID_DESC')


class ProjectSuccessMetricsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ProjectSuccessMetric`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `PROJECT_ID_ASC`None
    * `PROJECT_ID_DESC`None
    * `NAME_ASC`None
    * `NAME_DESC`None
    * `DESCRIPTION_ASC`None
    * `DESCRIPTION_DESC`None
    * `UNITS_ASC`None
    * `UNITS_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'UNITS_ASC', 'UNITS_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ProjectTypesOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `ProjectType`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `NAME_ASC`None
    * `NAME_DESC`None
    * `DESCRIPTION_ASC`None
    * `DESCRIPTION_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class ProjectsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `Project`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `NAME_ASC`None
    * `NAME_DESC`None
    * `DESCRIPTION_ASC`None
    * `DESCRIPTION_DESC`None
    * `ORGANIZATION_ID_ASC`None
    * `ORGANIZATION_ID_DESC`None
    * `PROJECT_TYPE_ID_ASC`None
    * `PROJECT_TYPE_ID_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `AUTO_REVIEW_ASC`None
    * `AUTO_REVIEW_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('AUTO_REVIEW_ASC', 'AUTO_REVIEW_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'ORGANIZATION_ID_ASC', 'ORGANIZATION_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECT_TYPE_ID_ASC', 'PROJECT_TYPE_ID_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class StateDefinitionsOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `StateDefinition`.

    Enumeration Choices:

    * `NATURAL`None
    * `SLUG_ASC`None
    * `SLUG_DESC`None
    * `PROJECT_ID_ASC`None
    * `PROJECT_ID_DESC`None
    * `LABEL_ASC`None
    * `LABEL_DESC`None
    * `DESCRIPTION_ASC`None
    * `DESCRIPTION_DESC`None
    * `DEFINITION_ASC`None
    * `DEFINITION_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'DEFINITION_ASC', 'DEFINITION_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'LABEL_ASC', 'LABEL_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROJECT_ID_ASC', 'PROJECT_ID_DESC', 'SLUG_ASC', 'SLUG_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


class StateMachinesOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `StateMachine`.

    Enumeration Choices:

    * `NATURAL`None
    * `ID_ASC`None
    * `ID_DESC`None
    * `STATE_DEFINITION_ASC`None
    * `STATE_DEFINITION_DESC`None
    * `CURRENT_STATE_ASC`None
    * `CURRENT_STATE_DESC`None
    * `CONTEXT_ASC`None
    * `CONTEXT_DESC`None
    * `MACHINE_ASC`None
    * `MACHINE_DESC`None
    * `STATE_ASC`None
    * `STATE_DESC`None
    * `IS_ACTIVE_ASC`None
    * `IS_ACTIVE_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CONTEXT_ASC', 'CONTEXT_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'CURRENT_STATE_ASC', 'CURRENT_STATE_DESC', 'ID_ASC', 'ID_DESC', 'IS_ACTIVE_ASC', 'IS_ACTIVE_DESC', 'MACHINE_ASC', 'MACHINE_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'STATE_ASC', 'STATE_DEFINITION_ASC', 'STATE_DEFINITION_DESC', 'STATE_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')


String = sgqlc.types.String

class UUID(sgqlc.types.Scalar):
    '''A universally unique identifier as defined by [RFC
    4122](https://tools.ietf.org/html/rfc4122).
    '''
    __schema__ = control_schema


class UsersOrderBy(sgqlc.types.Enum):
    '''Methods to use when ordering `User`.

    Enumeration Choices:

    * `NATURAL`None
    * `FIRST_NAME_ASC`None
    * `FIRST_NAME_DESC`None
    * `LAST_NAME_ASC`None
    * `LAST_NAME_DESC`None
    * `EMAIL_ASC`None
    * `EMAIL_DESC`None
    * `PHONE_NUMBER_ASC`None
    * `PHONE_NUMBER_DESC`None
    * `CREATED_AT_ASC`None
    * `CREATED_AT_DESC`None
    * `UPDATED_AT_ASC`None
    * `UPDATED_AT_DESC`None
    * `PRIMARY_KEY_ASC`None
    * `PRIMARY_KEY_DESC`None
    '''
    __schema__ = control_schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'EMAIL_ASC', 'EMAIL_DESC', 'FIRST_NAME_ASC', 'FIRST_NAME_DESC', 'LAST_NAME_ASC', 'LAST_NAME_DESC', 'NATURAL', 'PHONE_NUMBER_ASC', 'PHONE_NUMBER_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'UPDATED_AT_ASC', 'UPDATED_AT_DESC')



########################################################################
# Input Objects
########################################################################
class AddHistoricEventInput(sgqlc.types.Input):
    '''All input for the `addHistoricEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'historic_event', 'components')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    historic_event = sgqlc.types.Field(sgqlc.types.non_null('HistoricEventProposalInputRecordInput'), graphql_name='historicEvent')

    components = sgqlc.types.Field(sgqlc.types.list_of('ControllableComponentInput'), graphql_name='components')



class ApproveProposalInput(sgqlc.types.Input):
    '''All input for the `approveProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'approved_proposal', 'approved_components')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    approved_proposal = sgqlc.types.Field(sgqlc.types.non_null('EventApprovalInputRecordInput'), graphql_name='approvedProposal')

    approved_components = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ComponentToControlInputRecordInput')), graphql_name='approvedComponents')



class ApproveProposalReviewInput(sgqlc.types.Input):
    '''All input for the `approveProposalReview` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'approved_proposal')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    approved_proposal = sgqlc.types.Field(sgqlc.types.non_null('EventApprovalInputRecordInput'), graphql_name='approvedProposal')



class ChangeEventStateInput(sgqlc.types.Input):
    '''All input for the `changeEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_id', 'to_state', 'comment', 'changed_by_edge_node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controlEventId')

    to_state = sgqlc.types.Field(sgqlc.types.non_null('ControlEventStateInput'), graphql_name='toState')

    comment = sgqlc.types.Field(String, graphql_name='comment')

    changed_by_edge_node_id = sgqlc.types.Field(String, graphql_name='changedByEdgeNodeId')



class ChangeProposalStateInput(sgqlc.types.Input):
    '''All input for the `changeProposalState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_id', 'to_state', 'comment', 'changed_by_user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    to_state = sgqlc.types.Field(sgqlc.types.non_null('ControlEventStateInput'), graphql_name='toState')

    comment = sgqlc.types.Field(String, graphql_name='comment')

    changed_by_user_id = sgqlc.types.Field(String, graphql_name='changedByUserId')



class ComponentToControlInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting `ComponentToControlInputRecord`'''
    __schema__ = control_schema
    __field_names__ = ('controllable_component_id', 'state_definition_slug')
    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')

    state_definition_slug = sgqlc.types.Field(String, graphql_name='stateDefinitionSlug')



class ControlEventCondition(sgqlc.types.Input):
    '''A condition to be used against `ControlEvent` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'current_state', 'event_proposal_id', 'controllable_component_id', 'state_machine_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    '''Checks for equality with the object’s `startTime` field.'''

    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    '''Checks for equality with the object’s `endTime` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    '''Checks for equality with the object’s `currentState` field.'''

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''Checks for equality with the object’s `eventProposalId` field.'''

    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')
    '''Checks for equality with the object’s `controllableComponentId`
    field.
    '''

    state_machine_id = sgqlc.types.Field(UUID, graphql_name='stateMachineId')
    '''Checks for equality with the object’s `stateMachineId` field.'''



class ControlEventInput(sgqlc.types.Input):
    '''An input for mutations affecting `ControlEvent`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'current_state', 'event_proposal_id', 'controllable_component_id', 'state_machine_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')

    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')

    state_machine_id = sgqlc.types.Field(UUID, graphql_name='stateMachineId')



class ControlEventLogCondition(sgqlc.types.Input):
    '''A condition to be used against `ControlEventLog` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'control_event_id', 'previous_state', 'current_state', 'label', 'event_type', 'data')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    event_time = sgqlc.types.Field(Datetime, graphql_name='eventTime')
    '''Checks for equality with the object’s `eventTime` field.'''

    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')
    '''Checks for equality with the object’s `byUserId` field.'''

    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')
    '''Checks for equality with the object’s `byEdgeNodeId` field.'''

    control_event_id = sgqlc.types.Field(UUID, graphql_name='controlEventId')
    '''Checks for equality with the object’s `controlEventId` field.'''

    previous_state = sgqlc.types.Field(String, graphql_name='previousState')
    '''Checks for equality with the object’s `previousState` field.'''

    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    '''Checks for equality with the object’s `currentState` field.'''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''Checks for equality with the object’s `label` field.'''

    event_type = sgqlc.types.Field(String, graphql_name='eventType')
    '''Checks for equality with the object’s `eventType` field.'''

    data = sgqlc.types.Field(JSON, graphql_name='data')
    '''Checks for equality with the object’s `data` field.'''



class ControlEventLogPatch(sgqlc.types.Input):
    '''Represents an update to a `ControlEventLog`. Fields that are set
    will be updated.
    '''
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



class ControlEventPatch(sgqlc.types.Input):
    '''Represents an update to a `ControlEvent`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'current_state', 'event_proposal_id', 'controllable_component_id', 'state_machine_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')

    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')

    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')

    state_machine_id = sgqlc.types.Field(UUID, graphql_name='stateMachineId')



class ControlEventStateCondition(sgqlc.types.Input):
    '''A condition to be used against `ControlEventState` object types.
    All fields are tested for equality and combined with a logical
    ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(String, graphql_name='state')
    '''Checks for equality with the object’s `state` field.'''

    rules = sgqlc.types.Field(JSON, graphql_name='rules')
    '''Checks for equality with the object’s `rules` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class ControlEventStateInput(sgqlc.types.Input):
    '''An input for mutations affecting `ControlEventState`'''
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')

    rules = sgqlc.types.Field(JSON, graphql_name='rules')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ControlEventStatePatch(sgqlc.types.Input):
    '''Represents an update to a `ControlEventState`. Fields that are set
    will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at')
    state = sgqlc.types.Field(String, graphql_name='state')

    rules = sgqlc.types.Field(JSON, graphql_name='rules')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ControllableComponentCondition(sgqlc.types.Input):
    '''A condition to be used against `ControllableComponent` object
    types. All fields are tested for equality and combined with a
    logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at', 'is_schedulable')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    slug = sgqlc.types.Field(String, graphql_name='slug')
    '''Checks for equality with the object’s `slug` field.'''

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    '''Checks for equality with the object’s `facilityId` field.'''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''Checks for equality with the object’s `label` field.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Checks for equality with the object’s `description` field.'''

    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')
    '''Checks for equality with the object’s
    `controlledByEdgeNodeClientId` field.
    '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    is_schedulable = sgqlc.types.Field(Boolean, graphql_name='isSchedulable')
    '''Checks for equality with the object’s `isSchedulable` field.'''



class ControllableComponentInput(sgqlc.types.Input):
    '''An input for mutations affecting `ControllableComponent`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at', 'is_schedulable')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')

    description = sgqlc.types.Field(String, graphql_name='description')

    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    is_schedulable = sgqlc.types.Field(Boolean, graphql_name='isSchedulable')
    '''Indicator noting if the controllable component can be scheduled
    for a control event
    '''



class ControllableComponentPatch(sgqlc.types.Input):
    '''Represents an update to a `ControllableComponent`. Fields that are
    set will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at', 'is_schedulable')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    slug = sgqlc.types.Field(String, graphql_name='slug')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    label = sgqlc.types.Field(String, graphql_name='label')

    description = sgqlc.types.Field(String, graphql_name='description')

    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    is_schedulable = sgqlc.types.Field(Boolean, graphql_name='isSchedulable')
    '''Indicator noting if the controllable component can be scheduled
    for a control event
    '''



class CreateControlEventInput(sgqlc.types.Input):
    '''All input for the create `ControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    control_event = sgqlc.types.Field(sgqlc.types.non_null(ControlEventInput), graphql_name='controlEvent')
    '''The `ControlEvent` to be created by this mutation.'''



class CreateControllableComponentInput(sgqlc.types.Input):
    '''All input for the create `ControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    controllable_component = sgqlc.types.Field(ControllableComponentInput, graphql_name='controllableComponent')
    '''The `ControllableComponent` to be created by this mutation.'''



class CreateEdgeNodeInput(sgqlc.types.Input):
    '''All input for the create `EdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    edge_node = sgqlc.types.Field(sgqlc.types.non_null('EdgeNodeInput'), graphql_name='edgeNode')
    '''The `EdgeNode` to be created by this mutation.'''



class CreateEventProposalInput(sgqlc.types.Input):
    '''All input for the create `EventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    event_proposal = sgqlc.types.Field(sgqlc.types.non_null('EventProposalInput'), graphql_name='eventProposal')
    '''The `EventProposal` to be created by this mutation.'''



class CreateEventProposalMetricInput(sgqlc.types.Input):
    '''All input for the create `EventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_metric')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    event_proposal_metric = sgqlc.types.Field(sgqlc.types.non_null('EventProposalMetricInput'), graphql_name='eventProposalMetric')
    '''The `EventProposalMetric` to be created by this mutation.'''



class CreateEventProposalsControlledComponentInput(sgqlc.types.Input):
    '''All input for the create `EventProposalsControlledComponent`
    mutation.
    '''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposals_controlled_component')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    event_proposals_controlled_component = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsControlledComponentInput'), graphql_name='eventProposalsControlledComponent')
    '''The `EventProposalsControlledComponent` to be created by this
    mutation.
    '''



class CreateFacilityInput(sgqlc.types.Input):
    '''All input for the create `Facility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    facility = sgqlc.types.Field(sgqlc.types.non_null('FacilityInput'), graphql_name='facility')
    '''The `Facility` to be created by this mutation.'''



class CreateFacilityProjectInput(sgqlc.types.Input):
    '''All input for the create `FacilityProject` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    facility_project = sgqlc.types.Field(sgqlc.types.non_null('FacilityProjectInput'), graphql_name='facilityProject')
    '''The `FacilityProject` to be created by this mutation.'''



class CreateFacilityUserInput(sgqlc.types.Input):
    '''All input for the create `FacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    facility_user = sgqlc.types.Field(sgqlc.types.non_null('FacilityUserInput'), graphql_name='facilityUser')
    '''The `FacilityUser` to be created by this mutation.'''



class CreateOrganizationInput(sgqlc.types.Input):
    '''All input for the create `Organization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    organization = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInput'), graphql_name='organization')
    '''The `Organization` to be created by this mutation.'''



class CreateProjectAgentInput(sgqlc.types.Input):
    '''All input for the create `ProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_agent')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    project_agent = sgqlc.types.Field(sgqlc.types.non_null('ProjectAgentInput'), graphql_name='projectAgent')
    '''The `ProjectAgent` to be created by this mutation.'''



class CreateProjectInput(sgqlc.types.Input):
    '''All input for the create `Project` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    project = sgqlc.types.Field(sgqlc.types.non_null('ProjectInput'), graphql_name='project')
    '''The `Project` to be created by this mutation.'''



class CreateProjectSuccessMetricInput(sgqlc.types.Input):
    '''All input for the create `ProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    project_success_metric = sgqlc.types.Field(sgqlc.types.non_null('ProjectSuccessMetricInput'), graphql_name='projectSuccessMetric')
    '''The `ProjectSuccessMetric` to be created by this mutation.'''



class CreateProjectTypeInput(sgqlc.types.Input):
    '''All input for the create `ProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    project_type = sgqlc.types.Field(sgqlc.types.non_null('ProjectTypeInput'), graphql_name='projectType')
    '''The `ProjectType` to be created by this mutation.'''



class CreateStateDefinitionInput(sgqlc.types.Input):
    '''All input for the create `StateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_definition')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    state_definition = sgqlc.types.Field(sgqlc.types.non_null('StateDefinitionInput'), graphql_name='stateDefinition')
    '''The `StateDefinition` to be created by this mutation.'''



class CreateStateMachineInput(sgqlc.types.Input):
    '''All input for the create `StateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_machine')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    state_machine = sgqlc.types.Field(sgqlc.types.non_null('StateMachineInput'), graphql_name='stateMachine')
    '''The `StateMachine` to be created by this mutation.'''



class CreateUserInput(sgqlc.types.Input):
    '''All input for the create `User` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    user = sgqlc.types.Field(sgqlc.types.non_null('UserInput'), graphql_name='user')
    '''The `User` to be created by this mutation.'''



class DeleteControlEventByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteControlEventByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEvent` to be deleted.
    '''



class DeleteControlEventInput(sgqlc.types.Input):
    '''All input for the `deleteControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteControlEventLogByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteControlEventLogByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEventLog` to be deleted.
    '''



class DeleteControlEventLogInput(sgqlc.types.Input):
    '''All input for the `deleteControlEventLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteControlEventStateByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteControlEventStateByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEventState` to be deleted.
    '''



class DeleteControlEventStateInput(sgqlc.types.Input):
    '''All input for the `deleteControlEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')



class DeleteControllableComponentByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteControllableComponentByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControllableComponent` to be deleted.
    '''



class DeleteControllableComponentBySlugAndFacilityIdInput(sgqlc.types.Input):
    '''All input for the `deleteControllableComponentBySlugAndFacilityId`
    mutation.
    '''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'slug', 'facility_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')



class DeleteControllableComponentInput(sgqlc.types.Input):
    '''All input for the `deleteControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteEdgeNodeByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteEdgeNodeByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `EdgeNode`
    to be deleted.
    '''



class DeleteEdgeNodeInput(sgqlc.types.Input):
    '''All input for the `deleteEdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'client_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')



class DeleteEventProposalByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposalByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposal` to be deleted.
    '''



class DeleteEventProposalInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteEventProposalLogByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposalLogByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposalLog` to be deleted.
    '''



class DeleteEventProposalLogInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposalLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteEventProposalMetricByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposalMetricByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposalMetric` to be deleted.
    '''



class DeleteEventProposalMetricInput(sgqlc.types.Input):
    '''All input for the `deleteEventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteFacilityByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteFacilityByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `Facility`
    to be deleted.
    '''



class DeleteFacilityInput(sgqlc.types.Input):
    '''All input for the `deleteFacility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')



class DeleteFacilityUserByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteFacilityUserByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `FacilityUser` to be deleted.
    '''



class DeleteFacilityUserInput(sgqlc.types.Input):
    '''All input for the `deleteFacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteOrganizationByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteOrganizationByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `Organization` to be deleted.
    '''



class DeleteOrganizationInput(sgqlc.types.Input):
    '''All input for the `deleteOrganization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteProjectAgentByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteProjectAgentByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectAgent` to be deleted.
    '''



class DeleteProjectAgentInput(sgqlc.types.Input):
    '''All input for the `deleteProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteProjectByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteProjectByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `Project` to
    be deleted.
    '''



class DeleteProjectInput(sgqlc.types.Input):
    '''All input for the `deleteProject` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class DeleteProjectSuccessMetricByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteProjectSuccessMetricByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectSuccessMetric` to be deleted.
    '''



class DeleteProjectSuccessMetricInput(sgqlc.types.Input):
    '''All input for the `deleteProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteProjectTypeByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteProjectTypeByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectType` to be deleted.
    '''



class DeleteProjectTypeInput(sgqlc.types.Input):
    '''All input for the `deleteProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class DeleteStateDefinitionByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteStateDefinitionByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `StateDefinition` to be deleted.
    '''



class DeleteStateDefinitionInput(sgqlc.types.Input):
    '''All input for the `deleteStateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'slug')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')



class DeleteStateMachineByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteStateMachineByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `StateMachine` to be deleted.
    '''



class DeleteStateMachineInput(sgqlc.types.Input):
    '''All input for the `deleteStateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class DeleteUserByNodeIdInput(sgqlc.types.Input):
    '''All input for the `deleteUserByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `User` to be
    deleted.
    '''



class DeleteUserInput(sgqlc.types.Input):
    '''All input for the `deleteUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')



class EdgeNodeCondition(sgqlc.types.Input):
    '''A condition to be used against `EdgeNode` object types. All fields
    are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'created_at', 'updated_at', 'facility_id', 'last_fetch_time')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    '''Checks for equality with the object’s `clientId` field.'''

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    '''Checks for equality with the object’s `organizationId` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    '''Checks for equality with the object’s `facilityId` field.'''

    last_fetch_time = sgqlc.types.Field(Datetime, graphql_name='lastFetchTime')
    '''Checks for equality with the object’s `lastFetchTime` field.'''



class EdgeNodeInput(sgqlc.types.Input):
    '''An input for mutations affecting `EdgeNode`'''
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'created_at', 'updated_at', 'facility_id', 'last_fetch_time')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    last_fetch_time = sgqlc.types.Field(Datetime, graphql_name='lastFetchTime')
    '''The last time the edge communicated with the system to fetch
    control events
    '''



class EdgeNodePatch(sgqlc.types.Input):
    '''Represents an update to a `EdgeNode`. Fields that are set will be
    updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'created_at', 'updated_at', 'facility_id', 'last_fetch_time')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    last_fetch_time = sgqlc.types.Field(Datetime, graphql_name='lastFetchTime')
    '''The last time the edge communicated with the system to fetch
    control events
    '''



class EventApprovalInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting `EventApprovalInputRecord`'''
    __schema__ = control_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(UUID, graphql_name='id')



class EventProposalCondition(sgqlc.types.Input):
    '''A condition to be used against `EventProposal` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'facility_id', 'start_time', 'end_time', 'type', 'current_state', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Checks for equality with the object’s `projectId` field.'''

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    '''Checks for equality with the object’s `facilityId` field.'''

    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    '''Checks for equality with the object’s `startTime` field.'''

    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    '''Checks for equality with the object’s `endTime` field.'''

    type = sgqlc.types.Field(String, graphql_name='type')
    '''Checks for equality with the object’s `type` field.'''

    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    '''Checks for equality with the object’s `currentState` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class EventProposalInput(sgqlc.types.Input):
    '''An input for mutations affecting `EventProposal`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'facility_id', 'start_time', 'end_time', 'type', 'current_state', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')

    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class EventProposalInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting `EventProposalInputRecord`'''
    __schema__ = control_schema
    __field_names__ = ('starttime', 'endtime', 'facilityid', 'projectid')
    starttime = sgqlc.types.Field(Datetime, graphql_name='starttime')

    endtime = sgqlc.types.Field(Datetime, graphql_name='endtime')

    facilityid = sgqlc.types.Field(Int, graphql_name='facilityid')

    projectid = sgqlc.types.Field(String, graphql_name='projectid')



class EventProposalLogCondition(sgqlc.types.Input):
    '''A condition to be used against `EventProposalLog` object types.
    All fields are tested for equality and combined with a logical
    ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'previous_state', 'current_state', 'label', 'event_type', 'data', 'event_proposal_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    event_time = sgqlc.types.Field(Datetime, graphql_name='eventTime')
    '''Checks for equality with the object’s `eventTime` field.'''

    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')
    '''Checks for equality with the object’s `byUserId` field.'''

    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')
    '''Checks for equality with the object’s `byEdgeNodeId` field.'''

    previous_state = sgqlc.types.Field(String, graphql_name='previousState')
    '''Checks for equality with the object’s `previousState` field.'''

    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    '''Checks for equality with the object’s `currentState` field.'''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''Checks for equality with the object’s `label` field.'''

    event_type = sgqlc.types.Field(String, graphql_name='eventType')
    '''Checks for equality with the object’s `eventType` field.'''

    data = sgqlc.types.Field(JSON, graphql_name='data')
    '''Checks for equality with the object’s `data` field.'''

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''Checks for equality with the object’s `eventProposalId` field.'''



class EventProposalLogPatch(sgqlc.types.Input):
    '''Represents an update to a `EventProposalLog`. Fields that are set
    will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'previous_state', 'current_state', 'label', 'event_type', 'data', 'event_proposal_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    event_time = sgqlc.types.Field(Datetime, graphql_name='eventTime')

    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')

    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')

    previous_state = sgqlc.types.Field(String, graphql_name='previousState')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    label = sgqlc.types.Field(String, graphql_name='label')

    event_type = sgqlc.types.Field(String, graphql_name='eventType')

    data = sgqlc.types.Field(JSON, graphql_name='data')

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')



class EventProposalMetricCondition(sgqlc.types.Input):
    '''A condition to be used against `EventProposalMetric` object types.
    All fields are tested for equality and combined with a logical
    ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at', 'actual_impact_amount', 'controllable_component_id', 'id', 'event_proposal_id', 'calculation_metadata')
    project_success_metric_id = sgqlc.types.Field(UUID, graphql_name='projectSuccessMetricId')
    '''Checks for equality with the object’s `projectSuccessMetricId`
    field.
    '''

    projected_impact_amount = sgqlc.types.Field(Float, graphql_name='projectedImpactAmount')
    '''Checks for equality with the object’s `projectedImpactAmount`
    field.
    '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    actual_impact_amount = sgqlc.types.Field(Float, graphql_name='actualImpactAmount')
    '''Checks for equality with the object’s `actualImpactAmount` field.'''

    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')
    '''Checks for equality with the object’s `controllableComponentId`
    field.
    '''

    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''Checks for equality with the object’s `eventProposalId` field.'''

    calculation_metadata = sgqlc.types.Field(JSON, graphql_name='calculationMetadata')
    '''Checks for equality with the object’s `calculationMetadata` field.'''



class EventProposalMetricInput(sgqlc.types.Input):
    '''An input for mutations affecting `EventProposalMetric`'''
    __schema__ = control_schema
    __field_names__ = ('project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at', 'actual_impact_amount', 'controllable_component_id', 'id', 'event_proposal_id', 'calculation_metadata')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')
    '''E'@manyToManyFieldName projectSuccessMetrics' '''

    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    actual_impact_amount = sgqlc.types.Field(Float, graphql_name='actualImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    '''The associated controllable component the savings for this event
    are associated with
    '''

    id = sgqlc.types.Field(UUID, graphql_name='id')

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    calculation_metadata = sgqlc.types.Field(JSON, graphql_name='calculationMetadata')



class EventProposalMetricPatch(sgqlc.types.Input):
    '''Represents an update to a `EventProposalMetric`. Fields that are
    set will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at', 'actual_impact_amount', 'controllable_component_id', 'id', 'event_proposal_id', 'calculation_metadata')
    project_success_metric_id = sgqlc.types.Field(UUID, graphql_name='projectSuccessMetricId')
    '''E'@manyToManyFieldName projectSuccessMetrics' '''

    projected_impact_amount = sgqlc.types.Field(Float, graphql_name='projectedImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    actual_impact_amount = sgqlc.types.Field(Float, graphql_name='actualImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')
    '''The associated controllable component the savings for this event
    are associated with
    '''

    id = sgqlc.types.Field(UUID, graphql_name='id')

    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')

    calculation_metadata = sgqlc.types.Field(JSON, graphql_name='calculationMetadata')



class EventProposalPatch(sgqlc.types.Input):
    '''Represents an update to a `EventProposal`. Fields that are set
    will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'facility_id', 'start_time', 'end_time', 'type', 'current_state', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')

    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')

    type = sgqlc.types.Field(String, graphql_name='type')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class EventProposalsControlledComponentCondition(sgqlc.types.Input):
    '''A condition to be used against `EventProposalsControlledComponent`
    object types. All fields are tested for equality and combined with
    a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('event_proposal_id', 'controllable_component_id', 'created_at', 'updated_at', 'state_definition')
    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''Checks for equality with the object’s `eventProposalId` field.'''

    controllable_component_id = sgqlc.types.Field(UUID, graphql_name='controllableComponentId')
    '''Checks for equality with the object’s `controllableComponentId`
    field.
    '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    state_definition = sgqlc.types.Field(String, graphql_name='stateDefinition')
    '''Checks for equality with the object’s `stateDefinition` field.'''



class EventProposalsControlledComponentInput(sgqlc.types.Input):
    '''An input for mutations affecting
    `EventProposalsControlledComponent`
    '''
    __schema__ = control_schema
    __field_names__ = ('event_proposal_id', 'controllable_component_id', 'created_at', 'updated_at', 'state_definition')
    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''E'@manyToManyFieldName controlEvents' '''

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    '''E'@manyToManyFieldName controlledComponents' '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    state_definition = sgqlc.types.Field(String, graphql_name='stateDefinition')



class FacilityCondition(sgqlc.types.Input):
    '''A condition to be used against `Facility` object types. All fields
    are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Checks for equality with the object’s `name` field.'''

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    '''Checks for equality with the object’s `organizationId` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class FacilityInput(sgqlc.types.Input):
    '''An input for mutations affecting `Facility`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class FacilityPatch(sgqlc.types.Input):
    '''Represents an update to a `Facility`. Fields that are set will be
    updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class FacilityProjectCondition(sgqlc.types.Input):
    '''A condition to be used against `FacilityProject` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status', 'auto_approve')
    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    '''Checks for equality with the object’s `facilityId` field.'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Checks for equality with the object’s `projectId` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    enrollment_status = sgqlc.types.Field(String, graphql_name='enrollmentStatus')
    '''Checks for equality with the object’s `enrollmentStatus` field.'''

    auto_approve = sgqlc.types.Field(Boolean, graphql_name='autoApprove')
    '''Checks for equality with the object’s `autoApprove` field.'''



class FacilityProjectInput(sgqlc.types.Input):
    '''An input for mutations affecting `FacilityProject`'''
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status', 'auto_approve')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    '''E'@manyToManyFieldName facilities' '''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    '''E'@manyToManyFieldName projects' '''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    enrollment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='enrollmentStatus')

    auto_approve = sgqlc.types.Field(Boolean, graphql_name='autoApprove')
    '''If enabled, this project at this particular facility will skip the
    approval process
    '''



class FacilityUserCondition(sgqlc.types.Input):
    '''A condition to be used against `FacilityUser` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')
    '''Checks for equality with the object’s `facilityId` field.'''

    user_id = sgqlc.types.Field(String, graphql_name='userId')
    '''Checks for equality with the object’s `userId` field.'''

    role = sgqlc.types.Field(String, graphql_name='role')
    '''Checks for equality with the object’s `role` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class FacilityUserInput(sgqlc.types.Input):
    '''An input for mutations affecting `FacilityUser`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')

    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')

    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class FacilityUserPatch(sgqlc.types.Input):
    '''Represents an update to a `FacilityUser`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'facility_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    user_id = sgqlc.types.Field(String, graphql_name='userId')

    role = sgqlc.types.Field(String, graphql_name='role')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class HistoricEventProposalInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting
    `HistoricEventProposalInputRecord`
    '''
    __schema__ = control_schema
    __field_names__ = ('starttime', 'endtime', 'facilityid', 'projectid')
    starttime = sgqlc.types.Field(Datetime, graphql_name='starttime')

    endtime = sgqlc.types.Field(Datetime, graphql_name='endtime')

    facilityid = sgqlc.types.Field(Int, graphql_name='facilityid')

    projectid = sgqlc.types.Field(String, graphql_name='projectid')



class OrganizationCondition(sgqlc.types.Input):
    '''A condition to be used against `Organization` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Checks for equality with the object’s `name` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class OrganizationInput(sgqlc.types.Input):
    '''An input for mutations affecting `Organization`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class OrganizationPatch(sgqlc.types.Input):
    '''Represents an update to a `Organization`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectAgentCondition(sgqlc.types.Input):
    '''A condition to be used against `ProjectAgent` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Checks for equality with the object’s `projectId` field.'''

    user_id = sgqlc.types.Field(String, graphql_name='userId')
    '''Checks for equality with the object’s `userId` field.'''

    role = sgqlc.types.Field(String, graphql_name='role')
    '''Checks for equality with the object’s `role` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class ProjectAgentInput(sgqlc.types.Input):
    '''An input for mutations affecting `ProjectAgent`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')

    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectAgentPatch(sgqlc.types.Input):
    '''Represents an update to a `ProjectAgent`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'user_id', 'role', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    user_id = sgqlc.types.Field(String, graphql_name='userId')

    role = sgqlc.types.Field(String, graphql_name='role')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectCondition(sgqlc.types.Input):
    '''A condition to be used against `Project` object types. All fields
    are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at', 'auto_review')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Checks for equality with the object’s `name` field.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Checks for equality with the object’s `description` field.'''

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')
    '''Checks for equality with the object’s `organizationId` field.'''

    project_type_id = sgqlc.types.Field(String, graphql_name='projectTypeId')
    '''Checks for equality with the object’s `projectTypeId` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''

    auto_review = sgqlc.types.Field(Boolean, graphql_name='autoReview')
    '''Checks for equality with the object’s `autoReview` field.'''



class ProjectInput(sgqlc.types.Input):
    '''An input for mutations affecting `Project`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at', 'auto_review')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    project_type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectTypeId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    auto_review = sgqlc.types.Field(Boolean, graphql_name='autoReview')
    '''If enabled, this project will skip the review process'''



class ProjectPatch(sgqlc.types.Input):
    '''Represents an update to a `Project`. Fields that are set will be
    updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at', 'auto_review')
    id = sgqlc.types.Field(String, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    description = sgqlc.types.Field(String, graphql_name='description')

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')

    project_type_id = sgqlc.types.Field(String, graphql_name='projectTypeId')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')

    auto_review = sgqlc.types.Field(Boolean, graphql_name='autoReview')
    '''If enabled, this project will skip the review process'''



class ProjectSuccessMetricCondition(sgqlc.types.Input):
    '''A condition to be used against `ProjectSuccessMetric` object
    types. All fields are tested for equality and combined with a
    logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Checks for equality with the object’s `projectId` field.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Checks for equality with the object’s `name` field.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Checks for equality with the object’s `description` field.'''

    units = sgqlc.types.Field(String, graphql_name='units')
    '''Checks for equality with the object’s `units` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class ProjectSuccessMetricInput(sgqlc.types.Input):
    '''An input for mutations affecting `ProjectSuccessMetric`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The name of the success metric registered for the associated
    project
    '''

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    '''A brief description of how this metric is tied to savings for the
    project and what it would mean for the facility
    '''

    units = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='units')
    '''The units of this success metric'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectSuccessMetricPatch(sgqlc.types.Input):
    '''Represents an update to a `ProjectSuccessMetric`. Fields that are
    set will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The name of the success metric registered for the associated
    project
    '''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''A brief description of how this metric is tied to savings for the
    project and what it would mean for the facility
    '''

    units = sgqlc.types.Field(String, graphql_name='units')
    '''The units of this success metric'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectTypeCondition(sgqlc.types.Input):
    '''A condition to be used against `ProjectType` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Checks for equality with the object’s `name` field.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Checks for equality with the object’s `description` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class ProjectTypeInput(sgqlc.types.Input):
    '''An input for mutations affecting `ProjectType`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProjectTypePatch(sgqlc.types.Input):
    '''Represents an update to a `ProjectType`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    description = sgqlc.types.Field(String, graphql_name='description')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class ProposeEventInput(sgqlc.types.Input):
    '''All input for the `proposeEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'proposed_event', 'components_to_control')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    proposed_event = sgqlc.types.Field(sgqlc.types.non_null(EventProposalInputRecordInput), graphql_name='proposedEvent')

    components_to_control = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ComponentToControlInputRecordInput)), graphql_name='componentsToControl')



class RawControlEventInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting `RawControlEventInputRecord`'''
    __schema__ = control_schema
    __field_names__ = ('starttime', 'endtime', 'facilityid', 'projectid', 'type', 'metrics')
    starttime = sgqlc.types.Field(Datetime, graphql_name='starttime')

    endtime = sgqlc.types.Field(Datetime, graphql_name='endtime')

    facilityid = sgqlc.types.Field(Int, graphql_name='facilityid')

    projectid = sgqlc.types.Field(String, graphql_name='projectid')

    type = sgqlc.types.Field(String, graphql_name='type')

    metrics = sgqlc.types.Field(sgqlc.types.list_of('RawControlEventMetricInputRecordInput'), graphql_name='metrics')



class RawControlEventMetricInputRecordInput(sgqlc.types.Input):
    '''An input for mutations affecting
    `RawControlEventMetricInputRecord`
    '''
    __schema__ = control_schema
    __field_names__ = ('name', 'projectimpactamount')
    name = sgqlc.types.Field(String, graphql_name='name')

    projectimpactamount = sgqlc.types.Field(Float, graphql_name='projectimpactamount')



class SetControlEventsInput(sgqlc.types.Input):
    '''All input for the `setControlEvents` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_input')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    event_input = sgqlc.types.Field(sgqlc.types.non_null(RawControlEventInputRecordInput), graphql_name='eventInput')



class StateDefinitionCondition(sgqlc.types.Input):
    '''A condition to be used against `StateDefinition` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('slug', 'project_id', 'label', 'description', 'definition', 'created_at', 'updated_at')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    '''Checks for equality with the object’s `slug` field.'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Checks for equality with the object’s `projectId` field.'''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''Checks for equality with the object’s `label` field.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Checks for equality with the object’s `description` field.'''

    definition = sgqlc.types.Field(JSON, graphql_name='definition')
    '''Checks for equality with the object’s `definition` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class StateDefinitionInput(sgqlc.types.Input):
    '''An input for mutations affecting `StateDefinition`'''
    __schema__ = control_schema
    __field_names__ = ('slug', 'project_id', 'label', 'description', 'definition', 'created_at', 'updated_at')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    definition = sgqlc.types.Field(JSON, graphql_name='definition')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class StateDefinitionPatch(sgqlc.types.Input):
    '''Represents an update to a `StateDefinition`. Fields that are set
    will be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('slug', 'project_id', 'label', 'description', 'definition', 'created_at', 'updated_at')
    slug = sgqlc.types.Field(String, graphql_name='slug')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    label = sgqlc.types.Field(String, graphql_name='label')

    description = sgqlc.types.Field(String, graphql_name='description')

    definition = sgqlc.types.Field(JSON, graphql_name='definition')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class StateMachineCondition(sgqlc.types.Input):
    '''A condition to be used against `StateMachine` object types. All
    fields are tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'state_definition', 'current_state', 'context', 'machine', 'state', 'is_active', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    '''Checks for equality with the object’s `id` field.'''

    state_definition = sgqlc.types.Field(String, graphql_name='stateDefinition')
    '''Checks for equality with the object’s `stateDefinition` field.'''

    current_state = sgqlc.types.Field(String, graphql_name='currentState')
    '''Checks for equality with the object’s `currentState` field.'''

    context = sgqlc.types.Field(JSON, graphql_name='context')
    '''Checks for equality with the object’s `context` field.'''

    machine = sgqlc.types.Field(JSON, graphql_name='machine')
    '''Checks for equality with the object’s `machine` field.'''

    state = sgqlc.types.Field(JSON, graphql_name='state')
    '''Checks for equality with the object’s `state` field.'''

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    '''Checks for equality with the object’s `isActive` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class StateMachineInput(sgqlc.types.Input):
    '''An input for mutations affecting `StateMachine`'''
    __schema__ = control_schema
    __field_names__ = ('id', 'state_definition', 'current_state', 'context', 'machine', 'state', 'is_active', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    state_definition = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stateDefinition')

    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')

    context = sgqlc.types.Field(JSON, graphql_name='context')

    machine = sgqlc.types.Field(JSON, graphql_name='machine')

    state = sgqlc.types.Field(JSON, graphql_name='state')

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class StateMachinePatch(sgqlc.types.Input):
    '''Represents an update to a `StateMachine`. Fields that are set will
    be updated.
    '''
    __schema__ = control_schema
    __field_names__ = ('id', 'state_definition', 'current_state', 'context', 'machine', 'state', 'is_active', 'created_at', 'updated_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')

    state_definition = sgqlc.types.Field(String, graphql_name='stateDefinition')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    context = sgqlc.types.Field(JSON, graphql_name='context')

    machine = sgqlc.types.Field(JSON, graphql_name='machine')

    state = sgqlc.types.Field(JSON, graphql_name='state')

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class TransitionControlEventInput(sgqlc.types.Input):
    __schema__ = control_schema
    __field_names__ = ('control_event_id', 'transition_event')
    control_event_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='controlEventId')

    transition_event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='transitionEvent')



class UpdateControlEventByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateControlEventByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEvent` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ControlEvent`
    being updated.
    '''



class UpdateControlEventInput(sgqlc.types.Input):
    '''All input for the `updateControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ControlEvent`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateControlEventLogByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateControlEventLogByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEventLog` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControlEventLog` being updated.
    '''



class UpdateControlEventLogInput(sgqlc.types.Input):
    '''All input for the `updateControlEventLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventLogPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControlEventLog` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateControlEventStateByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateControlEventStateByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControlEventState` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStatePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControlEventState` being updated.
    '''



class UpdateControlEventStateInput(sgqlc.types.Input):
    '''All input for the `updateControlEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStatePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControlEventState` being updated.
    '''

    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')



class UpdateControllableComponentByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateControllableComponentByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ControllableComponent` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControllableComponent` being updated.
    '''



class UpdateControllableComponentBySlugAndFacilityIdInput(sgqlc.types.Input):
    '''All input for the `updateControllableComponentBySlugAndFacilityId`
    mutation.
    '''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'slug', 'facility_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControllableComponent` being updated.
    '''

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')



class UpdateControllableComponentInput(sgqlc.types.Input):
    '''All input for the `updateControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ControllableComponent` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateEdgeNodeByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateEdgeNodeByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `EdgeNode`
    to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `EdgeNode`
    being updated.
    '''



class UpdateEdgeNodeInput(sgqlc.types.Input):
    '''All input for the `updateEdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'client_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `EdgeNode`
    being updated.
    '''

    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')



class UpdateEventProposalByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateEventProposalByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposal` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposal` being updated.
    '''



class UpdateEventProposalInput(sgqlc.types.Input):
    '''All input for the `updateEventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposal` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateEventProposalLogByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateEventProposalLogByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposalLog` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposalLog` being updated.
    '''



class UpdateEventProposalLogInput(sgqlc.types.Input):
    '''All input for the `updateEventProposalLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposalLog` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateEventProposalMetricByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateEventProposalMetricByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `EventProposalMetric` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposalMetric` being updated.
    '''



class UpdateEventProposalMetricInput(sgqlc.types.Input):
    '''All input for the `updateEventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `EventProposalMetric` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateFacilityByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateFacilityByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `Facility`
    to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Facility`
    being updated.
    '''



class UpdateFacilityInput(sgqlc.types.Input):
    '''All input for the `updateFacility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Facility`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')



class UpdateFacilityUserByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateFacilityUserByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `FacilityUser` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityUserPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `FacilityUser`
    being updated.
    '''



class UpdateFacilityUserInput(sgqlc.types.Input):
    '''All input for the `updateFacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(FacilityUserPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `FacilityUser`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateOrganizationByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateOrganizationByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `Organization` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(OrganizationPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Organization`
    being updated.
    '''



class UpdateOrganizationInput(sgqlc.types.Input):
    '''All input for the `updateOrganization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(OrganizationPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Organization`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateProjectAgentByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateProjectAgentByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectAgent` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ProjectAgent`
    being updated.
    '''



class UpdateProjectAgentInput(sgqlc.types.Input):
    '''All input for the `updateProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ProjectAgent`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateProjectByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateProjectByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `Project` to
    be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Project`
    being updated.
    '''



class UpdateProjectInput(sgqlc.types.Input):
    '''All input for the `updateProject` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `Project`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class UpdateProjectSuccessMetricByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateProjectSuccessMetricByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectSuccessMetric` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ProjectSuccessMetric` being updated.
    '''



class UpdateProjectSuccessMetricInput(sgqlc.types.Input):
    '''All input for the `updateProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `ProjectSuccessMetric` being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateProjectTypeByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateProjectTypeByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `ProjectType` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectTypePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ProjectType`
    being updated.
    '''



class UpdateProjectTypeInput(sgqlc.types.Input):
    '''All input for the `updateProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(ProjectTypePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `ProjectType`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class UpdateStateDefinitionByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateStateDefinitionByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `StateDefinition` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(StateDefinitionPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `StateDefinition` being updated.
    '''



class UpdateStateDefinitionInput(sgqlc.types.Input):
    '''All input for the `updateStateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'slug')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(StateDefinitionPatch), graphql_name='patch')
    '''An object where the defined keys will be set on the
    `StateDefinition` being updated.
    '''

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')



class UpdateStateMachineByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateStateMachineByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single
    `StateMachine` to be updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(StateMachinePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `StateMachine`
    being updated.
    '''



class UpdateStateMachineInput(sgqlc.types.Input):
    '''All input for the `updateStateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null(StateMachinePatch), graphql_name='patch')
    '''An object where the defined keys will be set on the `StateMachine`
    being updated.
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')



class UpdateUserByNodeIdInput(sgqlc.types.Input):
    '''All input for the `updateUserByNodeId` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''The globally unique `ID` which will identify a single `User` to be
    updated.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null('UserPatch'), graphql_name='patch')
    '''An object where the defined keys will be set on the `User` being
    updated.
    '''



class UpdateUserInput(sgqlc.types.Input):
    '''All input for the `updateUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'patch', 'email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''An arbitrary string value with no semantic meaning. Will be
    included in the payload verbatim. May be used to track mutations
    by the client.
    '''

    patch = sgqlc.types.Field(sgqlc.types.non_null('UserPatch'), graphql_name='patch')
    '''An object where the defined keys will be set on the `User` being
    updated.
    '''

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')



class UserCondition(sgqlc.types.Input):
    '''A condition to be used against `User` object types. All fields are
    tested for equality and combined with a logical ‘and.’
    '''
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    '''Checks for equality with the object’s `firstName` field.'''

    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    '''Checks for equality with the object’s `lastName` field.'''

    email = sgqlc.types.Field(String, graphql_name='email')
    '''Checks for equality with the object’s `email` field.'''

    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    '''Checks for equality with the object’s `phoneNumber` field.'''

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    '''Checks for equality with the object’s `createdAt` field.'''

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    '''Checks for equality with the object’s `updatedAt` field.'''



class UserInput(sgqlc.types.Input):
    '''An input for mutations affecting `User`'''
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')

    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    phone_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phoneNumber')

    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')



class UserPatch(sgqlc.types.Input):
    '''Represents an update to a `User`. Fields that are set will be
    updated.
    '''
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
class AddHistoricEventPayload(sgqlc.types.Type):
    '''The output of our `addHistoricEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class ApproveProposalPayload(sgqlc.types.Type):
    '''The output of our `approveProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class ApproveProposalReviewPayload(sgqlc.types.Type):
    '''The output of our `approveProposalReview` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class ChangeEventStatePayload(sgqlc.types.Type):
    '''The output of our `changeEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'control_event_state_by_current_state', 'event_proposal', 'controllable_component', 'state_machine', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEvent`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `ControlEvent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `ControlEvent`.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''Reads a single `StateMachine` that is related to this
    `ControlEvent`.
    '''

    control_event_edge = sgqlc.types.Field('ControlEventsEdge', graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEvent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class ChangeProposalStatePayload(sgqlc.types.Type):
    '''The output of our `changeProposalState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventControlEventStatesByControlEventLogControlEventIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventControlEventStatesByControlEventLogControlEventIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class ControlEventEdgeNodesByControlEventLogControlEventIdAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventLogsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventLog` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventLog')), graphql_name='nodes')
    '''A list of `ControlEventLog` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventLogsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventLog` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventLog` you could get from the
    connection.
    '''



class ControlEventLogsEdge(sgqlc.types.Type):
    '''A `ControlEventLog` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventLog', graphql_name='node')
    '''The `ControlEventLog` at the end of the edge.'''



class ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventStateControlEventStatesByControlEventLogCurrentStateAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventStateControlEventStatesByControlEventLogPreviousStateAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControlEventStatesByEventProposalLogCurrentStateAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByEventProposalLogCurrentStateAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventStateControlEventStatesByEventProposalLogCurrentStateAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControlEventStatesByEventProposalLogPreviousStateAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventStatesByEventProposalLogPreviousStateAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventStateControlEventStatesByEventProposalLogPreviousStateAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEvent` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    '''A list of `ControlEvent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEvent`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEvent` you could get from the
    connection.
    '''



class ControlEventStateControlEventsByControlEventLogCurrentStateAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEvent` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    '''The `ControlEvent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEvent` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    '''A list of `ControlEvent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEvent`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEvent` you could get from the
    connection.
    '''



class ControlEventStateControlEventsByControlEventLogPreviousStateAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEvent` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    '''The `ControlEvent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateControllableComponentsByControlEventCurrentStateAndControllableComponentIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateControllableComponentsByControlEventCurrentStateAndControllableComponentIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class ControlEventStateControllableComponentsByControlEventCurrentStateAndControllableComponentIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class ControlEventStateEdgeNodesByControlEventLogCurrentStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class ControlEventStateEdgeNodesByControlEventLogPreviousStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateEdgeNodesByEventProposalLogCurrentStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByEventProposalLogCurrentStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class ControlEventStateEdgeNodesByEventProposalLogCurrentStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

    event_proposal_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateEdgeNodesByEventProposalLogPreviousStateAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEdgeNodesByEventProposalLogPreviousStateAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class ControlEventStateEdgeNodesByEventProposalLogPreviousStateAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

    event_proposal_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateEventProposalsByControlEventCurrentStateAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEventProposalsByControlEventCurrentStateAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControlEventStateEventProposalsByControlEventCurrentStateAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControlEventStateEventProposalsByEventProposalLogCurrentStateAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEventProposalsByEventProposalLogCurrentStateAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControlEventStateEventProposalsByEventProposalLogCurrentStateAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_logs = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateEventProposalsByEventProposalLogPreviousStateAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateEventProposalsByEventProposalLogPreviousStateAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControlEventStateEventProposalsByEventProposalLogPreviousStateAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_logs = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateFacilitiesByEventProposalCurrentStateAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateFacilitiesByEventProposalCurrentStateAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class ControlEventStateFacilitiesByEventProposalCurrentStateAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsConnection'), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateProjectsByEventProposalCurrentStateAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Project` values, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    '''A list of `Project` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateProjectsByEventProposalCurrentStateAndProjectIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Project`, info from the
    `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Project` you could get from the connection.'''



class ControlEventStateProjectsByEventProposalCurrentStateAndProjectIdManyToManyEdge(sgqlc.types.Type):
    '''A `Project` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Project', graphql_name='node')
    '''The `Project` at the end of the edge.'''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsConnection'), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ControlEventStateStateMachinesByControlEventCurrentStateAndStateMachineIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateMachine` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateMachine')), graphql_name='nodes')
    '''A list of `StateMachine` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateStateMachinesByControlEventCurrentStateAndStateMachineIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateMachine`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateMachine` you could get from the
    connection.
    '''



class ControlEventStateStateMachinesByControlEventCurrentStateAndStateMachineIdManyToManyEdge(sgqlc.types.Type):
    '''A `StateMachine` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateMachine', graphql_name='node')
    '''The `StateMachine` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControlEventStateUsersByEventProposalLogCurrentStateAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateUsersByEventProposalLogCurrentStateAndByUserIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class ControlEventStateUsersByEventProposalLogCurrentStateAndByUserIdManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

    event_proposal_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStateUsersByEventProposalLogPreviousStateAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStateUsersByEventProposalLogPreviousStateAndByUserIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class ControlEventStateUsersByEventProposalLogPreviousStateAndByUserIdManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

    event_proposal_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventStatesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventStatesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState` and cursor
    to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControlEventStatesEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''



class ControlEventsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEvent` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    '''A list of `ControlEvent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControlEventsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEvent` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEvent` you could get from the
    connection.
    '''



class ControlEventsEdge(sgqlc.types.Type):
    '''A `ControlEvent` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    '''The `ControlEvent` at the end of the edge.'''



class ControllableComponentControlEventStatesByControlEventControllableComponentIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentControlEventStatesByControlEventControllableComponentIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ControllableComponentControlEventStatesByControlEventControllableComponentIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControllableComponentEventProposalsByControlEventControllableComponentIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentEventProposalsByControlEventControllableComponentIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControllableComponentEventProposalsByControlEventControllableComponentIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControllableComponentEventProposalsByEventProposalMetricControllableComponentIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentEventProposalsByEventProposalMetricControllableComponentIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalMetric`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControllableComponentEventProposalsByEventProposalMetricControllableComponentIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null('EventProposalMetricsConnection'), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControllableComponentEventProposalsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentEventProposalsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalsControlledComponent`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ControllableComponentEventProposalsManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsControlledComponentsConnection'), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class ControllableComponentProjectSuccessMetricsByEventProposalMetricControllableComponentIdAndProjectSuccessMetricIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectSuccessMetric` values, with data
    from `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectSuccessMetric')), graphql_name='nodes')
    '''A list of `ProjectSuccessMetric` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentProjectSuccessMetricsByEventProposalMetricControllableComponentIdAndProjectSuccessMetricIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectSuccessMetric`, info
    from the `EventProposalMetric`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectSuccessMetric` you could get from the
    connection.
    '''



class ControllableComponentProjectSuccessMetricsByEventProposalMetricControllableComponentIdAndProjectSuccessMetricIdManyToManyEdge(sgqlc.types.Type):
    '''A `ProjectSuccessMetric` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='node')
    '''The `ProjectSuccessMetric` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null('EventProposalMetricsConnection'), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControllableComponentStateDefinitionsByEventProposalsControlledComponentControllableComponentIdAndStateDefinitionManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateDefinition` values, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateDefinition')), graphql_name='nodes')
    '''A list of `StateDefinition` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentStateDefinitionsByEventProposalsControlledComponentControllableComponentIdAndStateDefinitionManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateDefinition`, info from
    the `EventProposalsControlledComponent`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateDefinition` you could get from the
    connection.
    '''



class ControllableComponentStateDefinitionsByEventProposalsControlledComponentControllableComponentIdAndStateDefinitionManyToManyEdge(sgqlc.types.Type):
    '''A `StateDefinition` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components_by_state_definition')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateDefinition', graphql_name='node')
    '''The `StateDefinition` at the end of the edge.'''

    event_proposals_controlled_components_by_state_definition = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsControlledComponentsConnection'), graphql_name='eventProposalsControlledComponentsByStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class ControllableComponentStateMachinesByControlEventControllableComponentIdAndStateMachineIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateMachine` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateMachine')), graphql_name='nodes')
    '''A list of `StateMachine` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentStateMachinesByControlEventControllableComponentIdAndStateMachineIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateMachine`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateMachine` you could get from the
    connection.
    '''



class ControllableComponentStateMachinesByControlEventControllableComponentIdAndStateMachineIdManyToManyEdge(sgqlc.types.Type):
    '''A `StateMachine` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateMachine', graphql_name='node')
    '''The `StateMachine` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ControllableComponentsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ControllableComponentsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent` and
    cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class ControllableComponentsEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''



class CreateControlEventPayload(sgqlc.types.Type):
    '''The output of our create `ControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'control_event_state_by_current_state', 'event_proposal', 'controllable_component', 'state_machine', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    '''The `ControlEvent` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEvent`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `ControlEvent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `ControlEvent`.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''Reads a single `StateMachine` that is related to this
    `ControlEvent`.
    '''

    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEvent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateControllableComponentPayload(sgqlc.types.Type):
    '''The output of our create `ControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''The `ControllableComponent` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `ControllableComponent`.
    '''

    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    '''Reads a single `EdgeNode` that is related to this
    `ControllableComponent`.
    '''

    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControllableComponent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class CreateEdgeNodePayload(sgqlc.types.Type):
    '''The output of our create `EdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'query', 'organization', 'facility', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    '''The `EdgeNode` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `EdgeNode`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EdgeNode`.'''

    edge_node_edge = sgqlc.types.Field('EdgeNodesEdge', graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EdgeNode`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateEventProposalMetricPayload(sgqlc.types.Type):
    '''The output of our create `EventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_metric', 'query', 'project_success_metric', 'controllable_component', 'event_proposal', 'event_proposal_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal_metric = sgqlc.types.Field('EventProposalMetric', graphql_name='eventProposalMetric')
    '''The `EventProposalMetric` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''Reads a single `ProjectSuccessMetric` that is related to this
    `EventProposalMetric`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal_metric_edge = sgqlc.types.Field('EventProposalMetricsEdge', graphql_name='eventProposalMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposalMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class CreateEventProposalPayload(sgqlc.types.Type):
    '''The output of our create `EventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''The `EventProposal` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateEventProposalsControlledComponentPayload(sgqlc.types.Type):
    '''The output of our create `EventProposalsControlledComponent`
    mutation.
    '''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposals_controlled_component', 'query', 'event_proposal', 'controllable_component', 'state_definition_by_state_definition', 'event_proposals_controlled_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposals_controlled_component = sgqlc.types.Field('EventProposalsControlledComponent', graphql_name='eventProposalsControlledComponent')
    '''The `EventProposalsControlledComponent` that was created by this
    mutation.
    '''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalsControlledComponent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalsControlledComponent`.
    '''

    state_definition_by_state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `EventProposalsControlledComponent`.
    '''

    event_proposals_controlled_component_edge = sgqlc.types.Field('EventProposalsControlledComponentsEdge', graphql_name='eventProposalsControlledComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )
    '''An edge for our `EventProposalsControlledComponent`. May be used
    by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    '''



class CreateFacilityPayload(sgqlc.types.Type):
    '''The output of our create `Facility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''The `Facility` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Facility`.'''

    facility_edge = sgqlc.types.Field('FacilitiesEdge', graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Facility`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateFacilityProjectPayload(sgqlc.types.Type):
    '''The output of our create `FacilityProject` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_project', 'query', 'facility', 'project', 'facility_project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility_project = sgqlc.types.Field('FacilityProject', graphql_name='facilityProject')
    '''The `FacilityProject` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `FacilityProject`.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `FacilityProject`.
    '''

    facility_project_edge = sgqlc.types.Field('FacilityProjectsEdge', graphql_name='facilityProjectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityProjectsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
))
    )
    '''An edge for our `FacilityProject`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    '''



class CreateFacilityUserPayload(sgqlc.types.Type):
    '''The output of our create `FacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    '''The `FacilityUser` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `FacilityUser`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `FacilityUser`.'''

    facility_user_edge = sgqlc.types.Field('FacilityUsersEdge', graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `FacilityUser`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateOrganizationPayload(sgqlc.types.Type):
    '''The output of our create `Organization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''The `Organization` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization_edge = sgqlc.types.Field('OrganizationsEdge', graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Organization`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateProjectAgentPayload(sgqlc.types.Type):
    '''The output of our create `ProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_agent', 'query', 'project', 'user', 'project_agent_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_agent = sgqlc.types.Field('ProjectAgent', graphql_name='projectAgent')
    '''The `ProjectAgent` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `ProjectAgent`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `ProjectAgent`.'''

    project_agent_edge = sgqlc.types.Field('ProjectAgentsEdge', graphql_name='projectAgentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectAgent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateProjectPayload(sgqlc.types.Type):
    '''The output of our create `Project` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''The `Project` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Project`.'''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''Reads a single `ProjectType` that is related to this `Project`.'''

    project_edge = sgqlc.types.Field('ProjectsEdge', graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Project`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateProjectSuccessMetricPayload(sgqlc.types.Type):
    '''The output of our create `ProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''The `ProjectSuccessMetric` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `ProjectSuccessMetric`.
    '''

    project_success_metric_edge = sgqlc.types.Field('ProjectSuccessMetricsEdge', graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectSuccessMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class CreateProjectTypePayload(sgqlc.types.Type):
    '''The output of our create `ProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''The `ProjectType` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_type_edge = sgqlc.types.Field('ProjectTypesEdge', graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectType`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectTypesOrderBy!]`): The method to use when
      ordering `ProjectType`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateStateDefinitionPayload(sgqlc.types.Type):
    '''The output of our create `StateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_definition', 'query', 'project', 'state_definition_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinition')
    '''The `StateDefinition` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `StateDefinition`.
    '''

    state_definition_edge = sgqlc.types.Field('StateDefinitionsEdge', graphql_name='stateDefinitionEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateDefinition`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateStateMachinePayload(sgqlc.types.Type):
    '''The output of our create `StateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_machine', 'query', 'state_definition_by_state_definition', 'state_machine_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''The `StateMachine` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    state_definition_by_state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `StateMachine`.
    '''

    state_machine_edge = sgqlc.types.Field('StateMachinesEdge', graphql_name='stateMachineEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateMachine`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class CreateUserPayload(sgqlc.types.Type):
    '''The output of our create `User` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''The `User` that was created by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `User`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteControlEventLogPayload(sgqlc.types.Type):
    '''The output of our delete `ControlEventLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_log', 'deleted_control_event_log_node_id', 'query', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'control_event_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event_log = sgqlc.types.Field('ControlEventLog', graphql_name='controlEventLog')
    '''The `ControlEventLog` that was deleted by this mutation.'''

    deleted_control_event_log_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventLogNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `ControlEventLog`.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    '''Reads a single `ControlEvent` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''

    control_event_log_edge = sgqlc.types.Field(ControlEventLogsEdge, graphql_name='controlEventLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEventLog`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteControlEventPayload(sgqlc.types.Type):
    '''The output of our delete `ControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'deleted_control_event_node_id', 'query', 'control_event_state_by_current_state', 'event_proposal', 'controllable_component', 'state_machine', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    '''The `ControlEvent` that was deleted by this mutation.'''

    deleted_control_event_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEvent`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `ControlEvent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `ControlEvent`.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''Reads a single `StateMachine` that is related to this
    `ControlEvent`.
    '''

    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEvent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteControlEventStatePayload(sgqlc.types.Type):
    '''The output of our delete `ControlEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_state', 'deleted_control_event_state_node_id', 'query', 'control_event_state_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventState')
    '''The `ControlEventState` that was deleted by this mutation.'''

    deleted_control_event_state_node_id = sgqlc.types.Field(ID, graphql_name='deletedControlEventStateNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_edge = sgqlc.types.Field(ControlEventStatesEdge, graphql_name='controlEventStateEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEventState`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class DeleteControllableComponentPayload(sgqlc.types.Type):
    '''The output of our delete `ControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'deleted_controllable_component_node_id', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''The `ControllableComponent` that was deleted by this mutation.'''

    deleted_controllable_component_node_id = sgqlc.types.Field(ID, graphql_name='deletedControllableComponentNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `ControllableComponent`.
    '''

    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    '''Reads a single `EdgeNode` that is related to this
    `ControllableComponent`.
    '''

    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControllableComponent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class DeleteEdgeNodePayload(sgqlc.types.Type):
    '''The output of our delete `EdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'deleted_edge_node_node_id', 'query', 'organization', 'facility', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    '''The `EdgeNode` that was deleted by this mutation.'''

    deleted_edge_node_node_id = sgqlc.types.Field(ID, graphql_name='deletedEdgeNodeNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `EdgeNode`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EdgeNode`.'''

    edge_node_edge = sgqlc.types.Field('EdgeNodesEdge', graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EdgeNode`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteEventProposalLogPayload(sgqlc.types.Type):
    '''The output of our delete `EventProposalLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_log', 'deleted_event_proposal_log_node_id', 'query', 'by_user', 'by_edge_node', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'event_proposal', 'event_proposal_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal_log = sgqlc.types.Field('EventProposalLog', graphql_name='eventProposalLog')
    '''The `EventProposalLog` that was deleted by this mutation.'''

    deleted_event_proposal_log_node_id = sgqlc.types.Field(ID, graphql_name='deletedEventProposalLogNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    '''Reads a single `User` that is related to this `EventProposalLog`.'''

    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalLog`.
    '''

    event_proposal_log_edge = sgqlc.types.Field('EventProposalLogsEdge', graphql_name='eventProposalLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposalLog`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteEventProposalMetricPayload(sgqlc.types.Type):
    '''The output of our delete `EventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_metric', 'deleted_event_proposal_metric_node_id', 'query', 'project_success_metric', 'controllable_component', 'event_proposal', 'event_proposal_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal_metric = sgqlc.types.Field('EventProposalMetric', graphql_name='eventProposalMetric')
    '''The `EventProposalMetric` that was deleted by this mutation.'''

    deleted_event_proposal_metric_node_id = sgqlc.types.Field(ID, graphql_name='deletedEventProposalMetricNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''Reads a single `ProjectSuccessMetric` that is related to this
    `EventProposalMetric`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal_metric_edge = sgqlc.types.Field('EventProposalMetricsEdge', graphql_name='eventProposalMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposalMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class DeleteEventProposalPayload(sgqlc.types.Type):
    '''The output of our delete `EventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'deleted_event_proposal_node_id', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''The `EventProposal` that was deleted by this mutation.'''

    deleted_event_proposal_node_id = sgqlc.types.Field(ID, graphql_name='deletedEventProposalNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field('EventProposalsEdge', graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteFacilityPayload(sgqlc.types.Type):
    '''The output of our delete `Facility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'deleted_facility_node_id', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''The `Facility` that was deleted by this mutation.'''

    deleted_facility_node_id = sgqlc.types.Field(ID, graphql_name='deletedFacilityNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Facility`.'''

    facility_edge = sgqlc.types.Field('FacilitiesEdge', graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Facility`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteFacilityUserPayload(sgqlc.types.Type):
    '''The output of our delete `FacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'deleted_facility_user_node_id', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    '''The `FacilityUser` that was deleted by this mutation.'''

    deleted_facility_user_node_id = sgqlc.types.Field(ID, graphql_name='deletedFacilityUserNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `FacilityUser`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `FacilityUser`.'''

    facility_user_edge = sgqlc.types.Field('FacilityUsersEdge', graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `FacilityUser`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteOrganizationPayload(sgqlc.types.Type):
    '''The output of our delete `Organization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'deleted_organization_node_id', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''The `Organization` that was deleted by this mutation.'''

    deleted_organization_node_id = sgqlc.types.Field(ID, graphql_name='deletedOrganizationNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization_edge = sgqlc.types.Field('OrganizationsEdge', graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Organization`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteProjectAgentPayload(sgqlc.types.Type):
    '''The output of our delete `ProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_agent', 'deleted_project_agent_node_id', 'query', 'project', 'user', 'project_agent_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_agent = sgqlc.types.Field('ProjectAgent', graphql_name='projectAgent')
    '''The `ProjectAgent` that was deleted by this mutation.'''

    deleted_project_agent_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectAgentNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `ProjectAgent`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `ProjectAgent`.'''

    project_agent_edge = sgqlc.types.Field('ProjectAgentsEdge', graphql_name='projectAgentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectAgent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteProjectPayload(sgqlc.types.Type):
    '''The output of our delete `Project` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'deleted_project_node_id', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''The `Project` that was deleted by this mutation.'''

    deleted_project_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Project`.'''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''Reads a single `ProjectType` that is related to this `Project`.'''

    project_edge = sgqlc.types.Field('ProjectsEdge', graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Project`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteProjectSuccessMetricPayload(sgqlc.types.Type):
    '''The output of our delete `ProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'deleted_project_success_metric_node_id', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''The `ProjectSuccessMetric` that was deleted by this mutation.'''

    deleted_project_success_metric_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectSuccessMetricNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `ProjectSuccessMetric`.
    '''

    project_success_metric_edge = sgqlc.types.Field('ProjectSuccessMetricsEdge', graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectSuccessMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class DeleteProjectTypePayload(sgqlc.types.Type):
    '''The output of our delete `ProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'deleted_project_type_node_id', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''The `ProjectType` that was deleted by this mutation.'''

    deleted_project_type_node_id = sgqlc.types.Field(ID, graphql_name='deletedProjectTypeNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_type_edge = sgqlc.types.Field('ProjectTypesEdge', graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectType`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectTypesOrderBy!]`): The method to use when
      ordering `ProjectType`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteStateDefinitionPayload(sgqlc.types.Type):
    '''The output of our delete `StateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_definition', 'deleted_state_definition_node_id', 'query', 'project', 'state_definition_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinition')
    '''The `StateDefinition` that was deleted by this mutation.'''

    deleted_state_definition_node_id = sgqlc.types.Field(ID, graphql_name='deletedStateDefinitionNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `StateDefinition`.
    '''

    state_definition_edge = sgqlc.types.Field('StateDefinitionsEdge', graphql_name='stateDefinitionEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateDefinition`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteStateMachinePayload(sgqlc.types.Type):
    '''The output of our delete `StateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_machine', 'deleted_state_machine_node_id', 'query', 'state_definition_by_state_definition', 'state_machine_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''The `StateMachine` that was deleted by this mutation.'''

    deleted_state_machine_node_id = sgqlc.types.Field(ID, graphql_name='deletedStateMachineNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    state_definition_by_state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `StateMachine`.
    '''

    state_machine_edge = sgqlc.types.Field('StateMachinesEdge', graphql_name='stateMachineEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateMachine`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class DeleteUserPayload(sgqlc.types.Type):
    '''The output of our delete `User` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'deleted_user_node_id', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''The `User` that was deleted by this mutation.'''

    deleted_user_node_id = sgqlc.types.Field(ID, graphql_name='deletedUserNodeId')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `User`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EdgeNodeControlEventStatesByControlEventLogByEdgeNodeIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEvent` values, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEvent')), graphql_name='nodes')
    '''A list of `ControlEvent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEvent`, info from the
    `ControlEventLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEvent` you could get from the
    connection.
    '''



class EdgeNodeControlEventsByControlEventLogByEdgeNodeIdAndControlEventIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEvent` edge in the connection, with data from
    `ControlEventLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_event_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEvent', graphql_name='node')
    '''The `ControlEvent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class EdgeNodeEventProposalsByEventProposalLogByEdgeNodeIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeEventProposalsByEventProposalLogByEdgeNodeIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class EdgeNodeEventProposalsByEventProposalLogByEdgeNodeIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_logs = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `ControllableComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `ControllableComponent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class EdgeNodeFacilitiesByControllableComponentControlledByEdgeNodeClientIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from
    `ControllableComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'controllable_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''



class EdgeNodeUsersByEventProposalLogByEdgeNodeIdAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodeUsersByEventProposalLogByEdgeNodeIdAndByUserIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class EdgeNodeUsersByEventProposalLogByEdgeNodeIdAndByUserIdManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

    event_proposal_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EdgeNodesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgeNodesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode` and cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class EdgeNodesEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''



class Edgecontrolevent(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('componentslug', 'controlevent')
    componentslug = sgqlc.types.Field(String, graphql_name='componentslug')

    controlevent = sgqlc.types.Field('ControlEvent', graphql_name='controlevent')



class EdgecontroleventsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Edgecontrolevent` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Edgecontrolevent)), graphql_name='nodes')
    '''A list of `Edgecontrolevent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EdgecontroleventsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Edgecontrolevent` and cursor
    to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Edgecontrolevent` you could get from the
    connection.
    '''



class EdgecontroleventsEdge(sgqlc.types.Type):
    '''A `Edgecontrolevent` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field(Edgecontrolevent, graphql_name='node')
    '''The `Edgecontrolevent` at the end of the edge.'''



class EventProposalControlEventStatesByControlEventEventProposalIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControlEventStatesByControlEventEventProposalIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EventProposalControlEventStatesByControlEventEventProposalIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class EventProposalControlEventStatesByEventProposalLogEventProposalIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControlEventStatesByEventProposalLogEventProposalIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EventProposalControlEventStatesByEventProposalLogEventProposalIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalControlEventStatesByEventProposalLogEventProposalIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControlEventStatesByEventProposalLogEventProposalIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class EventProposalControlEventStatesByEventProposalLogEventProposalIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalControllableComponentsByControlEventEventProposalIdAndControllableComponentIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControllableComponentsByControlEventEventProposalIdAndControllableComponentIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class EventProposalControllableComponentsByControlEventEventProposalIdAndControllableComponentIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class EventProposalControllableComponentsByEventProposalMetricEventProposalIdAndControllableComponentIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControllableComponentsByEventProposalMetricEventProposalIdAndControllableComponentIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `EventProposalMetric`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class EventProposalControllableComponentsByEventProposalMetricEventProposalIdAndControllableComponentIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null('EventProposalMetricsConnection'), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalControlledComponentsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalControlledComponentsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `EventProposalsControlledComponent`, and the cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class EventProposalControlledComponentsManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsControlledComponentsConnection'), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class EventProposalEdgeNodesByEventProposalLogEventProposalIdAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalEdgeNodesByEventProposalLogEventProposalIdAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class EventProposalEdgeNodesByEventProposalLogEventProposalIdAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

    event_proposal_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null('EventProposalLogsConnection'), graphql_name='eventProposalLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalLogsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposalLog` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposalLog')), graphql_name='nodes')
    '''A list of `EventProposalLog` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalLogsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposalLog` and cursor
    to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposalLog` you could get from the
    connection.
    '''



class EventProposalLogsEdge(sgqlc.types.Type):
    '''A `EventProposalLog` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposalLog', graphql_name='node')
    '''The `EventProposalLog` at the end of the edge.'''



class EventProposalMetricsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposalMetric` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposalMetric')), graphql_name='nodes')
    '''A list of `EventProposalMetric` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalMetricsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposalMetric` and
    cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposalMetric` you could get from the
    connection.
    '''



class EventProposalMetricsEdge(sgqlc.types.Type):
    '''A `EventProposalMetric` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposalMetric', graphql_name='node')
    '''The `EventProposalMetric` at the end of the edge.'''



class EventProposalProjectSuccessMetricsByEventProposalMetricEventProposalIdAndProjectSuccessMetricIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectSuccessMetric` values, with data
    from `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectSuccessMetric')), graphql_name='nodes')
    '''A list of `ProjectSuccessMetric` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalProjectSuccessMetricsByEventProposalMetricEventProposalIdAndProjectSuccessMetricIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectSuccessMetric`, info
    from the `EventProposalMetric`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectSuccessMetric` you could get from the
    connection.
    '''



class EventProposalProjectSuccessMetricsByEventProposalMetricEventProposalIdAndProjectSuccessMetricIdManyToManyEdge(sgqlc.types.Type):
    '''A `ProjectSuccessMetric` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='node')
    '''The `ProjectSuccessMetric` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalStateDefinitionsByEventProposalsControlledComponentEventProposalIdAndStateDefinitionManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateDefinition` values, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateDefinition')), graphql_name='nodes')
    '''A list of `StateDefinition` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalStateDefinitionsByEventProposalsControlledComponentEventProposalIdAndStateDefinitionManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateDefinition`, info from
    the `EventProposalsControlledComponent`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateDefinition` you could get from the
    connection.
    '''



class EventProposalStateDefinitionsByEventProposalsControlledComponentEventProposalIdAndStateDefinitionManyToManyEdge(sgqlc.types.Type):
    '''A `StateDefinition` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components_by_state_definition')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateDefinition', graphql_name='node')
    '''The `StateDefinition` at the end of the edge.'''

    event_proposals_controlled_components_by_state_definition = sgqlc.types.Field(sgqlc.types.non_null('EventProposalsControlledComponentsConnection'), graphql_name='eventProposalsControlledComponentsByStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class EventProposalStateMachinesByControlEventEventProposalIdAndStateMachineIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateMachine` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateMachine')), graphql_name='nodes')
    '''A list of `StateMachine` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalStateMachinesByControlEventEventProposalIdAndStateMachineIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateMachine`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateMachine` you could get from the
    connection.
    '''



class EventProposalStateMachinesByControlEventEventProposalIdAndStateMachineIdManyToManyEdge(sgqlc.types.Type):
    '''A `StateMachine` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateMachine', graphql_name='node')
    '''The `StateMachine` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class EventProposalUsersByEventProposalLogEventProposalIdAndByUserIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalUsersByEventProposalLogEventProposalIdAndByUserIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class EventProposalUsersByEventProposalLogEventProposalIdAndByUserIdManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_user_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

    event_proposal_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class EventProposalsControlledComponent(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('event_proposal_id', 'controllable_component_id', 'created_at', 'updated_at', 'state_definition', 'event_proposal', 'controllable_component', 'state_definition_by_state_definition')
    event_proposal_id = sgqlc.types.Field(UUID, graphql_name='eventProposalId')
    '''E'@manyToManyFieldName controlEvents' '''

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    '''E'@manyToManyFieldName controlledComponents' '''

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    state_definition = sgqlc.types.Field(String, graphql_name='stateDefinition')

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalsControlledComponent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalsControlledComponent`.
    '''

    state_definition_by_state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `EventProposalsControlledComponent`.
    '''



class EventProposalsControlledComponentsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposalsControlledComponent`
    values.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(EventProposalsControlledComponent)), graphql_name='nodes')
    '''A list of `EventProposalsControlledComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventProposalsControlledComponentsEdge'))), graphql_name='edges')
    '''A list of edges which contains the
    `EventProposalsControlledComponent` and cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposalsControlledComponent` you could
    get from the connection.
    '''



class EventProposalsControlledComponentsEdge(sgqlc.types.Type):
    '''A `EventProposalsControlledComponent` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field(EventProposalsControlledComponent, graphql_name='node')
    '''The `EventProposalsControlledComponent` at the end of the edge.'''



class EventProposalsEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''



class FacilitiesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilitiesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility` and cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class FacilitiesEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''



class FacilityControlEventStatesByEventProposalFacilityIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityControlEventStatesByEventProposalFacilityIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class FacilityControlEventStatesByEventProposalFacilityIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposals_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposalsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `ControllableComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `ControllableComponent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class FacilityEdgeNodesByControllableComponentFacilityIdAndControlledByEdgeNodeClientIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `ControllableComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'controllable_components_by_controlled_by_edge_node_client_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''



class FacilityOrganizationsByEdgeNodeFacilityIdAndOrganizationIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Organization` values, with data from
    `EdgeNode`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    '''A list of `Organization` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityOrganizationsByEdgeNodeFacilityIdAndOrganizationIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Organization`, info from the
    `EdgeNode`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Organization` you could get from the
    connection.
    '''



class FacilityOrganizationsByEdgeNodeFacilityIdAndOrganizationIdManyToManyEdge(sgqlc.types.Type):
    '''A `Organization` edge in the connection, with data from
    `EdgeNode`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'edge_nodes')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Organization', graphql_name='node')
    '''The `Organization` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class FacilityProject(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('facility_id', 'project_id', 'created_at', 'updated_at', 'enrollment_status', 'auto_approve', 'facility', 'project')
    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')
    '''E'@manyToManyFieldName facilities' '''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    '''E'@manyToManyFieldName projects' '''

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    enrollment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='enrollmentStatus')

    auto_approve = sgqlc.types.Field(Boolean, graphql_name='autoApprove')
    '''If enabled, this project at this particular facility will skip the
    approval process
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `FacilityProject`.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `FacilityProject`.
    '''



class FacilityProjectsByEventProposalFacilityIdAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Project` values, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    '''A list of `Project` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsByEventProposalFacilityIdAndProjectIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Project`, info from the
    `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Project` you could get from the connection.'''



class FacilityProjectsByEventProposalFacilityIdAndProjectIdManyToManyEdge(sgqlc.types.Type):
    '''A `Project` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Project', graphql_name='node')
    '''The `Project` at the end of the edge.'''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Project` values, with data from
    `FacilityProject`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    '''A list of `Project` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Project`, info from the
    `FacilityProject`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Project` you could get from the connection.'''



class FacilityProjectsByFacilityProjectFacilityIdAndProjectIdManyToManyEdge(sgqlc.types.Type):
    '''A `Project` edge in the connection, with data from
    `FacilityProject`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Project', graphql_name='node')
    '''The `Project` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `FacilityProject`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    * `condition` (`FacilityProjectCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class FacilityProjectsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `FacilityProject` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FacilityProject)), graphql_name='nodes')
    '''A list of `FacilityProject` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityProjectsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `FacilityProject` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `FacilityProject` you could get from the
    connection.
    '''



class FacilityProjectsEdge(sgqlc.types.Type):
    '''A `FacilityProject` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field(FacilityProject, graphql_name='node')
    '''The `FacilityProject` at the end of the edge.'''



class FacilityUsersConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `FacilityUser` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FacilityUser')), graphql_name='nodes')
    '''A list of `FacilityUser` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityUsersEdge'))), graphql_name='edges')
    '''A list of edges which contains the `FacilityUser` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `FacilityUser` you could get from the
    connection.
    '''



class FacilityUsersEdge(sgqlc.types.Type):
    '''A `FacilityUser` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('FacilityUser', graphql_name='node')
    '''The `FacilityUser` at the end of the edge.'''



class FacilityUsersManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `FacilityUser`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FacilityUsersManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `FacilityUser`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class FacilityUsersManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from `FacilityUser`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_users')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `FacilityUser`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityUserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class Mutation(sgqlc.types.Type):
    '''The root mutation type which contains root level fields which
    mutate data.
    '''
    __schema__ = control_schema
    __field_names__ = ('create_control_event', 'create_controllable_component', 'create_edge_node', 'create_event_proposal_metric', 'create_event_proposal', 'create_event_proposals_controlled_component', 'create_facility', 'create_facility_project', 'create_facility_user', 'create_organization', 'create_project_agent', 'create_project_success_metric', 'create_project_type', 'create_project', 'create_state_definition', 'create_state_machine', 'create_user', 'update_control_event_log_by_node_id', 'update_control_event_log', 'update_control_event_state_by_node_id', 'update_control_event_state', 'update_control_event_by_node_id', 'update_control_event', 'update_controllable_component_by_node_id', 'update_controllable_component', 'update_controllable_component_by_slug_and_facility_id', 'update_edge_node_by_node_id', 'update_edge_node', 'update_event_proposal_log_by_node_id', 'update_event_proposal_log', 'update_event_proposal_metric_by_node_id', 'update_event_proposal_metric', 'update_event_proposal_by_node_id', 'update_event_proposal', 'update_facility_by_node_id', 'update_facility', 'update_facility_user_by_node_id', 'update_facility_user', 'update_organization_by_node_id', 'update_organization', 'update_project_agent_by_node_id', 'update_project_agent', 'update_project_success_metric_by_node_id', 'update_project_success_metric', 'update_project_type_by_node_id', 'update_project_type', 'update_project_by_node_id', 'update_project', 'update_state_definition_by_node_id', 'update_state_definition', 'update_state_machine_by_node_id', 'update_state_machine', 'update_user_by_node_id', 'update_user', 'delete_control_event_log_by_node_id', 'delete_control_event_log', 'delete_control_event_state_by_node_id', 'delete_control_event_state', 'delete_control_event_by_node_id', 'delete_control_event', 'delete_controllable_component_by_node_id', 'delete_controllable_component', 'delete_controllable_component_by_slug_and_facility_id', 'delete_edge_node_by_node_id', 'delete_edge_node', 'delete_event_proposal_log_by_node_id', 'delete_event_proposal_log', 'delete_event_proposal_metric_by_node_id', 'delete_event_proposal_metric', 'delete_event_proposal_by_node_id', 'delete_event_proposal', 'delete_facility_by_node_id', 'delete_facility', 'delete_facility_user_by_node_id', 'delete_facility_user', 'delete_organization_by_node_id', 'delete_organization', 'delete_project_agent_by_node_id', 'delete_project_agent', 'delete_project_success_metric_by_node_id', 'delete_project_success_metric', 'delete_project_type_by_node_id', 'delete_project_type', 'delete_project_by_node_id', 'delete_project', 'delete_state_definition_by_node_id', 'delete_state_definition', 'delete_state_machine_by_node_id', 'delete_state_machine', 'delete_user_by_node_id', 'delete_user', 'add_historic_event', 'approve_proposal', 'approve_proposal_review', 'change_event_state', 'change_proposal_state', 'propose_event', 'set_control_events', 'transition_control_event')
    create_control_event = sgqlc.types.Field(CreateControlEventPayload, graphql_name='createControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControlEventInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `ControlEvent`.

    Arguments:

    * `input` (`CreateControlEventInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_controllable_component = sgqlc.types.Field(CreateControllableComponentPayload, graphql_name='createControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateControllableComponentInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `ControllableComponent`.

    Arguments:

    * `input` (`CreateControllableComponentInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    create_edge_node = sgqlc.types.Field(CreateEdgeNodePayload, graphql_name='createEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `EdgeNode`.

    Arguments:

    * `input` (`CreateEdgeNodeInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_event_proposal_metric = sgqlc.types.Field(CreateEventProposalMetricPayload, graphql_name='createEventProposalMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventProposalMetricInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `EventProposalMetric`.

    Arguments:

    * `input` (`CreateEventProposalMetricInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_event_proposal = sgqlc.types.Field(CreateEventProposalPayload, graphql_name='createEventProposal', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventProposalInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `EventProposal`.

    Arguments:

    * `input` (`CreateEventProposalInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_event_proposals_controlled_component = sgqlc.types.Field(CreateEventProposalsControlledComponentPayload, graphql_name='createEventProposalsControlledComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventProposalsControlledComponentInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `EventProposalsControlledComponent`.

    Arguments:

    * `input` (`CreateEventProposalsControlledComponentInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    create_facility = sgqlc.types.Field(CreateFacilityPayload, graphql_name='createFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `Facility`.

    Arguments:

    * `input` (`CreateFacilityInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_facility_project = sgqlc.types.Field(CreateFacilityProjectPayload, graphql_name='createFacilityProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityProjectInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `FacilityProject`.

    Arguments:

    * `input` (`CreateFacilityProjectInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_facility_user = sgqlc.types.Field(CreateFacilityUserPayload, graphql_name='createFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFacilityUserInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `FacilityUser`.

    Arguments:

    * `input` (`CreateFacilityUserInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_organization = sgqlc.types.Field(CreateOrganizationPayload, graphql_name='createOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrganizationInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `Organization`.

    Arguments:

    * `input` (`CreateOrganizationInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_project_agent = sgqlc.types.Field(CreateProjectAgentPayload, graphql_name='createProjectAgent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectAgentInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `ProjectAgent`.

    Arguments:

    * `input` (`CreateProjectAgentInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_project_success_metric = sgqlc.types.Field(CreateProjectSuccessMetricPayload, graphql_name='createProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `ProjectSuccessMetric`.

    Arguments:

    * `input` (`CreateProjectSuccessMetricInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    create_project_type = sgqlc.types.Field(CreateProjectTypePayload, graphql_name='createProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectTypeInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `ProjectType`.

    Arguments:

    * `input` (`CreateProjectTypeInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_project = sgqlc.types.Field(CreateProjectPayload, graphql_name='createProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `Project`.

    Arguments:

    * `input` (`CreateProjectInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_state_definition = sgqlc.types.Field(CreateStateDefinitionPayload, graphql_name='createStateDefinition', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateStateDefinitionInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `StateDefinition`.

    Arguments:

    * `input` (`CreateStateDefinitionInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_state_machine = sgqlc.types.Field(CreateStateMachinePayload, graphql_name='createStateMachine', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateStateMachineInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `StateMachine`.

    Arguments:

    * `input` (`CreateStateMachineInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    create_user = sgqlc.types.Field(CreateUserPayload, graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    '''Creates a single `User`.

    Arguments:

    * `input` (`CreateUserInput!`): The exclusive input argument for
      this mutation. An object type, make sure to see documentation
      for this object’s fields.
    '''

    update_control_event_log_by_node_id = sgqlc.types.Field('UpdateControlEventLogPayload', graphql_name='updateControlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEventLog` using its globally unique id
    and a patch.

    Arguments:

    * `input` (`UpdateControlEventLogByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_control_event_log = sgqlc.types.Field('UpdateControlEventLogPayload', graphql_name='updateControlEventLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventLogInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEventLog` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateControlEventLogInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_control_event_state_by_node_id = sgqlc.types.Field('UpdateControlEventStatePayload', graphql_name='updateControlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventStateByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEventState` using its globally unique id
    and a patch.

    Arguments:

    * `input` (`UpdateControlEventStateByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_control_event_state = sgqlc.types.Field('UpdateControlEventStatePayload', graphql_name='updateControlEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventStateInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEventState` using a unique key and a
    patch.

    Arguments:

    * `input` (`UpdateControlEventStateInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_control_event_by_node_id = sgqlc.types.Field('UpdateControlEventPayload', graphql_name='updateControlEventByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEvent` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateControlEventByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_control_event = sgqlc.types.Field('UpdateControlEventPayload', graphql_name='updateControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControlEventInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControlEvent` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateControlEventInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_controllable_component_by_node_id = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControllableComponent` using its globally unique
    id and a patch.

    Arguments:

    * `input` (`UpdateControllableComponentByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    update_controllable_component = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControllableComponent` using a unique key and a
    patch.

    Arguments:

    * `input` (`UpdateControllableComponentInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_controllable_component_by_slug_and_facility_id = sgqlc.types.Field('UpdateControllableComponentPayload', graphql_name='updateControllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateControllableComponentBySlugAndFacilityIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ControllableComponent` using a unique key and a
    patch.

    Arguments:

    * `input`
      (`UpdateControllableComponentBySlugAndFacilityIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    update_edge_node_by_node_id = sgqlc.types.Field('UpdateEdgeNodePayload', graphql_name='updateEdgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEdgeNodeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EdgeNode` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateEdgeNodeByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_edge_node = sgqlc.types.Field('UpdateEdgeNodePayload', graphql_name='updateEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EdgeNode` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateEdgeNodeInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_event_proposal_log_by_node_id = sgqlc.types.Field('UpdateEventProposalLogPayload', graphql_name='updateEventProposalLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposalLog` using its globally unique id
    and a patch.

    Arguments:

    * `input` (`UpdateEventProposalLogByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_event_proposal_log = sgqlc.types.Field('UpdateEventProposalLogPayload', graphql_name='updateEventProposalLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalLogInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposalLog` using a unique key and a
    patch.

    Arguments:

    * `input` (`UpdateEventProposalLogInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_event_proposal_metric_by_node_id = sgqlc.types.Field('UpdateEventProposalMetricPayload', graphql_name='updateEventProposalMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposalMetric` using its globally unique
    id and a patch.

    Arguments:

    * `input` (`UpdateEventProposalMetricByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    update_event_proposal_metric = sgqlc.types.Field('UpdateEventProposalMetricPayload', graphql_name='updateEventProposalMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalMetricInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposalMetric` using a unique key and a
    patch.

    Arguments:

    * `input` (`UpdateEventProposalMetricInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_event_proposal_by_node_id = sgqlc.types.Field('UpdateEventProposalPayload', graphql_name='updateEventProposalByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposal` using its globally unique id and
    a patch.

    Arguments:

    * `input` (`UpdateEventProposalByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_event_proposal = sgqlc.types.Field('UpdateEventProposalPayload', graphql_name='updateEventProposal', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventProposalInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `EventProposal` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateEventProposalInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_facility_by_node_id = sgqlc.types.Field('UpdateFacilityPayload', graphql_name='updateFacilityByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Facility` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateFacilityByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_facility = sgqlc.types.Field('UpdateFacilityPayload', graphql_name='updateFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Facility` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateFacilityInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_facility_user_by_node_id = sgqlc.types.Field('UpdateFacilityUserPayload', graphql_name='updateFacilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `FacilityUser` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateFacilityUserByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_facility_user = sgqlc.types.Field('UpdateFacilityUserPayload', graphql_name='updateFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFacilityUserInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `FacilityUser` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateFacilityUserInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_organization_by_node_id = sgqlc.types.Field('UpdateOrganizationPayload', graphql_name='updateOrganizationByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Organization` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateOrganizationByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_organization = sgqlc.types.Field('UpdateOrganizationPayload', graphql_name='updateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Organization` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateOrganizationInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_project_agent_by_node_id = sgqlc.types.Field('UpdateProjectAgentPayload', graphql_name='updateProjectAgentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectAgentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectAgent` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateProjectAgentByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_project_agent = sgqlc.types.Field('UpdateProjectAgentPayload', graphql_name='updateProjectAgent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectAgentInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectAgent` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateProjectAgentInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_project_success_metric_by_node_id = sgqlc.types.Field('UpdateProjectSuccessMetricPayload', graphql_name='updateProjectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectSuccessMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectSuccessMetric` using its globally unique
    id and a patch.

    Arguments:

    * `input` (`UpdateProjectSuccessMetricByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    update_project_success_metric = sgqlc.types.Field('UpdateProjectSuccessMetricPayload', graphql_name='updateProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectSuccessMetric` using a unique key and a
    patch.

    Arguments:

    * `input` (`UpdateProjectSuccessMetricInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_project_type_by_node_id = sgqlc.types.Field('UpdateProjectTypePayload', graphql_name='updateProjectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectTypeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectType` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateProjectTypeByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_project_type = sgqlc.types.Field('UpdateProjectTypePayload', graphql_name='updateProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectTypeInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `ProjectType` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateProjectTypeInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_project_by_node_id = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProjectByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Project` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateProjectByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_project = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `Project` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateProjectInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_state_definition_by_node_id = sgqlc.types.Field('UpdateStateDefinitionPayload', graphql_name='updateStateDefinitionByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateStateDefinitionByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `StateDefinition` using its globally unique id
    and a patch.

    Arguments:

    * `input` (`UpdateStateDefinitionByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_state_definition = sgqlc.types.Field('UpdateStateDefinitionPayload', graphql_name='updateStateDefinition', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateStateDefinitionInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `StateDefinition` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateStateDefinitionInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_state_machine_by_node_id = sgqlc.types.Field('UpdateStateMachinePayload', graphql_name='updateStateMachineByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateStateMachineByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `StateMachine` using its globally unique id and a
    patch.

    Arguments:

    * `input` (`UpdateStateMachineByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    update_state_machine = sgqlc.types.Field('UpdateStateMachinePayload', graphql_name='updateStateMachine', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateStateMachineInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `StateMachine` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateStateMachineInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_user_by_node_id = sgqlc.types.Field('UpdateUserPayload', graphql_name='updateUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `User` using its globally unique id and a patch.

    Arguments:

    * `input` (`UpdateUserByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    update_user = sgqlc.types.Field('UpdateUserPayload', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    '''Updates a single `User` using a unique key and a patch.

    Arguments:

    * `input` (`UpdateUserInput!`): The exclusive input argument for
      this mutation. An object type, make sure to see documentation
      for this object’s fields.
    '''

    delete_control_event_log_by_node_id = sgqlc.types.Field(DeleteControlEventLogPayload, graphql_name='deleteControlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEventLog` using its globally unique id.

    Arguments:

    * `input` (`DeleteControlEventLogByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_control_event_log = sgqlc.types.Field(DeleteControlEventLogPayload, graphql_name='deleteControlEventLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventLogInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEventLog` using a unique key.

    Arguments:

    * `input` (`DeleteControlEventLogInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_control_event_state_by_node_id = sgqlc.types.Field(DeleteControlEventStatePayload, graphql_name='deleteControlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventStateByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEventState` using its globally unique id.

    Arguments:

    * `input` (`DeleteControlEventStateByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_control_event_state = sgqlc.types.Field(DeleteControlEventStatePayload, graphql_name='deleteControlEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventStateInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEventState` using a unique key.

    Arguments:

    * `input` (`DeleteControlEventStateInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_control_event_by_node_id = sgqlc.types.Field(DeleteControlEventPayload, graphql_name='deleteControlEventByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEvent` using its globally unique id.

    Arguments:

    * `input` (`DeleteControlEventByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_control_event = sgqlc.types.Field(DeleteControlEventPayload, graphql_name='deleteControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControlEventInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControlEvent` using a unique key.

    Arguments:

    * `input` (`DeleteControlEventInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_controllable_component_by_node_id = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControllableComponent` using its globally unique
    id.

    Arguments:

    * `input` (`DeleteControllableComponentByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    delete_controllable_component = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControllableComponent` using a unique key.

    Arguments:

    * `input` (`DeleteControllableComponentInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_controllable_component_by_slug_and_facility_id = sgqlc.types.Field(DeleteControllableComponentPayload, graphql_name='deleteControllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteControllableComponentBySlugAndFacilityIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ControllableComponent` using a unique key.

    Arguments:

    * `input`
      (`DeleteControllableComponentBySlugAndFacilityIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    delete_edge_node_by_node_id = sgqlc.types.Field(DeleteEdgeNodePayload, graphql_name='deleteEdgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEdgeNodeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EdgeNode` using its globally unique id.

    Arguments:

    * `input` (`DeleteEdgeNodeByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_edge_node = sgqlc.types.Field(DeleteEdgeNodePayload, graphql_name='deleteEdgeNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEdgeNodeInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EdgeNode` using a unique key.

    Arguments:

    * `input` (`DeleteEdgeNodeInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_event_proposal_log_by_node_id = sgqlc.types.Field(DeleteEventProposalLogPayload, graphql_name='deleteEventProposalLogByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalLogByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposalLog` using its globally unique id.

    Arguments:

    * `input` (`DeleteEventProposalLogByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_event_proposal_log = sgqlc.types.Field(DeleteEventProposalLogPayload, graphql_name='deleteEventProposalLog', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalLogInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposalLog` using a unique key.

    Arguments:

    * `input` (`DeleteEventProposalLogInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_event_proposal_metric_by_node_id = sgqlc.types.Field(DeleteEventProposalMetricPayload, graphql_name='deleteEventProposalMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposalMetric` using its globally unique
    id.

    Arguments:

    * `input` (`DeleteEventProposalMetricByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    delete_event_proposal_metric = sgqlc.types.Field(DeleteEventProposalMetricPayload, graphql_name='deleteEventProposalMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalMetricInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposalMetric` using a unique key.

    Arguments:

    * `input` (`DeleteEventProposalMetricInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_event_proposal_by_node_id = sgqlc.types.Field(DeleteEventProposalPayload, graphql_name='deleteEventProposalByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposal` using its globally unique id.

    Arguments:

    * `input` (`DeleteEventProposalByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_event_proposal = sgqlc.types.Field(DeleteEventProposalPayload, graphql_name='deleteEventProposal', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventProposalInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `EventProposal` using a unique key.

    Arguments:

    * `input` (`DeleteEventProposalInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_facility_by_node_id = sgqlc.types.Field(DeleteFacilityPayload, graphql_name='deleteFacilityByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Facility` using its globally unique id.

    Arguments:

    * `input` (`DeleteFacilityByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_facility = sgqlc.types.Field(DeleteFacilityPayload, graphql_name='deleteFacility', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Facility` using a unique key.

    Arguments:

    * `input` (`DeleteFacilityInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_facility_user_by_node_id = sgqlc.types.Field(DeleteFacilityUserPayload, graphql_name='deleteFacilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `FacilityUser` using its globally unique id.

    Arguments:

    * `input` (`DeleteFacilityUserByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_facility_user = sgqlc.types.Field(DeleteFacilityUserPayload, graphql_name='deleteFacilityUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteFacilityUserInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `FacilityUser` using a unique key.

    Arguments:

    * `input` (`DeleteFacilityUserInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_organization_by_node_id = sgqlc.types.Field(DeleteOrganizationPayload, graphql_name='deleteOrganizationByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizationByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Organization` using its globally unique id.

    Arguments:

    * `input` (`DeleteOrganizationByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_organization = sgqlc.types.Field(DeleteOrganizationPayload, graphql_name='deleteOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizationInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Organization` using a unique key.

    Arguments:

    * `input` (`DeleteOrganizationInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_project_agent_by_node_id = sgqlc.types.Field(DeleteProjectAgentPayload, graphql_name='deleteProjectAgentByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectAgentByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectAgent` using its globally unique id.

    Arguments:

    * `input` (`DeleteProjectAgentByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_project_agent = sgqlc.types.Field(DeleteProjectAgentPayload, graphql_name='deleteProjectAgent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectAgentInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectAgent` using a unique key.

    Arguments:

    * `input` (`DeleteProjectAgentInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_project_success_metric_by_node_id = sgqlc.types.Field(DeleteProjectSuccessMetricPayload, graphql_name='deleteProjectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectSuccessMetricByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectSuccessMetric` using its globally unique
    id.

    Arguments:

    * `input` (`DeleteProjectSuccessMetricByNodeIdInput!`): The
      exclusive input argument for this mutation. An object type, make
      sure to see documentation for this object’s fields.
    '''

    delete_project_success_metric = sgqlc.types.Field(DeleteProjectSuccessMetricPayload, graphql_name='deleteProjectSuccessMetric', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectSuccessMetricInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectSuccessMetric` using a unique key.

    Arguments:

    * `input` (`DeleteProjectSuccessMetricInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_project_type_by_node_id = sgqlc.types.Field(DeleteProjectTypePayload, graphql_name='deleteProjectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectTypeByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectType` using its globally unique id.

    Arguments:

    * `input` (`DeleteProjectTypeByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_project_type = sgqlc.types.Field(DeleteProjectTypePayload, graphql_name='deleteProjectType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectTypeInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `ProjectType` using a unique key.

    Arguments:

    * `input` (`DeleteProjectTypeInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_project_by_node_id = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProjectByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Project` using its globally unique id.

    Arguments:

    * `input` (`DeleteProjectByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_project = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `Project` using a unique key.

    Arguments:

    * `input` (`DeleteProjectInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_state_definition_by_node_id = sgqlc.types.Field(DeleteStateDefinitionPayload, graphql_name='deleteStateDefinitionByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteStateDefinitionByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `StateDefinition` using its globally unique id.

    Arguments:

    * `input` (`DeleteStateDefinitionByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_state_definition = sgqlc.types.Field(DeleteStateDefinitionPayload, graphql_name='deleteStateDefinition', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteStateDefinitionInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `StateDefinition` using a unique key.

    Arguments:

    * `input` (`DeleteStateDefinitionInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_state_machine_by_node_id = sgqlc.types.Field(DeleteStateMachinePayload, graphql_name='deleteStateMachineByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteStateMachineByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `StateMachine` using its globally unique id.

    Arguments:

    * `input` (`DeleteStateMachineByNodeIdInput!`): The exclusive
      input argument for this mutation. An object type, make sure to
      see documentation for this object’s fields.
    '''

    delete_state_machine = sgqlc.types.Field(DeleteStateMachinePayload, graphql_name='deleteStateMachine', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteStateMachineInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `StateMachine` using a unique key.

    Arguments:

    * `input` (`DeleteStateMachineInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_user_by_node_id = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUserByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserByNodeIdInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `User` using its globally unique id.

    Arguments:

    * `input` (`DeleteUserByNodeIdInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    delete_user = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserInput), graphql_name='input', default=None)),
))
    )
    '''Deletes a single `User` using a unique key.

    Arguments:

    * `input` (`DeleteUserInput!`): The exclusive input argument for
      this mutation. An object type, make sure to see documentation
      for this object’s fields.
    '''

    add_historic_event = sgqlc.types.Field(AddHistoricEventPayload, graphql_name='addHistoricEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddHistoricEventInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`AddHistoricEventInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    approve_proposal = sgqlc.types.Field(ApproveProposalPayload, graphql_name='approveProposal', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveProposalInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`ApproveProposalInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    approve_proposal_review = sgqlc.types.Field(ApproveProposalReviewPayload, graphql_name='approveProposalReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveProposalReviewInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`ApproveProposalReviewInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    change_event_state = sgqlc.types.Field(ChangeEventStatePayload, graphql_name='changeEventState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeEventStateInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`ChangeEventStateInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    change_proposal_state = sgqlc.types.Field(ChangeProposalStatePayload, graphql_name='changeProposalState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeProposalStateInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`ChangeProposalStateInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    propose_event = sgqlc.types.Field('ProposeEventPayload', graphql_name='proposeEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProposeEventInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`ProposeEventInput!`): The exclusive input argument for
      this mutation. An object type, make sure to see documentation
      for this object’s fields.
    '''

    set_control_events = sgqlc.types.Field('SetControlEventsPayload', graphql_name='setControlEvents', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetControlEventsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`SetControlEventsInput!`): The exclusive input argument
      for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''

    transition_control_event = sgqlc.types.Field('TransitionControlEventPayload', graphql_name='transitionControlEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TransitionControlEventInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`TransitionControlEventInput!`): The exclusive input
      argument for this mutation. An object type, make sure to see
      documentation for this object’s fields.
    '''



class Node(sgqlc.types.Interface):
    '''An object with a globally unique `ID`.'''
    __schema__ = control_schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    '''A globally unique identifier. Can be used in various places
    throughout the system to identify this single value.
    '''



class OrganizationFacilitiesByEdgeNodeOrganizationIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `EdgeNode`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationFacilitiesByEdgeNodeOrganizationIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `EdgeNode`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class OrganizationFacilitiesByEdgeNodeOrganizationIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from `EdgeNode`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'edge_nodes')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectType` values, with data from
    `Project`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectType')), graphql_name='nodes')
    '''A list of `ProjectType` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectType`, info from the
    `Project`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectType` you could get from the
    connection.
    '''



class OrganizationProjectTypesByProjectOrganizationIdAndProjectTypeIdManyToManyEdge(sgqlc.types.Type):
    '''A `ProjectType` edge in the connection, with data from `Project`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectType', graphql_name='node')
    '''The `ProjectType` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class OrganizationsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Organization` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    '''A list of `Organization` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Organization` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Organization` you could get from the
    connection.
    '''



class OrganizationsEdge(sgqlc.types.Type):
    '''A `Organization` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Organization', graphql_name='node')
    '''The `Organization` at the end of the edge.'''



class PageInfo(sgqlc.types.Type):
    '''Information about pagination in a connection.'''
    __schema__ = control_schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    '''When paginating forwards, are there more items?'''

    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    '''When paginating backwards, are there more items?'''

    start_cursor = sgqlc.types.Field(Cursor, graphql_name='startCursor')
    '''When paginating backwards, the cursor to continue.'''

    end_cursor = sgqlc.types.Field(Cursor, graphql_name='endCursor')
    '''When paginating forwards, the cursor to continue.'''



class ProjectAgentsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectAgent` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectAgent')), graphql_name='nodes')
    '''A list of `ProjectAgent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectAgentsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectAgent` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectAgent` you could get from the
    connection.
    '''



class ProjectAgentsEdge(sgqlc.types.Type):
    '''A `ProjectAgent` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectAgent', graphql_name='node')
    '''The `ProjectAgent` at the end of the edge.'''



class ProjectAgentsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values, with data from
    `ProjectAgent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectAgentsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User`, info from the
    `ProjectAgent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class ProjectAgentsManyToManyEdge(sgqlc.types.Type):
    '''A `User` edge in the connection, with data from `ProjectAgent`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'project_agents')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''

    project_agents = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentsConnection), graphql_name='projectAgents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectAgentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ProjectAgent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectAgentCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ProjectControlEventStatesByEventProposalProjectIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectControlEventStatesByEventProposalProjectIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class ProjectControlEventStatesByEventProposalProjectIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposals_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposalsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ProjectFacilitiesByEventProposalProjectIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFacilitiesByEventProposalProjectIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `EventProposal`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class ProjectFacilitiesByEventProposalProjectIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from
    `EventProposal`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `FacilityProject`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `FacilityProject`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class ProjectFacilitiesByFacilityProjectProjectIdAndFacilityIdManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from
    `FacilityProject`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `FacilityProject`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    * `condition` (`FacilityProjectCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class ProjectSuccessMetricControllableComponentsByEventProposalMetricProjectSuccessMetricIdAndControllableComponentIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSuccessMetricControllableComponentsByEventProposalMetricProjectSuccessMetricIdAndControllableComponentIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `EventProposalMetric`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class ProjectSuccessMetricControllableComponentsByEventProposalMetricProjectSuccessMetricIdAndControllableComponentIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ProjectSuccessMetricEventProposalsByEventProposalMetricProjectSuccessMetricIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSuccessMetricEventProposalsByEventProposalMetricProjectSuccessMetricIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalMetric`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class ProjectSuccessMetricEventProposalsByEventProposalMetricProjectSuccessMetricIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalMetric`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_metrics')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ProjectSuccessMetricsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectSuccessMetric` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectSuccessMetric')), graphql_name='nodes')
    '''A list of `ProjectSuccessMetric` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSuccessMetricsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectSuccessMetric` and
    cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectSuccessMetric` you could get from the
    connection.
    '''



class ProjectSuccessMetricsEdge(sgqlc.types.Type):
    '''A `ProjectSuccessMetric` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='node')
    '''The `ProjectSuccessMetric` at the end of the edge.'''



class ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Organization` values, with data from
    `Project`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Organization')), graphql_name='nodes')
    '''A list of `Organization` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Organization`, info from the
    `Project`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Organization` you could get from the
    connection.
    '''



class ProjectTypeOrganizationsByProjectProjectTypeIdAndOrganizationIdManyToManyEdge(sgqlc.types.Type):
    '''A `Organization` edge in the connection, with data from `Project`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'projects')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Organization', graphql_name='node')
    '''The `Organization` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class ProjectTypesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ProjectType` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProjectType')), graphql_name='nodes')
    '''A list of `ProjectType` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectTypesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ProjectType` and cursor to aid
    in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ProjectType` you could get from the
    connection.
    '''



class ProjectTypesEdge(sgqlc.types.Type):
    '''A `ProjectType` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ProjectType', graphql_name='node')
    '''The `ProjectType` at the end of the edge.'''



class Projectenrollmentstatus(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('enrollment_status', 'facility_id', 'facility_name', 'organization_id')
    enrollment_status = sgqlc.types.Field(String, graphql_name='enrollmentStatus')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    facility_name = sgqlc.types.Field(String, graphql_name='facilityName')

    organization_id = sgqlc.types.Field(UUID, graphql_name='organizationId')



class ProjectenrollmentstatusesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Projectenrollmentstatus` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Projectenrollmentstatus)), graphql_name='nodes')
    '''A list of `Projectenrollmentstatus` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectenrollmentstatusesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Projectenrollmentstatus` and
    cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Projectenrollmentstatus` you could get from
    the connection.
    '''



class ProjectenrollmentstatusesEdge(sgqlc.types.Type):
    '''A `Projectenrollmentstatus` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field(Projectenrollmentstatus, graphql_name='node')
    '''The `Projectenrollmentstatus` at the end of the edge.'''



class ProjectsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Project` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    '''A list of `Project` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Project` and cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Project` you could get from the connection.'''



class ProjectsEdge(sgqlc.types.Type):
    '''A `Project` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Project', graphql_name='node')
    '''The `Project` at the end of the edge.'''



class ProposeEventPayload(sgqlc.types.Type):
    '''The output of our `proposeEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field(EventProposalsEdge, graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class SetControlEventsPayload(sgqlc.types.Type):
    '''The output of our `setControlEvents` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'boolean', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    boolean = sgqlc.types.Field(Boolean, graphql_name='boolean')

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''



class StateDefinitionControlledComponentsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateDefinitionControlledComponentsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `EventProposalsControlledComponent`, and the cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class StateDefinitionControlledComponentsManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsControlledComponentsConnection), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class StateDefinitionEventProposalsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateDefinitionEventProposalsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalsControlledComponent`, and the cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class StateDefinitionEventProposalsManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalsControlledComponent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposals_controlled_components')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsControlledComponentsConnection), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''



class StateDefinitionsConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateDefinition` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateDefinition')), graphql_name='nodes')
    '''A list of `StateDefinition` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateDefinitionsEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateDefinition` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateDefinition` you could get from the
    connection.
    '''



class StateDefinitionsEdge(sgqlc.types.Type):
    '''A `StateDefinition` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateDefinition', graphql_name='node')
    '''The `StateDefinition` at the end of the edge.'''



class StateMachineControlEventStatesByControlEventStateMachineIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateMachineControlEventStatesByControlEventStateMachineIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class StateMachineControlEventStatesByControlEventStateMachineIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class StateMachineControllableComponentsByControlEventStateMachineIdAndControllableComponentIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControllableComponent` values, with
    data from `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControllableComponent')), graphql_name='nodes')
    '''A list of `ControllableComponent` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateMachineControllableComponentsByControlEventStateMachineIdAndControllableComponentIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControllableComponent`, info
    from the `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControllableComponent` you could get from the
    connection.
    '''



class StateMachineControllableComponentsByControlEventStateMachineIdAndControllableComponentIdManyToManyEdge(sgqlc.types.Type):
    '''A `ControllableComponent` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControllableComponent', graphql_name='node')
    '''The `ControllableComponent` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class StateMachineEventProposalsByControlEventStateMachineIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateMachineEventProposalsByControlEventStateMachineIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `ControlEvent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class StateMachineEventProposalsByControlEventStateMachineIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `ControlEvent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'control_events')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class StateMachinesConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `StateMachine` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('StateMachine')), graphql_name='nodes')
    '''A list of `StateMachine` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StateMachinesEdge'))), graphql_name='edges')
    '''A list of edges which contains the `StateMachine` and cursor to
    aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `StateMachine` you could get from the
    connection.
    '''



class StateMachinesEdge(sgqlc.types.Type):
    '''A `StateMachine` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('StateMachine', graphql_name='node')
    '''The `StateMachine` at the end of the edge.'''



class TransitionControlEventPayload(sgqlc.types.Type):
    __schema__ = control_schema
    __field_names__ = ('control_event', 'query')
    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')

    query = sgqlc.types.Field('Query', graphql_name='query')



class UpdateControlEventLogPayload(sgqlc.types.Type):
    '''The output of our update `ControlEventLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_log', 'query', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'control_event_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event_log = sgqlc.types.Field('ControlEventLog', graphql_name='controlEventLog')
    '''The `ControlEventLog` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `ControlEventLog`.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    '''Reads a single `ControlEvent` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''

    control_event_log_edge = sgqlc.types.Field(ControlEventLogsEdge, graphql_name='controlEventLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEventLog`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateControlEventPayload(sgqlc.types.Type):
    '''The output of our update `ControlEvent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event', 'query', 'control_event_state_by_current_state', 'event_proposal', 'controllable_component', 'state_machine', 'control_event_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event = sgqlc.types.Field('ControlEvent', graphql_name='controlEvent')
    '''The `ControlEvent` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEvent`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `ControlEvent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `ControlEvent`.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''Reads a single `StateMachine` that is related to this
    `ControlEvent`.
    '''

    control_event_edge = sgqlc.types.Field(ControlEventsEdge, graphql_name='controlEventEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEvent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateControlEventStatePayload(sgqlc.types.Type):
    '''The output of our update `ControlEventState` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'control_event_state', 'query', 'control_event_state_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    control_event_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventState')
    '''The `ControlEventState` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    control_event_state_edge = sgqlc.types.Field(ControlEventStatesEdge, graphql_name='controlEventStateEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControlEventState`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class UpdateControllableComponentPayload(sgqlc.types.Type):
    '''The output of our update `ControllableComponent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'controllable_component', 'query', 'facility', 'controlled_by_edge_node_client', 'controllable_component_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''The `ControllableComponent` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `ControllableComponent`.
    '''

    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    '''Reads a single `EdgeNode` that is related to this
    `ControllableComponent`.
    '''

    controllable_component_edge = sgqlc.types.Field(ControllableComponentsEdge, graphql_name='controllableComponentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ControllableComponent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class UpdateEdgeNodePayload(sgqlc.types.Type):
    '''The output of our update `EdgeNode` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'edge_node', 'query', 'organization', 'facility', 'edge_node_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    edge_node = sgqlc.types.Field('EdgeNode', graphql_name='edgeNode')
    '''The `EdgeNode` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `EdgeNode`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EdgeNode`.'''

    edge_node_edge = sgqlc.types.Field(EdgeNodesEdge, graphql_name='edgeNodeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EdgeNode`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateEventProposalLogPayload(sgqlc.types.Type):
    '''The output of our update `EventProposalLog` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_log', 'query', 'by_user', 'by_edge_node', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'event_proposal', 'event_proposal_log_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal_log = sgqlc.types.Field('EventProposalLog', graphql_name='eventProposalLog')
    '''The `EventProposalLog` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    '''Reads a single `User` that is related to this `EventProposalLog`.'''

    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalLog`.
    '''

    event_proposal_log_edge = sgqlc.types.Field(EventProposalLogsEdge, graphql_name='eventProposalLogEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposalLog`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateEventProposalMetricPayload(sgqlc.types.Type):
    '''The output of our update `EventProposalMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal_metric', 'query', 'project_success_metric', 'controllable_component', 'event_proposal', 'event_proposal_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal_metric = sgqlc.types.Field('EventProposalMetric', graphql_name='eventProposalMetric')
    '''The `EventProposalMetric` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''Reads a single `ProjectSuccessMetric` that is related to this
    `EventProposalMetric`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal_metric_edge = sgqlc.types.Field(EventProposalMetricsEdge, graphql_name='eventProposalMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposalMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class UpdateEventProposalPayload(sgqlc.types.Type):
    '''The output of our update `EventProposal` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'event_proposal', 'query', 'project', 'facility', 'control_event_state_by_current_state', 'event_proposal_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''The `EventProposal` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

    event_proposal_edge = sgqlc.types.Field(EventProposalsEdge, graphql_name='eventProposalEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `EventProposal`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateFacilityPayload(sgqlc.types.Type):
    '''The output of our update `Facility` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility', 'query', 'organization', 'facility_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''The `Facility` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Facility`.'''

    facility_edge = sgqlc.types.Field(FacilitiesEdge, graphql_name='facilityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Facility`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateFacilityUserPayload(sgqlc.types.Type):
    '''The output of our update `FacilityUser` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'facility_user', 'query', 'facility', 'user', 'facility_user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    facility_user = sgqlc.types.Field('FacilityUser', graphql_name='facilityUser')
    '''The `FacilityUser` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `FacilityUser`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `FacilityUser`.'''

    facility_user_edge = sgqlc.types.Field(FacilityUsersEdge, graphql_name='facilityUserEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilityUsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `FacilityUser`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateOrganizationPayload(sgqlc.types.Type):
    '''The output of our update `Organization` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'organization', 'query', 'organization_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''The `Organization` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization_edge = sgqlc.types.Field(OrganizationsEdge, graphql_name='organizationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Organization`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateProjectAgentPayload(sgqlc.types.Type):
    '''The output of our update `ProjectAgent` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_agent', 'query', 'project', 'user', 'project_agent_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_agent = sgqlc.types.Field('ProjectAgent', graphql_name='projectAgent')
    '''The `ProjectAgent` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `ProjectAgent`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `ProjectAgent`.'''

    project_agent_edge = sgqlc.types.Field(ProjectAgentsEdge, graphql_name='projectAgentEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectAgent`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateProjectPayload(sgqlc.types.Type):
    '''The output of our update `Project` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project', 'query', 'organization', 'project_type', 'project_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''The `Project` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Project`.'''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''Reads a single `ProjectType` that is related to this `Project`.'''

    project_edge = sgqlc.types.Field(ProjectsEdge, graphql_name='projectEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `Project`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateProjectSuccessMetricPayload(sgqlc.types.Type):
    '''The output of our update `ProjectSuccessMetric` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_success_metric', 'query', 'project', 'project_success_metric_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''The `ProjectSuccessMetric` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `ProjectSuccessMetric`.
    '''

    project_success_metric_edge = sgqlc.types.Field(ProjectSuccessMetricsEdge, graphql_name='projectSuccessMetricEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectSuccessMetric`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    '''



class UpdateProjectTypePayload(sgqlc.types.Type):
    '''The output of our update `ProjectType` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'project_type', 'query', 'project_type_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''The `ProjectType` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project_type_edge = sgqlc.types.Field(ProjectTypesEdge, graphql_name='projectTypeEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectTypesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `ProjectType`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[ProjectTypesOrderBy!]`): The method to use when
      ordering `ProjectType`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateStateDefinitionPayload(sgqlc.types.Type):
    '''The output of our update `StateDefinition` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_definition', 'query', 'project', 'state_definition_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinition')
    '''The `StateDefinition` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this
    `StateDefinition`.
    '''

    state_definition_edge = sgqlc.types.Field(StateDefinitionsEdge, graphql_name='stateDefinitionEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateDefinition`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateStateMachinePayload(sgqlc.types.Type):
    '''The output of our update `StateMachine` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'state_machine', 'query', 'state_definition_by_state_definition', 'state_machine_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''The `StateMachine` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    state_definition_by_state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `StateMachine`.
    '''

    state_machine_edge = sgqlc.types.Field(StateMachinesEdge, graphql_name='stateMachineEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `StateMachine`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UpdateUserPayload(sgqlc.types.Type):
    '''The output of our update `User` mutation.'''
    __schema__ = control_schema
    __field_names__ = ('client_mutation_id', 'user', 'query', 'user_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    '''The exact same `clientMutationId` that was provided in the
    mutation input, unchanged and unused. May be used by a client to
    track mutations.
    '''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''The `User` that was updated by this mutation.'''

    query = sgqlc.types.Field('Query', graphql_name='query')
    '''Our root query field type. Allows us to run any query from our
    mutation payload.
    '''

    user_edge = sgqlc.types.Field('UsersEdge', graphql_name='userEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
))
    )
    '''An edge for our `User`. May be used by Relay 1.

    Arguments:

    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    '''



class UserControlEventStatesByEventProposalLogByUserIdAndCurrentStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserControlEventStatesByEventProposalLogByUserIdAndCurrentStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class UserControlEventStatesByEventProposalLogByUserIdAndCurrentStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_current_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class UserControlEventStatesByEventProposalLogByUserIdAndPreviousStateManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `ControlEventState` values, with data
    from `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ControlEventState')), graphql_name='nodes')
    '''A list of `ControlEventState` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserControlEventStatesByEventProposalLogByUserIdAndPreviousStateManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `ControlEventState`, info from
    the `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `ControlEventState` you could get from the
    connection.
    '''



class UserControlEventStatesByEventProposalLogByUserIdAndPreviousStateManyToManyEdge(sgqlc.types.Type):
    '''A `ControlEventState` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_previous_state')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('ControlEventState', graphql_name='node')
    '''The `ControlEventState` at the end of the edge.'''

    event_proposal_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class UserEdgeNodesByEventProposalLogByUserIdAndByEdgeNodeIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EdgeNode` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EdgeNode')), graphql_name='nodes')
    '''A list of `EdgeNode` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserEdgeNodesByEventProposalLogByUserIdAndByEdgeNodeIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EdgeNode`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EdgeNode` you could get from the connection.'''



class UserEdgeNodesByEventProposalLogByUserIdAndByEdgeNodeIdManyToManyEdge(sgqlc.types.Type):
    '''A `EdgeNode` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs_by_by_edge_node_id')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EdgeNode', graphql_name='node')
    '''The `EdgeNode` at the end of the edge.'''

    event_proposal_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class UserEventProposalsByEventProposalLogByUserIdAndEventProposalIdManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `EventProposal` values, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventProposal')), graphql_name='nodes')
    '''A list of `EventProposal` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserEventProposalsByEventProposalLogByUserIdAndEventProposalIdManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `EventProposal`, info from the
    `EventProposalLog`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `EventProposal` you could get from the
    connection.
    '''



class UserEventProposalsByEventProposalLogByUserIdAndEventProposalIdManyToManyEdge(sgqlc.types.Type):
    '''A `EventProposal` edge in the connection, with data from
    `EventProposalLog`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'event_proposal_logs')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('EventProposal', graphql_name='node')
    '''The `EventProposal` at the end of the edge.'''

    event_proposal_logs = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class UserFacilitiesManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Facility` values, with data from
    `FacilityUser`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Facility')), graphql_name='nodes')
    '''A list of `Facility` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserFacilitiesManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Facility`, info from the
    `FacilityUser`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Facility` you could get from the connection.'''



class UserFacilitiesManyToManyEdge(sgqlc.types.Type):
    '''A `Facility` edge in the connection, with data from
    `FacilityUser`.
    '''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'facility_users')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Facility', graphql_name='node')
    '''The `Facility` at the end of the edge.'''

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
    '''Reads and enables pagination through a set of `FacilityUser`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityUserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class UserProjectsManyToManyConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `Project` values, with data from
    `ProjectAgent`.
    '''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Project')), graphql_name='nodes')
    '''A list of `Project` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserProjectsManyToManyEdge'))), graphql_name='edges')
    '''A list of edges which contains the `Project`, info from the
    `ProjectAgent`, and the cursor to aid in pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `Project` you could get from the connection.'''



class UserProjectsManyToManyEdge(sgqlc.types.Type):
    '''A `Project` edge in the connection, with data from `ProjectAgent`.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node', 'project_agents')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('Project', graphql_name='node')
    '''The `Project` at the end of the edge.'''

    project_agents = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentsConnection), graphql_name='projectAgents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectAgentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ProjectAgent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectAgentCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class UsersConnection(sgqlc.types.relay.Connection):
    '''A connection to a list of `User` values.'''
    __schema__ = control_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='nodes')
    '''A list of `User` objects.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsersEdge'))), graphql_name='edges')
    '''A list of edges which contains the `User` and cursor to aid in
    pagination.
    '''

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Information to aid in pagination.'''

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    '''The count of *all* `User` you could get from the connection.'''



class UsersEdge(sgqlc.types.Type):
    '''A `User` edge in the connection.'''
    __schema__ = control_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    '''A cursor for use in pagination.'''

    node = sgqlc.types.Field('User', graphql_name='node')
    '''The `User` at the end of the edge.'''



class ControlEvent(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'current_state', 'event_proposal_id', 'controllable_component_id', 'state_machine_id', 'control_event_state_by_current_state', 'event_proposal', 'controllable_component', 'state_machine', 'control_event_logs', 'edge_nodes_by_control_event_log_control_event_id_and_by_edge_node_id', 'control_event_states_by_control_event_log_control_event_id_and_previous_state', 'control_event_states_by_control_event_log_control_event_id_and_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')

    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')

    state_machine_id = sgqlc.types.Field(UUID, graphql_name='stateMachineId')

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEvent`.
    '''

    event_proposal = sgqlc.types.Field('EventProposal', graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `ControlEvent`.
    '''

    controllable_component = sgqlc.types.Field('ControllableComponent', graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `ControlEvent`.
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine')
    '''Reads a single `StateMachine` that is related to this
    `ControlEvent`.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControlEventLog(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'control_event_id', 'previous_state', 'current_state', 'label', 'event_type', 'data', 'by_edge_node', 'control_event', 'control_event_state_by_previous_state', 'control_event_state_by_current_state')
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

    by_edge_node = sgqlc.types.Field('EdgeNode', graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `ControlEventLog`.
    '''

    control_event = sgqlc.types.Field(ControlEvent, graphql_name='controlEvent')
    '''Reads a single `ControlEvent` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field('ControlEventState', graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `ControlEventLog`.
    '''



class ControlEventState(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('state', 'rules', 'created_at', 'updated_at', 'control_events_by_current_state', 'event_proposal_logs_by_previous_state', 'event_proposal_logs_by_current_state', 'event_proposals_by_current_state', 'control_event_logs_by_previous_state', 'control_event_logs_by_current_state', 'event_proposals_by_control_event_current_state_and_event_proposal_id', 'controllable_components_by_control_event_current_state_and_controllable_component_id', 'state_machines_by_control_event_current_state_and_state_machine_id', 'users_by_event_proposal_log_previous_state_and_by_user_id', 'edge_nodes_by_event_proposal_log_previous_state_and_by_edge_node_id', 'control_event_states_by_event_proposal_log_previous_state_and_current_state', 'event_proposals_by_event_proposal_log_previous_state_and_event_proposal_id', 'users_by_event_proposal_log_current_state_and_by_user_id', 'edge_nodes_by_event_proposal_log_current_state_and_by_edge_node_id', 'control_event_states_by_event_proposal_log_current_state_and_previous_state', 'event_proposals_by_event_proposal_log_current_state_and_event_proposal_id', 'projects_by_event_proposal_current_state_and_project_id', 'facilities_by_event_proposal_current_state_and_facility_id', 'edge_nodes_by_control_event_log_previous_state_and_by_edge_node_id', 'control_events_by_control_event_log_previous_state_and_control_event_id', 'control_event_states_by_control_event_log_previous_state_and_current_state', 'edge_nodes_by_control_event_log_current_state_and_by_edge_node_id', 'control_events_by_control_event_log_current_state_and_control_event_id', 'control_event_states_by_control_event_log_current_state_and_previous_state')
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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposal_logs_by_previous_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposal_logs_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposalsByCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_control_event_current_state_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEventProposalsByControlEventCurrentStateAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByControlEventCurrentStateAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    controllable_components_by_control_event_current_state_and_controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControllableComponentsByControlEventCurrentStateAndControllableComponentIdManyToManyConnection), graphql_name='controllableComponentsByControlEventCurrentStateAndControllableComponentId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    state_machines_by_control_event_current_state_and_state_machine_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateStateMachinesByControlEventCurrentStateAndStateMachineIdManyToManyConnection), graphql_name='stateMachinesByControlEventCurrentStateAndStateMachineId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateMachineCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateMachine`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateMachineCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    users_by_event_proposal_log_previous_state_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateUsersByEventProposalLogPreviousStateAndByUserIdManyToManyConnection), graphql_name='usersByEventProposalLogPreviousStateAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    edge_nodes_by_event_proposal_log_previous_state_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEdgeNodesByEventProposalLogPreviousStateAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByEventProposalLogPreviousStateAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_log_previous_state_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventStatesByEventProposalLogPreviousStateAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogPreviousStateAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_log_previous_state_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEventProposalsByEventProposalLogPreviousStateAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalLogPreviousStateAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    users_by_event_proposal_log_current_state_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateUsersByEventProposalLogCurrentStateAndByUserIdManyToManyConnection), graphql_name='usersByEventProposalLogCurrentStateAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    edge_nodes_by_event_proposal_log_current_state_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEdgeNodesByEventProposalLogCurrentStateAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByEventProposalLogCurrentStateAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_log_current_state_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateControlEventStatesByEventProposalLogCurrentStateAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogCurrentStateAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_log_current_state_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateEventProposalsByEventProposalLogCurrentStateAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalLogCurrentStateAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    projects_by_event_proposal_current_state_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateProjectsByEventProposalCurrentStateAndProjectIdManyToManyConnection), graphql_name='projectsByEventProposalCurrentStateAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    facilities_by_event_proposal_current_state_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(ControlEventStateFacilitiesByEventProposalCurrentStateAndFacilityIdManyToManyConnection), graphql_name='facilitiesByEventProposalCurrentStateAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ControllableComponent(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'slug', 'facility_id', 'label', 'description', 'controlled_by_edge_node_client_id', 'created_at', 'updated_at', 'is_schedulable', 'facility', 'controlled_by_edge_node_client', 'control_events', 'event_proposals_controlled_components', 'event_proposal_metrics', 'control_event_states_by_control_event_controllable_component_id_and_current_state', 'event_proposals_by_control_event_controllable_component_id_and_event_proposal_id', 'state_machines_by_control_event_controllable_component_id_and_state_machine_id', 'event_proposals', 'state_definitions_by_event_proposals_controlled_component_controllable_component_id_and_state_definition', 'project_success_metrics_by_event_proposal_metric_controllable_component_id_and_project_success_metric_id', 'event_proposals_by_event_proposal_metric_controllable_component_id_and_event_proposal_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')

    description = sgqlc.types.Field(String, graphql_name='description')

    controlled_by_edge_node_client_id = sgqlc.types.Field(String, graphql_name='controlledByEdgeNodeClientId')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    is_schedulable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSchedulable')
    '''Indicator noting if the controllable component can be scheduled
    for a control event
    '''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this
    `ControllableComponent`.
    '''

    controlled_by_edge_node_client = sgqlc.types.Field('EdgeNode', graphql_name='controlledByEdgeNodeClient')
    '''Reads a single `EdgeNode` that is related to this
    `ControllableComponent`.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsControlledComponentsConnection), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    control_event_states_by_control_event_controllable_component_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentControlEventStatesByControlEventControllableComponentIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventControllableComponentIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_control_event_controllable_component_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentEventProposalsByControlEventControllableComponentIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByControlEventControllableComponentIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    state_machines_by_control_event_controllable_component_id_and_state_machine_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentStateMachinesByControlEventControllableComponentIdAndStateMachineIdManyToManyConnection), graphql_name='stateMachinesByControlEventControllableComponentIdAndStateMachineId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateMachineCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateMachine`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateMachineCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentEventProposalsManyToManyConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    state_definitions_by_event_proposals_controlled_component_controllable_component_id_and_state_definition = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentStateDefinitionsByEventProposalsControlledComponentControllableComponentIdAndStateDefinitionManyToManyConnection), graphql_name='stateDefinitionsByEventProposalsControlledComponentControllableComponentIdAndStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateDefinitionCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateDefinition`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateDefinitionCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    project_success_metrics_by_event_proposal_metric_controllable_component_id_and_project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentProjectSuccessMetricsByEventProposalMetricControllableComponentIdAndProjectSuccessMetricIdManyToManyConnection), graphql_name='projectSuccessMetricsByEventProposalMetricControllableComponentIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectSuccessMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ProjectSuccessMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectSuccessMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_metric_controllable_component_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ControllableComponentEventProposalsByEventProposalMetricControllableComponentIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalMetricControllableComponentIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



class EdgeNode(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('client_id', 'organization_id', 'created_at', 'updated_at', 'facility_id', 'last_fetch_time', 'organization', 'facility', 'controllable_components_by_controlled_by_edge_node_client_id', 'event_proposal_logs_by_by_edge_node_id', 'control_event_logs_by_by_edge_node_id', 'facilities_by_controllable_component_controlled_by_edge_node_client_id_and_facility_id', 'users_by_event_proposal_log_by_edge_node_id_and_by_user_id', 'control_event_states_by_event_proposal_log_by_edge_node_id_and_previous_state', 'control_event_states_by_event_proposal_log_by_edge_node_id_and_current_state', 'event_proposals_by_event_proposal_log_by_edge_node_id_and_event_proposal_id', 'control_events_by_control_event_log_by_edge_node_id_and_control_event_id', 'control_event_states_by_control_event_log_by_edge_node_id_and_previous_state', 'control_event_states_by_control_event_log_by_edge_node_id_and_current_state')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    facility_id = sgqlc.types.Field(Int, graphql_name='facilityId')

    last_fetch_time = sgqlc.types.Field(Datetime, graphql_name='lastFetchTime')
    '''The last time the edge communicated with the system to fetch
    control events
    '''

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `EdgeNode`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EdgeNode`.'''

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
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    event_proposal_logs_by_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    users_by_event_proposal_log_by_edge_node_id_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeUsersByEventProposalLogByEdgeNodeIdAndByUserIdManyToManyConnection), graphql_name='usersByEventProposalLogByEdgeNodeIdAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_log_by_edge_node_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogByEdgeNodeIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    control_event_states_by_event_proposal_log_by_edge_node_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeControlEventStatesByEventProposalLogByEdgeNodeIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogByEdgeNodeIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_log_by_edge_node_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(EdgeNodeEventProposalsByEventProposalLogByEdgeNodeIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalLogByEdgeNodeIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposal(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'facility_id', 'start_time', 'end_time', 'type', 'current_state', 'created_at', 'updated_at', 'project', 'facility', 'control_event_state_by_current_state', 'control_events', 'event_proposals_controlled_components', 'event_proposal_metrics', 'event_proposal_logs', 'control_event_states_by_control_event_event_proposal_id_and_current_state', 'controllable_components_by_control_event_event_proposal_id_and_controllable_component_id', 'state_machines_by_control_event_event_proposal_id_and_state_machine_id', 'controlled_components', 'state_definitions_by_event_proposals_controlled_component_event_proposal_id_and_state_definition', 'project_success_metrics_by_event_proposal_metric_event_proposal_id_and_project_success_metric_id', 'controllable_components_by_event_proposal_metric_event_proposal_id_and_controllable_component_id', 'users_by_event_proposal_log_event_proposal_id_and_by_user_id', 'edge_nodes_by_event_proposal_log_event_proposal_id_and_by_edge_node_id', 'control_event_states_by_event_proposal_log_event_proposal_id_and_previous_state', 'control_event_states_by_event_proposal_log_event_proposal_id_and_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    facility_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='facilityId')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')

    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    project = sgqlc.types.Field('Project', graphql_name='project')
    '''Reads a single `Project` that is related to this `EventProposal`.'''

    facility = sgqlc.types.Field('Facility', graphql_name='facility')
    '''Reads a single `Facility` that is related to this `EventProposal`.'''

    control_event_state_by_current_state = sgqlc.types.Field(ControlEventState, graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposal`.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals_controlled_components = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsControlledComponentsConnection), graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposal_logs = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    control_event_states_by_control_event_event_proposal_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControlEventStatesByControlEventEventProposalIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventEventProposalIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    controllable_components_by_control_event_event_proposal_id_and_controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControllableComponentsByControlEventEventProposalIdAndControllableComponentIdManyToManyConnection), graphql_name='controllableComponentsByControlEventEventProposalIdAndControllableComponentId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    state_machines_by_control_event_event_proposal_id_and_state_machine_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalStateMachinesByControlEventEventProposalIdAndStateMachineIdManyToManyConnection), graphql_name='stateMachinesByControlEventEventProposalIdAndStateMachineId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateMachineCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateMachine`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateMachineCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    controlled_components = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControlledComponentsManyToManyConnection), graphql_name='controlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    state_definitions_by_event_proposals_controlled_component_event_proposal_id_and_state_definition = sgqlc.types.Field(sgqlc.types.non_null(EventProposalStateDefinitionsByEventProposalsControlledComponentEventProposalIdAndStateDefinitionManyToManyConnection), graphql_name='stateDefinitionsByEventProposalsControlledComponentEventProposalIdAndStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateDefinitionCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateDefinition`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateDefinitionCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    project_success_metrics_by_event_proposal_metric_event_proposal_id_and_project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalProjectSuccessMetricsByEventProposalMetricEventProposalIdAndProjectSuccessMetricIdManyToManyConnection), graphql_name='projectSuccessMetricsByEventProposalMetricEventProposalIdAndProjectSuccessMetricId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectSuccessMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectSuccessMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ProjectSuccessMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectSuccessMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    controllable_components_by_event_proposal_metric_event_proposal_id_and_controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControllableComponentsByEventProposalMetricEventProposalIdAndControllableComponentIdManyToManyConnection), graphql_name='controllableComponentsByEventProposalMetricEventProposalIdAndControllableComponentId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    users_by_event_proposal_log_event_proposal_id_and_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalUsersByEventProposalLogEventProposalIdAndByUserIdManyToManyConnection), graphql_name='usersByEventProposalLogEventProposalIdAndByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    edge_nodes_by_event_proposal_log_event_proposal_id_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalEdgeNodesByEventProposalLogEventProposalIdAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByEventProposalLogEventProposalIdAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_log_event_proposal_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControlEventStatesByEventProposalLogEventProposalIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogEventProposalIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    control_event_states_by_event_proposal_log_event_proposal_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(EventProposalControlEventStatesByEventProposalLogEventProposalIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogEventProposalIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class EventProposalLog(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'event_time', 'by_user_id', 'by_edge_node_id', 'previous_state', 'current_state', 'label', 'event_type', 'data', 'event_proposal_id', 'by_user', 'by_edge_node', 'control_event_state_by_previous_state', 'control_event_state_by_current_state', 'event_proposal')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    event_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='eventTime')

    by_user_id = sgqlc.types.Field(String, graphql_name='byUserId')

    by_edge_node_id = sgqlc.types.Field(String, graphql_name='byEdgeNodeId')

    previous_state = sgqlc.types.Field(String, graphql_name='previousState')

    current_state = sgqlc.types.Field(String, graphql_name='currentState')

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')

    event_type = sgqlc.types.Field(String, graphql_name='eventType')

    data = sgqlc.types.Field(JSON, graphql_name='data')

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    by_user = sgqlc.types.Field('User', graphql_name='byUser')
    '''Reads a single `User` that is related to this `EventProposalLog`.'''

    by_edge_node = sgqlc.types.Field(EdgeNode, graphql_name='byEdgeNode')
    '''Reads a single `EdgeNode` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_previous_state = sgqlc.types.Field(ControlEventState, graphql_name='controlEventStateByPreviousState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    control_event_state_by_current_state = sgqlc.types.Field(ControlEventState, graphql_name='controlEventStateByCurrentState')
    '''Reads a single `ControlEventState` that is related to this
    `EventProposalLog`.
    '''

    event_proposal = sgqlc.types.Field(EventProposal, graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalLog`.
    '''



class EventProposalMetric(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('project_success_metric_id', 'projected_impact_amount', 'created_at', 'updated_at', 'actual_impact_amount', 'controllable_component_id', 'id', 'event_proposal_id', 'calculation_metadata', 'project_success_metric', 'controllable_component', 'event_proposal')
    project_success_metric_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='projectSuccessMetricId')
    '''E'@manyToManyFieldName projectSuccessMetrics' '''

    projected_impact_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectedImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    actual_impact_amount = sgqlc.types.Field(Float, graphql_name='actualImpactAmount')
    '''The amount of savings impact associated with the specific control
    event and the referenced metric
    '''

    controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='controllableComponentId')
    '''The associated controllable component the savings for this event
    are associated with
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='eventProposalId')

    calculation_metadata = sgqlc.types.Field(JSON, graphql_name='calculationMetadata')

    project_success_metric = sgqlc.types.Field('ProjectSuccessMetric', graphql_name='projectSuccessMetric')
    '''Reads a single `ProjectSuccessMetric` that is related to this
    `EventProposalMetric`.
    '''

    controllable_component = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponent')
    '''Reads a single `ControllableComponent` that is related to this
    `EventProposalMetric`.
    '''

    event_proposal = sgqlc.types.Field(EventProposal, graphql_name='eventProposal')
    '''Reads a single `EventProposal` that is related to this
    `EventProposalMetric`.
    '''



class Facility(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'organization_id', 'created_at', 'updated_at', 'organization', 'edge_nodes', 'controllable_components', 'facility_projects', 'facility_users', 'event_proposals', 'organizations_by_edge_node_facility_id_and_organization_id', 'edge_nodes_by_controllable_component_facility_id_and_controlled_by_edge_node_client_id', 'projects_by_facility_project_facility_id_and_project_id', 'users', 'projects_by_event_proposal_facility_id_and_project_id', 'control_event_states_by_event_proposal_facility_id_and_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Facility`.'''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `FacilityProject`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    * `condition` (`FacilityProjectCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `FacilityUser`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityUserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    organizations_by_edge_node_facility_id_and_organization_id = sgqlc.types.Field(sgqlc.types.non_null(FacilityOrganizationsByEdgeNodeFacilityIdAndOrganizationIdManyToManyConnection), graphql_name='organizationsByEdgeNodeFacilityIdAndOrganizationId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(OrganizationCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Organization`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`OrganizationCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    projects_by_event_proposal_facility_id_and_project_id = sgqlc.types.Field(sgqlc.types.non_null(FacilityProjectsByEventProposalFacilityIdAndProjectIdManyToManyConnection), graphql_name='projectsByEventProposalFacilityIdAndProjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_facility_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(FacilityControlEventStatesByEventProposalFacilityIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalFacilityIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



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
    '''Reads a single `Facility` that is related to this `FacilityUser`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `FacilityUser`.'''



class Organization(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'created_at', 'updated_at', 'edge_nodes', 'projects', 'facilities', 'facilities_by_edge_node_organization_id_and_facility_id', 'project_types_by_project_organization_id_and_project_type_id')
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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    facilities_by_edge_node_organization_id_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(OrganizationFacilitiesByEdgeNodeOrganizationIdAndFacilityIdManyToManyConnection), graphql_name='facilitiesByEdgeNodeOrganizationIdAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `ProjectType`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectTypesOrderBy!]`): The method to use when
      ordering `ProjectType`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectTypeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class Project(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'name', 'description', 'organization_id', 'project_type_id', 'created_at', 'updated_at', 'auto_review', 'organization', 'project_type', 'facility_projects', 'project_success_metrics', 'project_agents', 'event_proposals', 'state_definitions', 'facilities_by_facility_project_project_id_and_facility_id', 'agents', 'facilities_by_event_proposal_project_id_and_facility_id', 'control_event_states_by_event_proposal_project_id_and_current_state')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    organization_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='organizationId')

    project_type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectTypeId')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    auto_review = sgqlc.types.Field(Boolean, graphql_name='autoReview')
    '''If enabled, this project will skip the review process'''

    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    '''Reads a single `Organization` that is related to this `Project`.'''

    project_type = sgqlc.types.Field('ProjectType', graphql_name='projectType')
    '''Reads a single `ProjectType` that is related to this `Project`.'''

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
    '''Reads and enables pagination through a set of `FacilityProject`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    * `condition` (`FacilityProjectCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of
    `ProjectSuccessMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectSuccessMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    project_agents = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentsConnection), graphql_name='projectAgents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectAgentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ProjectAgent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectAgentCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    state_definitions = sgqlc.types.Field(sgqlc.types.non_null(StateDefinitionsConnection), graphql_name='stateDefinitions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateDefinitionCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateDefinition`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateDefinitionCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    agents = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentsManyToManyConnection), graphql_name='agents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(UserCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    facilities_by_event_proposal_project_id_and_facility_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectFacilitiesByEventProposalProjectIdAndFacilityIdManyToManyConnection), graphql_name='facilitiesByEventProposalProjectIdAndFacilityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FacilitiesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(FacilityCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_project_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(ProjectControlEventStatesByEventProposalProjectIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalProjectIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''



class ProjectAgent(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'user_id', 'role', 'created_at', 'updated_at', 'project', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')

    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    project = sgqlc.types.Field(Project, graphql_name='project')
    '''Reads a single `Project` that is related to this `ProjectAgent`.'''

    user = sgqlc.types.Field('User', graphql_name='user')
    '''Reads a single `User` that is related to this `ProjectAgent`.'''



class ProjectSuccessMetric(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'project_id', 'name', 'description', 'units', 'created_at', 'updated_at', 'project', 'event_proposal_metrics', 'controllable_components_by_event_proposal_metric_project_success_metric_id_and_controllable_component_id', 'event_proposals_by_event_proposal_metric_project_success_metric_id_and_event_proposal_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The name of the success metric registered for the associated
    project
    '''

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    '''A brief description of how this metric is tied to savings for the
    project and what it would mean for the facility
    '''

    units = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='units')
    '''The units of this success metric'''

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    project = sgqlc.types.Field(Project, graphql_name='project')
    '''Reads a single `Project` that is related to this
    `ProjectSuccessMetric`.
    '''

    event_proposal_metrics = sgqlc.types.Field(sgqlc.types.non_null(EventProposalMetricsConnection), graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    controllable_components_by_event_proposal_metric_project_success_metric_id_and_controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricControllableComponentsByEventProposalMetricProjectSuccessMetricIdAndControllableComponentIdManyToManyConnection), graphql_name='controllableComponentsByEventProposalMetricProjectSuccessMetricIdAndControllableComponentId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_metric_project_success_metric_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(ProjectSuccessMetricEventProposalsByEventProposalMetricProjectSuccessMetricIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalMetricProjectSuccessMetricIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''



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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Organization`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`OrganizationCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''



class Query(sgqlc.types.Type, Node):
    '''The root query type which gives access points into the data
    universe.
    '''
    __schema__ = control_schema
    __field_names__ = ('query', 'node', 'control_event_logs', 'control_event_states', 'control_events', 'controllable_components', 'edge_nodes', 'event_proposal_logs', 'event_proposal_metrics', 'event_proposals', 'event_proposals_controlled_components', 'facilities', 'facility_projects', 'facility_users', 'organizations', 'project_agents', 'project_success_metrics', 'project_types', 'projects', 'state_definitions', 'state_machines', 'users', 'control_event_log', 'control_event_state', 'control_event', 'controllable_component', 'controllable_component_by_slug_and_facility_id', 'edge_node', 'event_proposal_log', 'event_proposal_metric', 'event_proposal', 'facility', 'facility_user', 'organization', 'project_agent', 'project_success_metric', 'project_type', 'project', 'state_definition', 'state_machine', 'user', 'control_events_by_edge_node_client_id', 'edge_control_events', 'facility_enrollment_status_for_project', 'control_event_log_by_node_id', 'control_event_state_by_node_id', 'control_event_by_node_id', 'controllable_component_by_node_id', 'edge_node_by_node_id', 'event_proposal_log_by_node_id', 'event_proposal_metric_by_node_id', 'event_proposal_by_node_id', 'facility_by_node_id', 'facility_user_by_node_id', 'organization_by_node_id', 'project_agent_by_node_id', 'project_success_metric_by_node_id', 'project_type_by_node_id', 'project_by_node_id', 'state_definition_by_node_id', 'state_machine_by_node_id', 'user_by_node_id')
    query = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='query')
    '''Exposes the root query type nested one level down. This is helpful
    for Relay 1 which can only query top level fields if they are in a
    particular form.
    '''

    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Fetches an object given its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID`.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventLogsOrderBy!]`): The method to use
      when ordering `ControlEventLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventLogCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposal_logs = sgqlc.types.Field(EventProposalLogsConnection, graphql_name='eventProposalLogs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposal_metrics = sgqlc.types.Field(EventProposalMetricsConnection, graphql_name='eventProposalMetrics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalMetricsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalMetricCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalMetricsOrderBy!]`): The method to use
      when ordering `EventProposalMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals = sgqlc.types.Field(EventProposalsConnection, graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    event_proposals_controlled_components = sgqlc.types.Field(EventProposalsControlledComponentsConnection, graphql_name='eventProposalsControlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `FacilityProject`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityProjectsOrderBy!]`): The method to use
      when ordering `FacilityProject`. (default: `[NATURAL]`)
    * `condition` (`FacilityProjectCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `FacilityUser`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityUserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Organization`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[OrganizationsOrderBy!]`): The method to use when
      ordering `Organization`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`OrganizationCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    project_agents = sgqlc.types.Field(ProjectAgentsConnection, graphql_name='projectAgents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectAgentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ProjectAgent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectAgentCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of
    `ProjectSuccessMetric`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectSuccessMetricsOrderBy!]`): The method to
      use when ordering `ProjectSuccessMetric`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectSuccessMetricCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `ProjectType`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectTypesOrderBy!]`): The method to use when
      ordering `ProjectType`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectTypeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    state_definitions = sgqlc.types.Field(StateDefinitionsConnection, graphql_name='stateDefinitions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateDefinitionsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateDefinitionCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateDefinition`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateDefinitionsOrderBy!]`): The method to use
      when ordering `StateDefinition`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateDefinitionCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    state_machines = sgqlc.types.Field(StateMachinesConnection, graphql_name='stateMachines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateMachineCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateMachine`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateMachineCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

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
    '''Reads and enables pagination through a set of `User`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[UsersOrderBy!]`): The method to use when ordering
      `User`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`UserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_log = sgqlc.types.Field(ControlEventLog, graphql_name='controlEventLog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    control_event_state = sgqlc.types.Field(ControlEventState, graphql_name='controlEventState', args=sgqlc.types.ArgDict((
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `state` (`String!`)None
    '''

    control_event = sgqlc.types.Field(ControlEvent, graphql_name='controlEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    controllable_component = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    controllable_component_by_slug_and_facility_id = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponentBySlugAndFacilityId', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('facility_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='facilityId', default=None)),
))
    )
    '''Arguments:

    * `slug` (`String!`)None
    * `facility_id` (`Int!`)None
    '''

    edge_node = sgqlc.types.Field(EdgeNode, graphql_name='edgeNode', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    '''Arguments:

    * `client_id` (`String!`)None
    '''

    event_proposal_log = sgqlc.types.Field(EventProposalLog, graphql_name='eventProposalLog', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    event_proposal_metric = sgqlc.types.Field(EventProposalMetric, graphql_name='eventProposalMetric', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    event_proposal = sgqlc.types.Field(EventProposal, graphql_name='eventProposal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    facility = sgqlc.types.Field(Facility, graphql_name='facility', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`Int!`)None
    '''

    facility_user = sgqlc.types.Field(FacilityUser, graphql_name='facilityUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    project_agent = sgqlc.types.Field(ProjectAgent, graphql_name='projectAgent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    project_success_metric = sgqlc.types.Field(ProjectSuccessMetric, graphql_name='projectSuccessMetric', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    project_type = sgqlc.types.Field(ProjectType, graphql_name='projectType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)None
    '''

    project = sgqlc.types.Field(Project, graphql_name='project', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)None
    '''

    state_definition = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinition', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    '''Arguments:

    * `slug` (`String!`)None
    '''

    state_machine = sgqlc.types.Field('StateMachine', graphql_name='stateMachine', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`UUID!`)None
    '''

    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    '''Arguments:

    * `email` (`String!`)None
    '''

    control_events_by_edge_node_client_id = sgqlc.types.Field(ControlEventsConnection, graphql_name='controlEventsByEdgeNodeClientId', args=sgqlc.types.ArgDict((
        ('clientid', sgqlc.types.Arg(String, graphql_name='clientid', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `clientid` (`String`)None
    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    '''

    edge_control_events = sgqlc.types.Field(EdgecontroleventsConnection, graphql_name='edgeControlEvents', args=sgqlc.types.ArgDict((
        ('clientid', sgqlc.types.Arg(String, graphql_name='clientid', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Edgecontrolevent`.

    Arguments:

    * `clientid` (`String`)None
    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    '''

    facility_enrollment_status_for_project = sgqlc.types.Field(ProjectenrollmentstatusesConnection, graphql_name='facilityEnrollmentStatusForProject', args=sgqlc.types.ArgDict((
        ('projectid', sgqlc.types.Arg(String, graphql_name='projectid', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `Projectenrollmentstatus`.

    Arguments:

    * `projectid` (`String`)None
    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    '''

    control_event_log_by_node_id = sgqlc.types.Field(ControlEventLog, graphql_name='controlEventLogByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ControlEventLog` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ControlEventLog`.
    '''

    control_event_state_by_node_id = sgqlc.types.Field(ControlEventState, graphql_name='controlEventStateByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ControlEventState` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ControlEventState`.
    '''

    control_event_by_node_id = sgqlc.types.Field(ControlEvent, graphql_name='controlEventByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ControlEvent` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ControlEvent`.
    '''

    controllable_component_by_node_id = sgqlc.types.Field(ControllableComponent, graphql_name='controllableComponentByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ControllableComponent` using its globally unique
    `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ControllableComponent`.
    '''

    edge_node_by_node_id = sgqlc.types.Field(EdgeNode, graphql_name='edgeNodeByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `EdgeNode` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `EdgeNode`.
    '''

    event_proposal_log_by_node_id = sgqlc.types.Field(EventProposalLog, graphql_name='eventProposalLogByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `EventProposalLog` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `EventProposalLog`.
    '''

    event_proposal_metric_by_node_id = sgqlc.types.Field(EventProposalMetric, graphql_name='eventProposalMetricByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `EventProposalMetric` using its globally unique
    `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `EventProposalMetric`.
    '''

    event_proposal_by_node_id = sgqlc.types.Field(EventProposal, graphql_name='eventProposalByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `EventProposal` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `EventProposal`.
    '''

    facility_by_node_id = sgqlc.types.Field(Facility, graphql_name='facilityByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `Facility` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `Facility`.
    '''

    facility_user_by_node_id = sgqlc.types.Field(FacilityUser, graphql_name='facilityUserByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `FacilityUser` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `FacilityUser`.
    '''

    organization_by_node_id = sgqlc.types.Field(Organization, graphql_name='organizationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `Organization` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `Organization`.
    '''

    project_agent_by_node_id = sgqlc.types.Field(ProjectAgent, graphql_name='projectAgentByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ProjectAgent` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ProjectAgent`.
    '''

    project_success_metric_by_node_id = sgqlc.types.Field(ProjectSuccessMetric, graphql_name='projectSuccessMetricByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ProjectSuccessMetric` using its globally unique
    `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ProjectSuccessMetric`.
    '''

    project_type_by_node_id = sgqlc.types.Field(ProjectType, graphql_name='projectTypeByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `ProjectType` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `ProjectType`.
    '''

    project_by_node_id = sgqlc.types.Field(Project, graphql_name='projectByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `Project` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `Project`.
    '''

    state_definition_by_node_id = sgqlc.types.Field('StateDefinition', graphql_name='stateDefinitionByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `StateDefinition` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `StateDefinition`.
    '''

    state_machine_by_node_id = sgqlc.types.Field('StateMachine', graphql_name='stateMachineByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `StateMachine` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `StateMachine`.
    '''

    user_by_node_id = sgqlc.types.Field('User', graphql_name='userByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    '''Reads a single `User` using its globally unique `ID`.

    Arguments:

    * `node_id` (`ID!`): The globally unique `ID` to be used in
      selecting a single `User`.
    '''



class StateDefinition(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('slug', 'project_id', 'label', 'description', 'definition', 'created_at', 'updated_at', 'project', 'event_proposals_controlled_components_by_state_definition', 'state_machines_by_state_definition', 'event_proposals', 'controlled_components')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    definition = sgqlc.types.Field(JSON, graphql_name='definition')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    project = sgqlc.types.Field(Project, graphql_name='project')
    '''Reads a single `Project` that is related to this
    `StateDefinition`.
    '''

    event_proposals_controlled_components_by_state_definition = sgqlc.types.Field(sgqlc.types.non_null(EventProposalsControlledComponentsConnection), graphql_name='eventProposalsControlledComponentsByStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsControlledComponentsOrderBy)), graphql_name='orderBy', default=['NATURAL'])),
        ('condition', sgqlc.types.Arg(EventProposalsControlledComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `EventProposalsControlledComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsControlledComponentsOrderBy!]`): The
      method to use when ordering `EventProposalsControlledComponent`.
      (default: `[NATURAL]`)
    * `condition` (`EventProposalsControlledComponentCondition`): A
      condition to be used in determining which values should be
      returned by the collection.
    '''

    state_machines_by_state_definition = sgqlc.types.Field(sgqlc.types.non_null(StateMachinesConnection), graphql_name='stateMachinesByStateDefinition', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StateMachinesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(StateMachineCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `StateMachine`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[StateMachinesOrderBy!]`): The method to use when
      ordering `StateMachine`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`StateMachineCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    event_proposals = sgqlc.types.Field(sgqlc.types.non_null(StateDefinitionEventProposalsManyToManyConnection), graphql_name='eventProposals', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    controlled_components = sgqlc.types.Field(sgqlc.types.non_null(StateDefinitionControlledComponentsManyToManyConnection), graphql_name='controlledComponents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''



class StateMachine(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('id', 'state_definition', 'current_state', 'context', 'machine', 'state', 'is_active', 'created_at', 'updated_at', 'state_definition_by_state_definition', 'control_events', 'control_event_states_by_control_event_state_machine_id_and_current_state', 'event_proposals_by_control_event_state_machine_id_and_event_proposal_id', 'controllable_components_by_control_event_state_machine_id_and_controllable_component_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')

    state_definition = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stateDefinition')

    current_state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentState')

    context = sgqlc.types.Field(JSON, graphql_name='context')

    machine = sgqlc.types.Field(JSON, graphql_name='machine')

    state = sgqlc.types.Field(JSON, graphql_name='state')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    state_definition_by_state_definition = sgqlc.types.Field(StateDefinition, graphql_name='stateDefinitionByStateDefinition')
    '''Reads a single `StateDefinition` that is related to this
    `StateMachine`.
    '''

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
    '''Reads and enables pagination through a set of `ControlEvent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventsOrderBy!]`): The method to use when
      ordering `ControlEvent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_control_event_state_machine_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(StateMachineControlEventStatesByControlEventStateMachineIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByControlEventStateMachineIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_control_event_state_machine_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(StateMachineEventProposalsByControlEventStateMachineIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByControlEventStateMachineIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

    controllable_components_by_control_event_state_machine_id_and_controllable_component_id = sgqlc.types.Field(sgqlc.types.non_null(StateMachineControllableComponentsByControlEventStateMachineIdAndControllableComponentIdManyToManyConnection), graphql_name='controllableComponentsByControlEventStateMachineIdAndControllableComponentId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControllableComponentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControllableComponentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of
    `ControllableComponent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControllableComponentsOrderBy!]`): The method to
      use when ordering `ControllableComponent`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControllableComponentCondition`): A condition to
      be used in determining which values should be returned by the
      collection.
    '''



class User(sgqlc.types.Type, Node):
    __schema__ = control_schema
    __field_names__ = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at', 'event_proposal_logs_by_by_user_id', 'facility_users', 'project_agents', 'edge_nodes_by_event_proposal_log_by_user_id_and_by_edge_node_id', 'control_event_states_by_event_proposal_log_by_user_id_and_previous_state', 'control_event_states_by_event_proposal_log_by_user_id_and_current_state', 'event_proposals_by_event_proposal_log_by_user_id_and_event_proposal_id', 'facilities', 'projects')
    first_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstName')

    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastName')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    phone_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phoneNumber')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='createdAt')

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='updatedAt')

    event_proposal_logs_by_by_user_id = sgqlc.types.Field(sgqlc.types.non_null(EventProposalLogsConnection), graphql_name='eventProposalLogsByByUserId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalLogsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalLogCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposalLog`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalLogsOrderBy!]`): The method to use
      when ordering `EventProposalLog`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalLogCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `FacilityUser`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilityUsersOrderBy!]`): The method to use when
      ordering `FacilityUser`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityUserCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    project_agents = sgqlc.types.Field(sgqlc.types.non_null(ProjectAgentsConnection), graphql_name='projectAgents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectAgentsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectAgentCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ProjectAgent`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectAgentsOrderBy!]`): The method to use when
      ordering `ProjectAgent`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectAgentCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    edge_nodes_by_event_proposal_log_by_user_id_and_by_edge_node_id = sgqlc.types.Field(sgqlc.types.non_null(UserEdgeNodesByEventProposalLogByUserIdAndByEdgeNodeIdManyToManyConnection), graphql_name='edgeNodesByEventProposalLogByUserIdAndByEdgeNodeId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EdgeNodesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EdgeNodeCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EdgeNode`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EdgeNodesOrderBy!]`): The method to use when
      ordering `EdgeNode`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EdgeNodeCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    control_event_states_by_event_proposal_log_by_user_id_and_previous_state = sgqlc.types.Field(sgqlc.types.non_null(UserControlEventStatesByEventProposalLogByUserIdAndPreviousStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogByUserIdAndPreviousState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    control_event_states_by_event_proposal_log_by_user_id_and_current_state = sgqlc.types.Field(sgqlc.types.non_null(UserControlEventStatesByEventProposalLogByUserIdAndCurrentStateManyToManyConnection), graphql_name='controlEventStatesByEventProposalLogByUserIdAndCurrentState', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ControlEventStatesOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ControlEventStateCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `ControlEventState`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ControlEventStatesOrderBy!]`): The method to use
      when ordering `ControlEventState`. (default:
      `[PRIMARY_KEY_ASC]`)
    * `condition` (`ControlEventStateCondition`): A condition to be
      used in determining which values should be returned by the
      collection.
    '''

    event_proposals_by_event_proposal_log_by_user_id_and_event_proposal_id = sgqlc.types.Field(sgqlc.types.non_null(UserEventProposalsByEventProposalLogByUserIdAndEventProposalIdManyToManyConnection), graphql_name='eventProposalsByEventProposalLogByUserIdAndEventProposalId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EventProposalsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(EventProposalCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `EventProposal`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[EventProposalsOrderBy!]`): The method to use when
      ordering `EventProposal`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`EventProposalCondition`): A condition to be used
      in determining which values should be returned by the
      collection.
    '''

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
    '''Reads and enables pagination through a set of `Facility`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[FacilitiesOrderBy!]`): The method to use when
      ordering `Facility`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`FacilityCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''

    projects = sgqlc.types.Field(sgqlc.types.non_null(UserProjectsManyToManyConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectsOrderBy)), graphql_name='orderBy', default=['PRIMARY_KEY_ASC'])),
        ('condition', sgqlc.types.Arg(ProjectCondition, graphql_name='condition', default=None)),
))
    )
    '''Reads and enables pagination through a set of `Project`.

    Arguments:

    * `first` (`Int`): Only read the first `n` values of the set.
    * `last` (`Int`): Only read the last `n` values of the set.
    * `offset` (`Int`): Skip the first `n` values from our `after`
      cursor, an alternative to cursor based pagination. May not be
      used with `last`.
    * `before` (`Cursor`): Read all values in the set before (above)
      this cursor.
    * `after` (`Cursor`): Read all values in the set after (below)
      this cursor.
    * `order_by` (`[ProjectsOrderBy!]`): The method to use when
      ordering `Project`. (default: `[PRIMARY_KEY_ASC]`)
    * `condition` (`ProjectCondition`): A condition to be used in
      determining which values should be returned by the collection.
    '''




########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
control_schema.query_type = Query
control_schema.mutation_type = Mutation
control_schema.subscription_type = None

