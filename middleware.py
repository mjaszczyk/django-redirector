# -*- coding: utf-8 *-*
from __future__ import absolute_import

from django.http import QueryDict
from django.core.urlresolvers import reverse, get_callable, RegexURLResolver, Resolver404
from django.conf.urls.defaults import patterns

from .models import Rule
from .views import redirect_to


class Redirector(object):

    _resolver = None

    class RuleNotFound(Exception):
        pass

    @classmethod
    def get_resolver(cls):
        if cls._resolver:
            return cls._resolver

        pats = []
        for rule in Rule.on_site.all():
            view = redirect_to
            params = {}

            if rule.target_view:
                view = rule.target_view
            if rule.target_params:
                params = QueryDict(rule.target_params, mutable=True)
            if rule.target_url_name:
                params = {'url': reverse(rule.target_url_name, kwargs=params)}
            if rule.target_url:
                params = {'url': rule.target_url}
            if rule.redirection_type:
                params['status_code'] = rule.redirection_type

            pats.append((r'^%s$' % rule.pattern, view, params))

        urlpatterns = patterns('', *pats)
        resolver = RegexURLResolver(r'^/', urlpatterns)
        resolver.app_name = 'redirector'
        cls._resolver = resolver
        return resolver

    @classmethod
    def find_redirection(cls, request):
        resolver = cls.get_resolver()
        try:
            matched_rule = resolver.resolve(request.path_info)
        except Resolver404:
            raise Redirector.RuleNotFound
        else:
            return get_callable(matched_rule.view_name)(request, *matched_rule.args,
                **matched_rule.kwargs)


class RedirectorMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            # No need to check for a redirects for non-404 responses.
            return response
        try:
            return Redirector.find_redirection(request)
        except Redirector.RuleNotFound:
            return response
