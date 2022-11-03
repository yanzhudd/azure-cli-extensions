# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "load-test update",
)
class Update(AAZCommand):
    """Update LoadTest resource.
    """

    _aaz_info = {
        "version": "2022-12-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.loadtestservice/loadtests/{}", "2022-12-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.load_test_name = AAZStrArg(
            options=["-n", "--name", "--load-test-name"],
            help="Load Test name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "LoadTestResource"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="LoadTestResource",
            help="The type of identity used for the resource.",
            nullable=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="LoadTestResource",
            help="Resource tags.",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Description of the resource.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=512,
            ),
        )
        _args_schema.encryption = AAZObjectArg(
            options=["--encryption"],
            arg_group="Properties",
            help="CMK Encryption property.",
            nullable=True,
        )

        encryption = cls._args_schema.encryption
        encryption.identity = AAZObjectArg(
            options=["identity"],
            help="All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.",
            nullable=True,
        )
        encryption.key_url = AAZStrArg(
            options=["key-url"],
            help="key encryption key Url, versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.",
            nullable=True,
        )

        identity = cls._args_schema.encryption.identity
        identity.resource_id = AAZStrArg(
            options=["resource-id"],
            help="user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId",
            nullable=True,
        )
        identity.type = AAZStrArg(
            options=["type"],
            help="Managed identity type to use for accessing encryption key Url",
            nullable=True,
            enum={"SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.LoadTestsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.LoadTestsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class LoadTestsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "loadTestName", self.ctx.args.load_test_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_load_test_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class LoadTestsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "loadTestName", self.ctx.args.load_test_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_load_test_resource_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("encryption", AAZObjectType, ".encryption")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("identity", AAZObjectType, ".identity")
                encryption.set_prop("keyUrl", AAZStrType, ".key_url")

            identity = _builder.get(".properties.encryption.identity")
            if identity is not None:
                identity.set_prop("resourceId", AAZStrType, ".resource_id")
                identity.set_prop("type", AAZStrType, ".type")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_load_test_resource_read = None


def _build_schema_load_test_resource_read(_schema):
    global _schema_load_test_resource_read
    if _schema_load_test_resource_read is not None:
        _schema.id = _schema_load_test_resource_read.id
        _schema.identity = _schema_load_test_resource_read.identity
        _schema.location = _schema_load_test_resource_read.location
        _schema.name = _schema_load_test_resource_read.name
        _schema.properties = _schema_load_test_resource_read.properties
        _schema.system_data = _schema_load_test_resource_read.system_data
        _schema.tags = _schema_load_test_resource_read.tags
        _schema.type = _schema_load_test_resource_read.type
        return

    _schema_load_test_resource_read = AAZObjectType()

    load_test_resource_read = _schema_load_test_resource_read
    load_test_resource_read.id = AAZStrType(
        flags={"read_only": True},
    )
    load_test_resource_read.identity = AAZObjectType()
    load_test_resource_read.location = AAZStrType(
        flags={"required": True},
    )
    load_test_resource_read.name = AAZStrType(
        flags={"read_only": True},
    )
    load_test_resource_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    load_test_resource_read.system_data = AAZObjectType(
        serialized_name="systemData",
        flags={"read_only": True},
    )
    load_test_resource_read.tags = AAZDictType()
    load_test_resource_read.type = AAZStrType(
        flags={"read_only": True},
    )

    identity = _schema_load_test_resource_read.identity
    identity.principal_id = AAZStrType(
        serialized_name="principalId",
        flags={"read_only": True},
    )
    identity.tenant_id = AAZStrType(
        serialized_name="tenantId",
        flags={"read_only": True},
    )
    identity.type = AAZStrType(
        flags={"required": True},
    )
    identity.user_assigned_identities = AAZDictType(
        serialized_name="userAssignedIdentities",
    )

    user_assigned_identities = _schema_load_test_resource_read.identity.user_assigned_identities
    user_assigned_identities.Element = AAZObjectType()

    _element = _schema_load_test_resource_read.identity.user_assigned_identities.Element
    _element.client_id = AAZStrType(
        serialized_name="clientId",
        flags={"read_only": True},
    )
    _element.principal_id = AAZStrType(
        serialized_name="principalId",
        flags={"read_only": True},
    )

    properties = _schema_load_test_resource_read.properties
    properties.data_plane_uri = AAZStrType(
        serialized_name="dataPlaneURI",
        flags={"read_only": True},
    )
    properties.description = AAZStrType()
    properties.encryption = AAZObjectType()
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
    )

    encryption = _schema_load_test_resource_read.properties.encryption
    encryption.identity = AAZObjectType()
    encryption.key_url = AAZStrType(
        serialized_name="keyUrl",
    )

    identity = _schema_load_test_resource_read.properties.encryption.identity
    identity.resource_id = AAZStrType(
        serialized_name="resourceId",
    )
    identity.type = AAZStrType()

    system_data = _schema_load_test_resource_read.system_data
    system_data.created_at = AAZStrType(
        serialized_name="createdAt",
    )
    system_data.created_by = AAZStrType(
        serialized_name="createdBy",
    )
    system_data.created_by_type = AAZStrType(
        serialized_name="createdByType",
    )
    system_data.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
    )
    system_data.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
    )
    system_data.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
    )

    tags = _schema_load_test_resource_read.tags
    tags.Element = AAZStrType()

    _schema.id = _schema_load_test_resource_read.id
    _schema.identity = _schema_load_test_resource_read.identity
    _schema.location = _schema_load_test_resource_read.location
    _schema.name = _schema_load_test_resource_read.name
    _schema.properties = _schema_load_test_resource_read.properties
    _schema.system_data = _schema_load_test_resource_read.system_data
    _schema.tags = _schema_load_test_resource_read.tags
    _schema.type = _schema_load_test_resource_read.type


__all__ = ["Update"]
