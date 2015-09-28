import re
import base64

from django.views.generic import RedirectView

from external_urls.signals import external_click


class ExternalLinkView(RedirectView):

    def dispatch(self, request, external_url, *args, **kwargs):
        self.ip = request.META['REMOTE_ADDR']
        try:
            self.url = base64.decodestring(external_url)
        except (Exception, ), e:
            if not re.search(r'^http(s)?://', external_url):
                self.url = 'http://{0}'.format(external_url)

        external_click.send(sender=self.__class__, url=self.url, ip=self.ip)
        return super(ExternalLinkView, self).dispatch(request, *args, **kwargs)
