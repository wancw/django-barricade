# coding: utf-8

from django.conf.urls.defaults import url, patterns
from django.http import HttpResponse
from django.views.decorators.cache import never_cache


@never_cache
def dummy_view(request):
    """Dummy view for middleware tests"""

    return HttpResponse('OK')


urlpatterns = patterns('',
    (r'^$', dummy_view),
)
