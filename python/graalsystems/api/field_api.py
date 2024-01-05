# coding: utf-8

"""
    Tenant API

    Tenant API

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr

from typing import List

from graalsystems.models.field import Field

from graalsystems.api_client import ApiClient
from graalsystems.api_response import ApiResponse
from graalsystems.rest import RESTResponseType


class FieldApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_field(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        field: Annotated[Field, Field(description="The field to be created")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Field:
        """Create a field


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param field: The field to be created (required)
        :type field: Field
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_field_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            field=field,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Field",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def create_field_with_http_info(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        field: Annotated[Field, Field(description="The field to be created")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Field]:
        """Create a field


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param field: The field to be created (required)
        :type field: Field
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_field_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            field=field,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Field",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def create_field_without_preload_content(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        field: Annotated[Field, Field(description="The field to be created")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create a field


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param field: The field to be created (required)
        :type field: Field
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_field_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            field=field,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Field",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_field_serialize(
        self,
        x_tenant,
        layer_name,
        database_name,
        table_name,
        field,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if layer_name is not None:
            _path_params['layer_name'] = layer_name
        if database_name is not None:
            _path_params['database_name'] = database_name
        if table_name is not None:
            _path_params['table_name'] = table_name
        # process the query parameters
        # process the header parameters
        if x_tenant is not None:
            _header_params['X-Tenant'] = x_tenant
        # process the form parameters
        # process the body parameter
        if field is not None:
            _body_params = field


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.graal.systems.v1.field+json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.graal.systems.v1.field+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'internal'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/layers/{layer_name}/databases/{database_name}/tables/{table_name}/fields',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def find_fields(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Field]:
        """Retrieve all fields


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_fields_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Field]",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def find_fields_with_http_info(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Field]]:
        """Retrieve all fields


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_fields_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Field]",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def find_fields_without_preload_content(
        self,
        x_tenant: StrictStr,
        layer_name: Annotated[StrictStr, Field(description="Name of the layer")],
        database_name: Annotated[StrictStr, Field(description="Name of the database")],
        table_name: Annotated[StrictStr, Field(description="Name of the table")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve all fields


        :param x_tenant: (required)
        :type x_tenant: str
        :param layer_name: Name of the layer (required)
        :type layer_name: str
        :param database_name: Name of the database (required)
        :type database_name: str
        :param table_name: Name of the table (required)
        :type table_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_fields_serialize(
            x_tenant=x_tenant,
            layer_name=layer_name,
            database_name=database_name,
            table_name=table_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Field]",
            '400': None,
            '405': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _find_fields_serialize(
        self,
        x_tenant,
        layer_name,
        database_name,
        table_name,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if layer_name is not None:
            _path_params['layer_name'] = layer_name
        if database_name is not None:
            _path_params['database_name'] = database_name
        if table_name is not None:
            _path_params['table_name'] = table_name
        # process the query parameters
        # process the header parameters
        if x_tenant is not None:
            _header_params['X-Tenant'] = x_tenant
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.graal.systems.v1.field+json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'internal'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/layers/{layer_name}/databases/{database_name}/tables/{table_name}/fields',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

