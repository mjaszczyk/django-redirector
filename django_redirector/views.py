# -*- coding: utf-8 *-*
from django.http import HttpResponse


def redirect_to(request, url, status_code=301):
    response = HttpResponse()
    response.status_code = status_code
    response['Location'] = url
    return response
