# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import six
from django.template import Context, Template
from django.test import TestCase

from external_urls.templatetags.external_urls import external_url


class ExternalUrlViewsTest(TestCase):

    def test_external_link_view_redirect(self):
        """test ExternalLinkView redirect to correct URL"""

        url = 'https://example.com/page/1'
        encoded_url = six.b(external_url(url))
        response = self.client.get(encoded_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, url)


class ExternalUrlTempalteTagTest(TestCase):

    def test_external_url(self):
        """test external_url template tag"""

        template = Template(
            '''{% load external_urls %}
               <html>
               {% external_url 'https://example.com/' %}
               </html>
            '''
        )
        html = template.render(Context())
        self.assertIn('/goto/aHR0cHM6Ly9leGFtcGxlLmNvbS8=', html)
