import json
from enum import Enum
from typing import Any, Dict


class DBOperation(Enum):
    INSERT = 0
    UPDATE = 1
    UPSERT = 2
    DELETE = 3

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class CTRHeader:
    def __init__(self, forwardable=True, deduplicatable=True):
        self.forwardable = forwardable
        self.deduplicatable = deduplicatable


class ChangeTrackingRecord:
    """A JSON Serializable ndustrial.io ChangeTrackingRecord(tm) that is
    ingestable by the ndustrial ETL java/kotlin components.

    topic: Str           - the name of the canonical being ETL-ed
    version: Str         - the change table version or CDC version number (cursor position)
    operation: enum      - a DB operation (insert/update/upsert/delete) from the DBOperation enum
    source_host: Str     - the hostname/ip/table that homes the source data
    source_table: Str    - the name of the table from where the data is being extracted
    source_database: Str - the name of the db being extracted against
    tuple: dict          - key/value pairs that make up the data payload. This
                           value defaults to an empty dict and can be updated after creation
    headers: CTRHeader() - the header information that informs ETL devices what do with the CTR
    """

    def __init__(
        self,
        topic: str,
        version: int,
        operation: DBOperation,
        source_host: str,
        source_table: str,
        source_database: str,
        tuple=dict(),
        headers=CTRHeader(),
    ):

        errors = ""
        if type(topic) is not str:
            errors += "\nTopic parameter must be a string"
        if type(version) is not int:
            errors += "\nVersion parameter must be long (int)"
        if not (DBOperation.has_value(operation)):
            errors += "\nOperation parameter must be member of DBOperation enum"
        if type(source_host) is not str:
            errors += "\nsource_host parameter must be a string"
        if type(source_table) is not str:
            errors += "\nsource_host parameter must be a string"
        if type(source_database) is not str:
            errors += "\nsource_database parameter must be a string"

        if errors:
            raise AttributeError(errors)

        self.topic = topic
        self.version = version
        self.operation = operation
        self.source_host = source_host
        self.source_table = source_table
        self.source_database = source_database
        self.tuple = tuple
        self.headers = headers
        self.addlParams: Dict[str, Any] = dict()

    def getJSONString(self) -> str:
        return json.dumps(self, default=lambda x: x.__dict__)
