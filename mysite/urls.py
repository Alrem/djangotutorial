from django.conf.urls import patterns, include, url
from django.contrib import admin
from nine import urls

urlpatterns = patterns(
    '',
    url(r'^nine/', include('nine.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
