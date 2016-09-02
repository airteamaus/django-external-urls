from django.conf.urls import url

from . views import ExternalLinkView

urlpatterns = [
    url(r'^goto/(?P<external_url>.+)$', ExternalLinkView.as_view(), name='external_link')
]
