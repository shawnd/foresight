from django.conf.urls import patterns, include, url
from django.conf import urls, settings
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foresight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^foresight_api/', urls.include('foresight_api.urls')),
)
