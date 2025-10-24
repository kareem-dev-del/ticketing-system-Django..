from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *

# Create your views here.
def register_customer(request):
    if request.POST:
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False) #commit=False = أنشئ object في RAM بس (لسه مش في DB)
            new.is_customer = True
            new.save()
            messages.success(request,'make user Succefully...')
            return redirect('login')#home
        else:
            # print(form.errors)
           # messages.warning(request,'')
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterCustomerForm()
    return render(request,'register.html',{'form' : form})   

def login_customer(request):
    error_message = None  # هنا هنسجل رسالة الخطأ
    if request.POST:
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request , username=username , password = password)
       if user is not None and user.is_active:
           login(request,user)
           messages.success(request , 'Logged in Successfully... ')
           return redirect('/')
       else:
        messages.warning(request, 'Error Try agin....')
        error_message = 'Invalid username or password'

    return render(request, 'login.html', {'error': error_message})

def logout_customer(request):
    logout(request)   #بيمسح الـ session بالكامل ويشيل أي بيانات
    messages.warning(request, 'Logged out....') 
    return redirect('login')                                                   
