import json

from django.http.response import HttpResponse


def params_error(data):
    return HttpResponse(json.dumps({
        'data': data
    }))
