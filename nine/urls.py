from django.conf.urls import patterns, include, url
from nine.views import square


urlpatterns = patterns('',
    url(r'^square/$', square),
    url(r'^heroes/$', heroes),
    url(r'^heroes/(?P<course_slug>[\w-]+)$', hero),

#    url(r'^(?P<course_id>\d+)/$', course_item),
#    url(r'^(?P<course_slug>[\w-]+)/$', course_view),
)
