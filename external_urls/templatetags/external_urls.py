from __future__ import absolute_import, division, print_function
import base64
import six

from django.core.urlresolvers import reverse_lazy
from django.template import Library

register = Library()


@register.simple_tag
def external_url(url):
    """Trap external click on external"""
    if six.PY2:
        url = base64.encodestring(url.encode('utf-8')).strip('\n')
    elif six.PY3:
        url = base64.encodebytes(bytes(url, 'utf-8')).strip(b'\n')
    return reverse_lazy('external_link', kwargs={'external_url': url})
