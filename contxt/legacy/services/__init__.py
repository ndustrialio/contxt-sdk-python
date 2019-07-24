import json
from datetime import datetime
from pprint import pformat

import jwt
import pandas as pd
import pytz
import requests
from tabulate import tabulate

from contxt.exceptions import UnauthorizedException

API_VERSION = "v1"


class ApiClient:
    def __init__(self, access_token):

        self.access_token = access_token

    def execute(self, api_request):

        headers = {}
        retries = 3
        status = -1

        response = None

        while status in [-1, 504] and retries > 0:

            # authorize this request?
            if api_request.authorize():
                headers["Authorization"] = "Bearer " + self.access_token

            if api_request.method() == "GET":
                response = requests.get(url=str(api_request), headers=headers)
            if api_request.method() == "POST":
                if api_request.content_type == ApiRequest.URLENCODED_CONTENT_TYPE:
                    response = requests.post(
                        url=str(api_request), data=api_request.body(), headers=headers
                    )
                else:
                    response = requests.post(
                        url=str(api_request), json=api_request.body(), headers=headers
                    )
            if api_request.method() == "PUT":
                response = requests.put(
                    url=str(api_request), data=api_request.body(), headers=headers
                )
            if api_request.method() == "DELETE":
                response = requests.delete(url=str(api_request), headers=headers)

            status = response.status_code
            retries -= 1

        return self.process_response(response)

    def process_response(self, response):

        # throw an exception in case of a status problem
        # response.raise_for_status()

        # lifted the following code from requests/models.py and modified it
        http_error_msg = ""

        if 400 <= response.status_code < 500:
            msg = json.loads(response.text)["message"]
            raise UnauthorizedException(f"{response.reason} - {msg}")

        elif response.status_code == 500:
            msg = json.loads(response.text)["message"]
            http_error_msg = (
                f"{response.status_code} Server Error: {response.reason} - {msg}"
            )

        elif 500 < response.status_code < 600:
            http_error_msg = (
                f"{response.status_code} Server Error: {response.reason}"
                f" - {response.text}"
            )

        if http_error_msg:
            raise requests.exceptions.HTTPError(http_error_msg, response=self)

        # decode json response if there is a response
        if response.status_code != 204:
            return response.json()
        else:
            return None


class PagedEndpoint:
    def __init__(self, base_url, client, request, parameters):
        self.base_url = base_url
        self.client = client
        self.request = request
        self.parameters = parameters

        # set defaults
        self.set_limit(500)
        self.set_offset(0)
        self.response = None

    def set_offset(self, offset):
        self.parameters["offset"] = offset

    def set_limit(self, limit):
        self.parameters["limit"] = limit

    def execute(self):
        return self.client.execute(
            self.request.params(self.parameters).base_url(self.base_url)
        )


class PagedResponse:
    def __init__(self, endpoint):

        self.endpoint = endpoint
        self.data = self.endpoint.execute()

        self.total_records = self.data["_metadata"]["totalRecords"]
        self.offset = self.data["_metadata"]["offset"]

        self.records = self.data["records"]
        self.retrieved_record_count = len(self.records)

    def get_more_records(self):
        self.endpoint.set_offset(self.retrieved_record_count)
        self.data = self.endpoint.execute()

        self.records = self.data["records"]
        self.retrieved_record_count += len(self.records)

    def __iter__(self):

        while True:

            for record in self.records:
                yield record

            if self.retrieved_record_count < self.total_records:

                # go get more records
                self.get_more_records()

            else:
                break


class DataResponse(object):
    def __init__(self, data, client):
        self.client = client
        self.count = data["meta"]["count"]
        self.has_more = data["meta"]["has_more"]

        self.next_page_url = None
        if self.has_more:
            self.next_page_url = data["meta"]["next_page_url"]

        self.records = data["records"]

    def __iter__(self):

        while True:
            for record in self.records:
                record["event_time"] = datetime.strptime(
                    record["event_time"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ).replace(tzinfo=pytz.UTC)
                yield record

            if self.has_more:
                response = self.client.execute(
                    StringRequest(self.next_page_url).method("GET")
                )

                self.count = response["meta"]["count"]
                self.has_more = response["meta"]["has_more"]

                self.next_page_url = None
                if self.has_more:
                    self.next_page_url = response["meta"]["next_page_url"]

                self.records = response["records"]
            else:
                break


class StringRequest:
    URLENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
    JSON_CONTENT_TYPE = "application/json"

    def __init__(self, request_string):
        self.request_string = request_string

        # authorize request, default true
        self.authorize_request = True

        self.http_content_type = self.JSON_CONTENT_TYPE

        self.http_body = {}

        self.http_method = None

    def authorize(self, authorize=None):

        if authorize is None:
            return self.authorize_request
        else:
            self.authorize_request = authorize

            return self

    def body(self, body=None):
        if body is None:
            return self.http_body
        else:
            self.http_body = body
            return self

    def content_type(self, content_type=None):

        if content_type is None:
            return self.http_content_type
        else:
            self.http_content_type = content_type
            return self

    def method(self, method=None):
        if method is None:
            return self.http_method
        else:
            self.http_method = method
            return self

    def __str__(self):
        return self.request_string


class ApiRequest:
    URLENCODED_CONTENT_TYPE = "application/x-www-form-urlencoded"
    JSON_CONTENT_TYPE = "application/json"

    def __init__(self, uri, authorize=True):

        self.uri = uri

        self.http_base_url = None

        # authorize request, default true
        self.authorize_request = authorize

        self.http_content_type = self.JSON_CONTENT_TYPE

        self.http_params = {}

        self.api_version = True

        self.http_method = None

        self.http_body = {}

    def params(self, params=None):

        if params is None:
            return self.http_params
        else:
            self.http_params = params
            return self

    def authorize(self, authorize=None):

        if authorize is None:
            return self.authorize_request
        else:
            self.authorize_request = authorize

            return self

    def base_url(self, base_url=None):
        if base_url is None:
            return self.http_base_url
        else:
            self.http_base_url = base_url

            return self

    def version(self, version=None):

        if version is None:
            return self.api_version
        else:
            self.api_version = version
            return self

    def method(self, method=None):
        if method is None:
            return self.http_method
        else:
            self.http_method = method
            return self

    def content_type(self, content_type=None):

        if content_type is None:
            return self.http_content_type
        else:
            self.http_content_type = content_type
            return self

    def body(self, body=None):
        if body is None:
            return self.http_body
        else:
            self.http_body = body
            return self

    def __str__(self):

        request_chunks = []

        request_chunks.append(self.http_base_url)

        if self.api_version:
            request_chunks.append(API_VERSION)

        request_chunks.append(self.uri)

        # append params
        if self.http_params:
            param_string = "?"

            param_list = []

            for p, v in self.http_params.items():
                param_list.append(p + "=" + str(v))

            param_string += "&".join(param_list)

            request_string = "/".join(request_chunks) + param_string

        else:
            request_string = "/".join(request_chunks)

        return request_string


class GET(ApiRequest):
    def __init__(self, uri, authorize=True):
        super().__init__(uri, authorize)

    def method(self, method=None):
        return "GET"


class POST(ApiRequest):
    def __init__(self, uri, authorize=True):
        super().__init__(uri, authorize)

    def method(self, method=None):
        return "POST"


class PUT(ApiRequest):
    def __init__(self, uri, authorize=True):
        super().__init__(uri, authorize)

    def method(self, method=None):
        return "PUT"


class DELETE(ApiRequest):
    def __init__(self, uri, authorize=True):
        super().__init__(uri, authorize)

    def method(self, method=None):
        return "DELETE"


class ApiService:
    def __init__(self, base_url):

        self.client = None
        self.base_url = base_url

    def execute(self, api_request, execute=True):

        if execute:

            result = self.client.execute(api_request.base_url(self.base_url))

            return result

        else:
            return api_request.base_url(self.base_url)


class Service(ApiService):
    def __init__(self, base_url, access_token):

        super().__init__(base_url)

        self.client = ApiClient(access_token=access_token)

    def get_logged_in_user_id(self):
        # TODO do actual token verification
        decoded_token = jwt.decode(self.client.access_token, verify=False)
        return decoded_token["sub"]


def to_raw(v):
    if isinstance(v, APIObject) or isinstance(v, APIObjectDict):
        return v.get_dict()
    elif isinstance(v, APIObjectCollection):
        return v.get_dicts()
    else:
        return v


class APIObject:
    def __init__(self, keys_to_ignore=None):
        # TODO: may want to following a naming pattern for ignored keys, like
        # prefixed with _ instead of explicitly declaring the ignored keys
        self._keys_to_ignore = {"_keys_to_ignore"} | set(keys_to_ignore or [])

    def get_dict(self):
        return {
            k: to_raw(v)
            for k, v in self.__dict__.items()
            if k not in self._keys_to_ignore
        }

    def get_keys(self):
        return self.get_dict().keys()

    def get_values(self):
        return self.get_dict().values()

    def get_df(self):
        d = self.get_dict()
        return pd.DataFrame(data=d.values(), columns=d.keys())

    def pretty_print(self):
        dict = self.get_dict()
        return pformat(dict, indent=4)

    def __str__(self):
        d = self.get_dict()
        return tabulate([d.values()], headers=d.keys())


class APIObjectCollection:
    def __init__(self, obj_list):
        assert isinstance(obj_list, list)

        self.list_of_objects = obj_list

    def __repr__(self):
        if not self.list_of_objects:
            return "None"
        vals = [obj.get_values() for obj in self.list_of_objects]
        return tabulate(vals, headers=self.list_of_objects[0].get_keys())

    def __iter__(self):
        for item in self.list_of_objects:
            yield item

    def __len__(self):
        return len(self.list_of_objects)

    def __getitem__(self, item):
        return self.list_of_objects.__getitem__(item)

    def get_dicts(self):
        return [to_raw(o) for o in self.list_of_objects]

    def get_keys(self):
        dicts = self.get_dicts()
        return dicts[0].keys() if dicts else []

    def get_values(self):
        dicts = self.get_dicts()
        return [d.values() for d in dicts]

    def get_df(self):
        return pd.DataFrame(self.get_values(), columns=self.get_keys())

    def pretty_print(self):
        if not self.list_of_objects:
            return "None"
        vals = [obj for obj in self.list_of_objects]
        return pformat(vals, indent=4)


class APIObjectDict:
    def __init__(self, obj_dict: dict):
        self.dict_of_objects = obj_dict

    def get_dict(self):
        return {key: to_raw(self.dict_of_objects[key]) for key in self.dict_of_objects}

    def pretty_print(self):
        if not self.dict_of_objects:
            return "None"
        return pformat(self.dict_of_objects, indent=4)

    def __str__(self):
        d = self.get_dict()
        return tabulate([d.values()], headers=d.keys())
