from foresight_api.models import Users,Contact_Info
from rest_framework import serializers

class Users_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Users
		fields = ('id','RFID','password','firstName','lastName')

class Contact_Info_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact_Info
		fields = ('address','country','postalCode','email','phoneNumber')