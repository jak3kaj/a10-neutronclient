# Copyright (C) 2016 A10 Networks Inc. All rights reserved.

import operator

from a10_openstack_lib.resources import a10_certificate
from neutronclient.common import utils

from a10_neutronclient import client_extension


class CertificateExtension(client_extension.ClientExtension):

    resource = a10_certificates.CERTIFICATE
    resource_plural = a10_certificates.CERTIFICATES

    resource_attribute_map = a10_certificates.RESOURCE_ATTRIBUTE_MAP

    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class CertificateList(client_extension.List, CertificateExtension):
    """List A10 SSL Certificates"""

    shell_command = 'a10-certificate-list'

    list_columns = ['id', 'name', 'description', 'cert_data', 'key_data', 'intermediate_data', 'password']


class CertificateCreate(client_extension.Create, CertificateExtension):
    """Create A10 scaling group"""

    shell_command = 'a10-certificate-create'

    list_columns = ['id', 'name', 'description', 'cert_data', 'key_data', 'intermediate_data', 'password']

    def add_known_arguments(self, parser):
        self._add_known_arguments(parser, ['name'])


class CertificateDelete(client_extension.Delete, ScalingGroupExtension):
    """Delete A10 SSL Certificate"""

    shell_command = 'a10-certificate-delete'


class CertificateShow(client_extension.Show, ScalingGroupExtension):
    """Show A10 SSL Certificate"""

    shell_command = 'a10-certificate-show'


class CertificateBindingExtension(client_extension.ClientExtension):

    resource = a10_certificate.CERTIFICATE_BINDING
    resource_plural = a10_certificate.CERTIFICATE_BINDINGS

    resource_attribute_map = a10_certificate.RESOURCE_ATTRIBUTE_MAP

    object_path = '%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class CertificateBindingList(client_extension.List, CertificateBindingExtension):
    """List A10 A10 SSL Certificate <-> Listener Bindings"""

    shell_command = 'a10-certificatebinding-list'

    list_columns = ['certificate_id', 'listener_id']


class CertificateBindingCreate(client_extension.Create, CertificateBindingExtension):
    """Create A10 scaling group worker"""

    shell_command = 'a10-certificatebinding-create'
    list_columns = ['certificate_id', 'listener_id']

    def add_known_arguments(self, parser):
        self._add_known_arguments(parser, ['certificate_id', 'listener_id'])


class CertificateBindingDelete(client_extension.Delete, CertificateBindingExtension):
    """Delete A10 scaling group worker"""

    shell_command = 'a10-certificatebinding-delete'


class CertificateBindingShow(client_extension.Show, CertificateBindingExtension):
    """Show A10 scaling group worker"""

    shell_command = 'a10-certificatebinding-show'


