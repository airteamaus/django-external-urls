from __future__ import absolute_import, division, print_function
import base64
import six

from django.views.generic import RedirectView

from external_urls.signals import external_click


class ExternalLinkView(RedirectView):

    permanent = False

    def dispatch(self, request, external_url, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        if six.PY2:
            self.url = base64.decodestring(external_url)
        elif six.PY3:
            self.url = base64.decodebytes(bytes(external_url, 'utf-8')).decode('utf-8')
        external_click.send_robust(sender=self.__class__, url=self.url, ip=ip)
        return super(ExternalLinkView, self).dispatch(request, *args, **kwargs)
