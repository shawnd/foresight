from django.db import models


class Users(models.Model):
	RFID=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	firstName=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)
	def __unicode__(self):
		return u"%s %s" % (self.RFID)

class Contact_Info(models.Model):
	user_id=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	country=models.CharField(max_length=50)
	postalCode=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	phoneNumber=models.CharField(max_length=50)

class Room_Data(models.Model):
    user_id=models.CharField(max_length=50)
    temp=models.CharField(max_length=50)
    humidityPercentage=models.CharField(max_length=50)
    humidityTemp=models.CharField(max_length=50)
    batteryVoltage=models.CharField(max_length=50)
    airflow=models.CharField(max_length=50)
    timestamp=models.DateTimeField()
    roomNum=models.CharField(max_length=50)
    hotel=models.CharField(max_length=50)

class Customer_History(models.Model):
	user_id=models.CharField(max_length=50)
	hotel=models.CharField(max_length=50)
	roomNum=models.CharField(max_length=50)
	daysStayed=models.CharField(max_length=50)
	timestamp=models.CharField(max_length=50)
	counter=models.IntegerField()

class Recently_Scanned(models.Model):
	employeeID=models.CharField(max_length=50)
	RFID=models.CharField(max_length=50)
	timestamp=models.DateTimeField(auto_now=True)

class User_Avg(models.Model):
	RFID=models.CharField(max_length=50)
	temp=models.IntegerField()