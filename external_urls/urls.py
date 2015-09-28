from django.conf.urls import patterns, url

from views import ExternalLinkView

urlpatterns = patterns('',
    url(r'^goto/(?P<external_url>.+)$', ExternalLinkView.as_view(), name='external_link'),
)
