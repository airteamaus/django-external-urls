from django import VERSION
from django.conf.urls import url

from external_urls.views import ExternalLinkView

external_link_url = url(r'^goto/(?P<external_url>.+)$', ExternalLinkView.as_view(), name='external_link')

if VERSION >= (1, 8):
    urlpatterns = [external_link_url]
else:
    # django <= 1.7 compatibility
    from django.conf.urls import patterns
    urlpatterns = patterns('', external_link_url)
