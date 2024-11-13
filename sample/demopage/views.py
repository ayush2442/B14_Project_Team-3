
from tkinter import image_names
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    return render(request,'index.html')
 
def login(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')
    if(request.method == "POST"):
        un = request.POST['username']
        pw = request.POST['password']
        #authenticate() is used to check for the values present in the database or not
        #if the values are matched, then it will return the username
        #if the values are not matched, then it will return as 'None'
        # use authenticate(), need to import it from auth package
        user = authenticate(request,username=un,password=pw)
        if(user is not None):
            return redirect('/profile')
        else:
            msg = 'Invalid Username/Password'
            form = AuthenticationForm(request.POST)
            return render(request,'login.html',{'form':form,'msg':msg})
    else:
        form = AuthenticationForm()
        #used to create a basic login page with username and password
        return render(request,'login.html',{'form':form})
def login(request):
    if(request.user.is_authenticated):
        return redirect('/login')
    if(request.method == "POST"):
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request,username=un,password=pw)
        if(user is not None):
            return redirect('/profile')
        else:
            msg = 'Invalid Username/Password'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
 
def register(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            un = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            authenticate(username=un,password=pw)
            return redirect('/login')
    else:
        form = UserCreationForm()
        #UserCreationForm() is used to create a basic registration page with username, password and confirm password
        return render(request,'register.html',{'form':form})
 
# def register(request):
#     if(request.user.is_authenticated):
#         return redirect('/')
#     if(request.method == "POST"):
#         un = request.POST['username']
#         pw1 = request.POST['password']
#         pw2 = request.POST['confirmPassword']
#         user = authenticate(request,username=un)
#         print(user)
#         if(user is None):
#             if(pw1==pw2):
#                 authenticate(username=un,password=pw1)
#                 return redirect('/login')
#             else:
#                 msg = 'Incorrect password!'
#                 return render(request,'register.html',{'msg':msg})
#         else:
#             msg = 'User already registered!'
#             return render(request,'register.html',{'msg':msg})
#     else:
#         return render(request,'register.html')
   
def profile(request):
    if(request.method=='POST'):
        image_names = request.FILES.get('uploadImage')
        print(image_names)
        return render(request,'profile.html',{'img':image_names})
    else:
        return render(request,'profile.html')