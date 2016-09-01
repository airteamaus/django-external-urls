django-external-urls
========================

.. _badges:

.. image:: https://travis-ci.org/sv0/django-external-urls.svg?branch=master
    :target: https://travis-ci.org/sv0/django-external-urls

.. image:: https://coveralls.io/repos/github/sv0/django-external-urls/badge.svg?branch=master
    :target: https://coveralls.io/github/sv0/django-external-urls?branch=master


Captures clicks on external links, and invokes a callback (signal).

Useful for tracking outbound links.

    pip install django-external-urls


Settings:
------------------------

Add to ``settings.py``::

    INSTALLED_APPS = (
        'external_urls',
    )

Add to ``url.py``::

    urlpatterns = patterns('',
        url(r'', include('external_urls.urls')),
    )


Usage:
------------------------

1. The templates can be used as follows::

    {% load external_urls %}
    {% external_url object.website %}
    {% external_url "http://example.com/" %}

2. Sends a Signal, ``external_link``::

    from external_links.signals import external_click
    from django.dispatch import receiver

    @receiver(external_click)
    def my_callback(sender, url, ip):
        print("tracked click to {} from {}".format(url, ip))
