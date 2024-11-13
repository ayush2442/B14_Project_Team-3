from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
def home(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    
    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=un, password=pw)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/profile')
        else:
            msg = 'Invalid Username/Password'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user = authenticate(username=un, password=pw)
            
            if user is not None:
                auth_login(request, user)
                return redirect('/profile')
        else:
            msg = 'Please correct the errors below.'
            return render(request, 'register.html', {'form': form, 'msg': msg})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def profile(request):
    img_url = None  # Initialize img_url as None
    if request.method == "POST" and 'profileImage' in request.FILES:
        img_file = request.FILES['profileImage']  # Get the uploaded file
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)  # Save file
        img_url = fs.url(filename)  # Get URL of the uploaded file

    return render(request, 'profile.html', {'uploaded_image_url': img_url})


def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('/')  # Redirect to login page after logout
