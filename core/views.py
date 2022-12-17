from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse(template.render({}, request))