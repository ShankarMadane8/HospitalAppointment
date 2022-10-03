from django.shortcuts import render,redirect
from .forms import  PatientForm,DoctorForm,BlogPostForm,EventModelForm
from .models import BlogPost, Doctor,Patient,EventModel
import datetime
# Create your views here.


def Dashboard(request):
  if request.session.get("user")==None:  
    return redirect("login")
  user=request.session.get("user")
  name=request.session.get("name")
  doctors=Doctor.objects.all()
  blogs=BlogPost.objects.all()
  return render(request,"app/dashboard.html",{"name":name,"user":user,"blogs":blogs,"doctors":doctors})
  
def Signup(request): 
  if request.session.get("name")!=None:
    return redirect("dashboard")
  msg=''
  if request.method=='POST':
    fm=PatientForm(data=request.POST,files=request.FILES)
    print("-------------------Aftter validation------------------------")
    if fm.is_valid():
      user=fm.cleaned_data["user"]
      print("-------------------before validation------------------------")
      print("----------------------------------------------")
      print("user:",user,user=="Patient")
      print("-----------------------------------------------")
      if user=="Patient":
        print("patient save---------------------------  ")
        fm.save()
        msg="Patient-your are successfully registerd !!!"
        fm=PatientForm()
      else:
        first_name=fm.cleaned_data["first_name"]
        last_name=fm.cleaned_data["last_name"]
        profile_picture=fm.cleaned_data["profile_picture"]
        username=fm.cleaned_data["username"]
        email=fm.cleaned_data["email"]
        password=fm.cleaned_data["password"]
        confirm_password=fm.cleaned_data["confirm_password"]
        address1=fm.cleaned_data["address1"]
        city=fm.cleaned_data["city"]
        state=fm.cleaned_data["state"]
        pincode=fm.cleaned_data["pincode"]
        d=Doctor(first_name=first_name,last_name=last_name,profile_picture=profile_picture,username=username,email=email,password=password,confirm_password=confirm_password,address1=address1,city=city,state=state,pincode=pincode)
        d.save()
        print("doctor save  ---------------------------  ")
        msg="Doctor-your are successfully registerd !!!"
        fm=PatientForm()
      
  else:
    fm=PatientForm()

  return render(request,"app/signup.html",{"fm":fm,"msg":msg})

def Login(request):
  if request.session.get("name")!=None:
    return redirect("dashboard")
  errors=""
  if request.method=="POST":    
    email=request.POST['email']
    password=request.POST['password']
    errors=None     
    try:
      if request.POST['user']=="Patient":
        User=Patient.objects.get(email=email)
      else:
        User=Doctor.objects.get(email=email)
    except:
      errors='Enter valid email and password !!!'
      
    if not errors:
      if password==User.password:
        request.session["user"]=request.POST["user"]
        request.session["name"]=User.first_name
        request.session["email"]=User.email
        return redirect("dashboard")
      else:
        errors='Enter valid  password !!!'
    
  form=PatientForm()
  return render(request,"app/login.html",{"forms":form,"errors":errors})

def logout(request):
  del request.session['user']
  del request.session["name"]
  del request.session["email"]
  return redirect('login')


def blogPost(request):
  
  msg=''
  if request.method=='POST':
    print("--------------------",request.FILES,"--------------------")
    fm=BlogPostForm(data=request.POST,files=request.FILES,)
    if fm.is_valid():    
      print("Blog save---------------------------  ")
      fm.save()
      msg="Successfully Blog Post Add !!!"
      fm=BlogPostForm()
  else:
    fm=BlogPostForm()
  return render(request,"app/blogPost.html",{"fm":fm,"msg":msg})




def update_post(request,id):
  msg=""
  if request.method=="POST":
    blog=BlogPost.objects.get(id=id)
    fm=BlogPostForm(request.POST,request.FILES,instance=blog)
    if fm.is_valid():
      fm.save()
      msg="update blog post successfully !!!"
  else:
    blog=BlogPost.objects.get(id=id)
    fm=BlogPostForm(instance=blog)
  return render(request,'app/blogPost.html',{"fm":fm,"msg":msg})
  

def delete_post(requset,id):
	pi=BlogPost.objects.get(pk=id)
	pi.delete()
	return redirect('dashboard')



def bookAppointment(request):
  email=request.GET.get("email")
  first_name=request.GET.get("first_name")
  last_name=request.GET.get("last_name")
  if request.method=="POST":
    form=EventModelForm(request.POST)
    if form.is_valid():
      obj=form.save()
      msg="Add Appointment"
      email=request.GET.get("email")
      first_name=request.GET.get("first_name")
      last_name=request.GET.get("last_name")
      required_speciality=form.cleaned_data["required_speciality"]
      date=form.cleaned_data["date"]
      start_time=form.cleaned_data["start_time"]

      print("---------------------------")
      print(email," ",required_speciality," ",date," ",start_time)
      print(obj.id)
      print("--------------------")
      request.session["appointment"+email]=obj.id
  form=EventModelForm()
  return render(request,"app/bookAppointment.html",{"form":form,"email":email,"first_name":first_name,"last_name":last_name})



def appointmentDetails(request):
  events=EventModel.objects.all()
  email=request.GET.get("email")
  first_name=request.GET.get("first_name") 
  last_name=request.GET.get("last_name")
  appointment=request.session.get("appointment"+email)
  user=request.session.get("user")
  name=request.session.get("name")
  event=EventModel.objects.get(id=appointment)

  print("start time:",event.start_time)
  secs_to_add=45*60
  timeval=event.start_time
  secs = timeval.hour * 3600 + timeval.minute * 60 + timeval.second
  secs += secs_to_add
  end_time=datetime.time(secs // 3600, (secs % 3600) // 60, secs % 60)
  print("end time:",end_time)

  return render(request,"app/appointmentDetails.html",{"events":events,"user":user,"name":name,"appointment":appointment,"end_time":end_time,"first_name":first_name,"last_name":last_name})
