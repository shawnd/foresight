from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from foresight_api import views
from views import Users_ViewSet,Contact_Info_ViewSet,Room_Data_ViewSet,Customer_History_ViewSet,Recently_Scanned_ViewSet,Get_Scanned,User_Avg_ViewSet,Add_Temp,Avg_Temp,Latest_RD

router = routers.DefaultRouter()
router.register(r'Users', views.Users_ViewSet)
router.register(r'Contact_Info', views.Contact_Info_ViewSet)
router.register(r'Room_Data', views.Room_Data_ViewSet)
router.register(r'Customer_History', views.Customer_History_ViewSet)
router.register(r'Recently_Scanned', views.Recently_Scanned_ViewSet)
router.register(r'User_Avg', views.User_Avg_ViewSet)

filter_fields = ('code')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^Users/(?P<pk>[0-9]+)/$', views.Users_ViewSet.as_view()),
    url(r'^Contact_Info/(?P<pk>[0-9]+)/$', views.Contact_Info_ViewSet.as_view()),
    url(r'^Room_Data/(?P<pk>[0-9]+)/$', views.Room_Data_ViewSet.as_view()),
    url(r'^Customer_History/(?P<pk>[0-9]+)/$', views.Room_Data_ViewSet.as_view()),
    url(r'^Recently_Scanned/(?P<pk>[0-9]+)/$', views.Recently_Scanned_ViewSet.as_view()),
    url(r'^User_Avg/(?P<pk>[0-9]+)/$', views.User_Avg_ViewSet.as_view()),
    url(r'^Get_Scanned/', views.Get_Scanned.as_view()),
    url(r'^Add_Temp/', views.Add_Temp.as_view()),
    url(r'^Avg_Temp/', views.Avg_Temp.as_view()),
    url(r'^Latest_RD/', views.Latest_RD.as_view()),
)