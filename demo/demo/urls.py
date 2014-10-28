from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.apiviews import ListUsers
from .routers import router

admin.autodiscover()

urlpatterns = patterns('',
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browseable API.
    url(r'^', include(router.urls)),
    url(r'listusers/$', ListUsers.as_view(), {}, name='api-list-users'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
