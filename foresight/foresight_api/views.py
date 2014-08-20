from django.shortcuts import render
from foresight_api.models import Users,Contact_Info,Room_Data
from rest_framework import viewsets
from foresight_api.serializers import Users_Serializer,Contact_Info_Serializer,Room_Data_Serializer

class Users_ViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Users_Serializer

class Contact_Info_ViewSet(viewsets.ModelViewSet):
	queryset = Contact_Info.objects.all()
	serializer_class = Contact_Info_Serializer

class Room_Data_ViewSet(viewsets.ModelViewSet):
	queryset = Room_Data.objects.all()
	serializer_class = Room_Data_Serializer