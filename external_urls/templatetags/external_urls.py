import base64
from django.core.urlresolvers import reverse_lazy
from django.template import Library

register = Library()


@register.simple_tag
def external_url(url):
    """Trap external click on external"""
    url = base64.encodestring(url.encode('utf-8')).replace("\n", "")
    return reverse_lazy('external_link', kwargs={'external_url': url})

