from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from foresight_api import views
from views import Users_ViewSet,Contact_Info_ViewSet

router = routers.DefaultRouter()
router.register(r'Users', views.Users_ViewSet)
router.register(r'Contact_Info', views.Contact_Info_ViewSet)
filter_fields = ('code')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^Users/(?P<pk>[0-9]+)/$', views.Users_ViewSet.as_view()),
    #url(r'^Contact_Info/(?P<pk>[0-9]+)/$', views.Contact_Info_ViewSet.as_view()),
)