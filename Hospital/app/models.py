
from datetime import datetime
from email.headerregistry import Address
from django.db import models

# Create your models here.

class Patient(models.Model):
  User=(
    ("Patient","Patient"),
    ("Doctor","Doctor")
  )

  user = models.CharField(max_length = 20,choices = User)
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  profile_picture=models.ImageField(upload_to='files/',null=True,blank=True)
  username=models.CharField(max_length=50,unique=True)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  confirm_password=models.CharField(max_length=50)
  address1 = models.CharField("Address line 1", max_length=100,)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=12)


class Doctor(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  profile_picture=models.ImageField(upload_to='files/',null=True,blank=True)
  username=models.CharField(max_length=50,unique=True)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  confirm_password=models.CharField(max_length=50)
  address1 = models.CharField("Address line 1", max_length=100,)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=12)



class Category(models.Model):
	category_name=models.CharField(max_length=20)
		
	def get_all_category():
		return Category.objects.all()
	
	def __str__(self):
		return self.category_name
		   

class BlogPost(models.Model):
  title=models.CharField(max_length=50)
  image=models.ImageField(upload_to='file', null=True, blank=True)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
  summary=models.CharField(max_length=15)
  content=models.CharField(max_length=50)


  

class EventModel(models.Model):
  required_speciality=models.CharField(max_length=50)
  date=models.DateField(null=True)
  start_time=models.TimeField(null=True)
 
  