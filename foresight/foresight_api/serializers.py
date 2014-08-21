from foresight_api.models import Users,Contact_Info,Room_Data,Customer_History,Recently_Scanned
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
		fields = ('temp','humidityPercentage','humidityTemp','batteryVoltage','airflow','timestamp','user_id','hotel','roomNum')

class Customer_History_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer_History
		fields = ('hotel','roomNum','daysStayed','timestamp','counter','user_id')

class Recently_Scanned_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Recently_Scanned
		fields = ('employeeID','RFID','timestamp')