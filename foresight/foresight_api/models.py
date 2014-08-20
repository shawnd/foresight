from django.db import models


class Users(models.Model):
	RFID=models.IntegerField()
	password=models.CharField(max_length=50)
	firstName=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)

class Contact_Info(models.Model):
	address=models.CharField(max_length=50)
	country=models.CharField(max_length=50)
	postalCode=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	phoneNumber=models.CharField(max_length=50)

	