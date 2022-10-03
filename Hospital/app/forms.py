from dataclasses import fields

from django import forms
from .models import Patient,Doctor,BlogPost,EventModel
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget, AdminSplitDateTime

class PatientForm(forms.ModelForm): 
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
  
    class Meta:
        model = Patient
        fields=['user','first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode']

        widgets={
          "first_name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "last_name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "username":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "email":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "address1":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "city":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "state":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "pincode":forms.TextInput(attrs={'class':'form-control form-control-sm'})

      }
    

    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )




class DoctorForm(forms.ModelForm):    
    class Meta:
        model = Doctor
        fields=['first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title","image","category","summary","content")




class EventModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = "__all__"
        widgets={
            "date":AdminDateWidget(),
            "start_time":AdminTimeWidget(),
        }