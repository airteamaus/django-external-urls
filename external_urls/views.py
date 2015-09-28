import base64
from django.views.generic import RedirectView
from external_urls.signals import external_click


class ExternalLinkView(RedirectView):

    permanent = False

    def dispatch(self, request, external_url, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        self.url = base64.decodestring(external_url)
        external_click.send_robust(sender=self.__class__, url=self.url, ip=ip)
        return super(ExternalLinkView, self).dispatch(request, *args, **kwargs)
