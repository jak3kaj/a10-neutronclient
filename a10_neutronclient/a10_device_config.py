# Copyright 2015,  A10 Networks
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from a10_openstack_lib.resources import a10_config

from a10_neutronclient import client_extension


class A10DeviceConfigExtension(client_extension.ClientExtension):
    resource = a10_device_config.RESOURCE
    resource_plural = a10_device_config.RESOURCES

    resource_attribute_map = a10_device_config.RESOURCE_ATTRIBUTE_MAP

    object_path = ('/{}').format(resource_plural)
    version = ['2.0']


class A10DeviceConfigShow(client_extension.Show, A10DeviceConfigExtension):
    """Show A10 Configuration"""

    shell_command = 'a10-device-config-show'


class A10DeviceConfigCreate(client_extension.Create, DeviceInstanceExtension):

    shell_command = 'a10-device-config-key-create'
    list_columns = ['name', 'description']


class DeviceInstanceDelete(client_extension.Delete, DeviceInstanceExtension):
    """Delete A10 vThunder Instance"""

    shell_command = 'a10-device-config-key-delete'


class DeviceInstanceUpdate(client_extension.Update, DeviceInstanceExtension):
    """Update A10 vThunder Instance"""

    shell_command = "a10-device-config-update"
    list_columns = ['host', 'api_version', 'conn-limit', 'username', 'password', 'api_version']
