from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(requests):
    if requests.method=='POST':
        username=requests.POST['username']
        password=requests.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requests,user)
            return redirect('/')
        else:
            messages.info(requests,'invalid credientials')
            return redirect('login')

    else:
        return render(requests,'login.html')
def register(requests):
    if requests.method =="POST":
        first_name=requests.POST['first_name']
        last_name = requests.POST['last_name']
        username = requests.POST['username']
        password1 = requests.POST['password1']
        password2 = requests.POST['password2']
        email = requests.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(requests,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(requests,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(requests,"user created")
                return redirect('register')
        else:
            messages.info(requests,'password not matching..')
            return redirect('register')
        return redirect('/')
    else:
        return render(requests,'register.html')


def logout(requests):
    auth.logout(requests)
    return redirect('/')