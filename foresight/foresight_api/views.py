from django.shortcuts import render
from foresight_api.models import Users,Contact_Info,Room_Data,Customer_History
from rest_framework import viewsets
from foresight_api.serializers import Users_Serializer,Contact_Info_Serializer,Room_Data_Serializer,Customer_History_Serializer
from rest_framework import viewsets, filters, generics

class Users_ViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Users_Serializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('RFID','firstName','lastName')

class Contact_Info_ViewSet(viewsets.ModelViewSet):
	queryset = Contact_Info.objects.all()
	serializer_class = Contact_Info_Serializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ['user_id']

class Room_Data_ViewSet(viewsets.ModelViewSet):
	queryset = Room_Data.objects.all()
	serializer_class = Room_Data_Serializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ['user_id','hotel','roomNum']

class Customer_History_ViewSet(viewsets.ModelViewSet):
	queryset = Customer_History.objects.all()
	serializer_class = Customer_History_Serializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ['hotel','roomNum']