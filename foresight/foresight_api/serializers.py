from foresight_api.models import Users,Contact_Info,Room_Data
from rest_framework import serializers

class Users_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Users
		fields = ('id','RFID','password','firstName','lastName')

class Contact_Info_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact_Info
		fields = ('address','country','postalCode','email','phoneNumber','user_id')

class Room_Data_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Room_Data
		fields = ('temp','humidityPercentage','humidityTemp','batteryVoltage','airflow','timestamp','user_id')