from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from .models import EventModel, Patient,Doctor,BlogPost,Category
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
   list_display=('user','first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode')
    
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
   list_display=('first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=("title","image","category","summary","content")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display=("category_name",)


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
   list_display=("required_speciality","date","start_time")
