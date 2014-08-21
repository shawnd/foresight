from django.shortcuts import render
from foresight_api.models import Users,Contact_Info,Room_Data,Customer_History,Recently_Scanned
from rest_framework import viewsets
from foresight_api.serializers import Users_Serializer,Contact_Info_Serializer,Room_Data_Serializer,Customer_History_Serializer,Recently_Scanned_Serializer
from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
import datetime
from django.utils import timezone
from itertools import chain

class Get_Scanned(APIView):

    def get(self, request, *args, **kw):
       # arg1 = request.GET.get('employee_id',None)
        #response = serializers.serialize("json",Response(Recently_Scanned.objects.order_by('-timestamp')[:5]), status=status.HTTP_200_OK))
        result = serializers.serialize("json", Recently_Scanned.objects.order_by('-timestamp')[:5])
        response = Response(result, status=status.HTTP_200_OK)        
        return response


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

class Recently_Scanned_ViewSet(viewsets.ModelViewSet):
	queryset = Recently_Scanned.objects.all()
	serializer_class = Recently_Scanned_Serializer
	filter_backends = (filters.DjangoFilterBackend,)
	