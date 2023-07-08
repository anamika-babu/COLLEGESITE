from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .form import DetailForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if not username or (not password) or (not confirmpassword):
             messages.info(request, "Field is Required")
        else:
             user = User.objects.create_user(username=username, password=password)
             user.save();
             return redirect('login')

    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage/')
        else:
            messages.info(request, "Field is Required ")
            pass
    else:
        return render(request, "login.html")

def newpage(request):
    return render(request, "newpage.html")

def detailform(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Order Confirmed')
    else:
        form = DetailForm()
    return render(request,"detailform.html",{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')
