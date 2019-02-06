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

from a10_openstack_lib.resources import a10_device

from a10_neutronclient import client_extension


class VThunderExtension(client_extension.ClientExtension):

    resource = a10_device.VTHUNDER
    resource_plural = a10_device.VTHUNDERS

    resource_attribute_map = a10_device.RESOURCE_ATTRIBUTE_MAP

    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class VThunderList(client_extension.List, VThunderExtension):
    """List current A10 vThunder instances"""

    shell_command = 'a10-vthunder-list'
    list_columns = ['id', 'name', 'host', 'api_version', 'nova_instance_id',
                    'description']


class VThunderShow(client_extension.Show, VThunderExtension):
    """Show A10 vThunder instance"""

    shell_command = 'a10-vthunder-show'


class VThunderCreate(client_extension.Create, VThunderExtension):
    """Create A10 vThunder Instance"""

    shell_command = 'a10-vthunder-create'
    list_columns = ['nova-flavor', 'glance-image', 'api-version',
                    'management-network', 'data-neteworks']

    def add_known_arguments(self, parser):
            self._add_known_arguments(
                parser, ['flavor', 'image', 'username', 'password',
                         'api-version', 'management-network',
                         'data-neteworks'])


class VThunderDelete(client_extension.Delete, VThunderExtension):
    """Delete A10 vThunder Instance"""

    shell_command = 'a10-vthunder-delete'


class VThunderUpdate(client_extension.Update, VThunderExtension):
    """Update A10 vThunder Instance"""

    shell_command = 'a10-vthunder-update'
    list_columns = ['nova-flavor', 'glance-image', 'api-version',
                    'management-network', 'data-neteworks']


class DeviceExtension(client_extension.ClientExtension):

    resource = a10_device.DEVICE
    resource_plural = a10_device.DEVICES

    resource_attribute_map = a10_device.RESOURCE_ATTRIBUTE_MAP

    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class DeviceList(client_extension.List, DeviceExtension):
    """List current A10 vThunder instances"""

    shell_command = 'a10-device-list'
    list_columns = ['id', 'name', 'protocol', 'host', 'port', 'api_version',
                    'description']


class DeviceShow(client_extension.Show, DeviceExtension):
    """Show A10 vThunder instance"""

    shell_command = 'a10-device-show'


class DeviceCreate(client_extension.Create, DeviceExtension):

    shell_command = 'a10-device-create'
    list_columns = ['name', 'host', 'protocol', 'port', 'api_version']

    def add_known_arguments(self, parser):
            self._add_known_arguments(parser, ['host', 'username',
                                               'password', 'api_version'])


class DeviceDelete(client_extension.Delete, DeviceExtension):
    """Delete A10 vThunder Instance"""

    shell_command = 'a10-device-delete'


class DeviceUpdate(client_extension.Update, DeviceExtension):
    """Update A10 vThunder Instance"""

    shell_command = 'a10-device-update'
    list_columns = ['name', 'host', 'api_version']


class A10DeviceKeyExtension(client_extension.ClientExtension):

    resource = a10_device.DEVICE_KEY
    resource_plural = a10_device.DEVICE_KEYS

    resource_attribute_map = a10_device.RESOURCE_ATTRIBUTE_MAP

    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class A10DeviceKeyList(client_extension.List, A10DeviceKeyExtension):
    """List current A10 vThunder instances"""

    shell_command = 'a10-device-key-list'
    list_columns = ['name', 'description']


class A10DeviceKeyShow(client_extension.Show, A10DeviceKeyExtension):
    """Show A10 vThunder instance"""

    shell_command = 'a10-device-key-show'
    list_columns = ['id', 'name', 'description', 'default_value', 'type']


class A10DeviceKeyCreate(client_extension.Create, A10DeviceKeyExtension):

    shell_command = 'a10-device-key-create'
    list_columns = ['name', 'description']

    def add_known_arguments(self, parser):
            self._add_known_arguments(parser, ['name'])


class A10DeviceKeyDelete(client_extension.Delete, A10DeviceKeyExtension):
    """Delete A10 vThunder Instance"""

    shell_command = 'a10-device-key-delete'


class A10DeviceKeyUpdate(client_extension.Update, A10DeviceKeyExtension):
    """Update A10 vThunder Instance"""

    shell_command = 'a10-device-key-update'
    list_columns = ['name', 'description']

    def add_known_arguments(self, parser):
            self._add_known_arguments(parser, ['name'])


class A10DeviceValueExtension(client_extension.ClientExtension):

    resource = a10_device.DEVICE_VALUE
    resource_plural = a10_device.DEVICE_VALUES

    resource_attribute_map = a10_device.RESOURCE_ATTRIBUTE_MAP

    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class A10DeviceValueList(client_extension.List, A10DeviceValueExtension):
    """List current A10 vThunder instances"""

    shell_command = 'a10-device-value-list'

    list_columns = ['id', 'key_id', 'device_id', 'value', 'description']


class A10DeviceValueShow(client_extension.Show, A10DeviceValueExtension):
    """Show A10 vThunder instance"""

    shell_command = 'a10-device-value-show'


class A10DeviceValueCreate(client_extension.Create, A10DeviceValueExtension):

    shell_command = 'a10-device-value-create'
    list_columns = ['key_id', 'device_id', 'value', 'description']

    def add_known_arguments(self, parser):
            self._add_known_arguments(parser, ['name'])


class A10DeviceValueDelete(client_extension.Delete, A10DeviceValueExtension):
    """Delete A10 vThunder Instance"""

    shell_command = 'a10-device-value-delete'


class A10DeviceValueUpdate(client_extension.Update, A10DeviceValueExtension):
    """Update A10 vThunder Instance"""

    shell_command = 'a10-device-value-update'
    list_columns = ['key_id', 'device_id', 'value', 'description']

    def add_known_arguments(self, parser):
            self._add_known_arguments(parser, ['name'])
