import json
import random
import string
from string import digits
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import *


# Create your views here.
def home(request):

    data={}
    return render(request, 'home.html',data)


def deconnexion(request):
    logout(request)
    return redirect('mylogin')
    return render(request, 'pages/home.html')


def acc(request):
    return render(request, 'pages/acc.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def loginUser(request):
    postdata = json.loads(request.body.decode('utf-8'))
    username=postdata['username']
    password=postdata['pass']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        print("user is login")
        login(request, user)
        if next: 
            return redirect(next)
        else:
            return redirect('acc') # page si connect
    else:
        return render(request, 'pages/login.html')


def registerUser(request):
    postdata = json.loads(request.body.decode('utf-8'))
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 10000000:
        compt+=1
    name=postdata['name']
    email=postdata['email']
    password=postdata['pass']
    repass = postdata['re_pass']
    module = postdata['module']
    
        
    print("name ++++++++++++++++++++",name)
    isemail=False
    print("email +++++++++++++++++++",email)
    print("password+++++++++++++++++++",password)
    print("repassword +++++++++++++++++++",repass)
    print("module +++++++++++++++++++",module)
    if (len(name)!=0 and len(password)!=0): 
        if password==repass:
            try:
                validate_email(email)
                isemail=True
            except:
                data={
                    'success':False,
                    'message':'Entrez un Email Valide...'
                }
            if isemail:
                try:
                    # User
                    user = User(username=name , email = email )
                    user.save()
                    user.password = password
                    user.set_password(user.password)
                    user.save()
                    myModule=Module.objects.filter(pk=1)
                    
                    print(myModule)
                    myJeton=10
                    myApiKay=myTex=''.join(random.choice(string.ascii_uppercase+string.digits) for i in range(20))
                    newUser=User_module(user=user,module=myModule,jeton=myJeton,jeton_restant=myJeton,apiKay=myApiKay,status=True)
                    newUser.save()
                
                    data={
                        'success':True,
                        'message':'enregistrement effectue avec succes '
                    }
                except Exception as err:
                    print(err)
                    data={
                        'success':False,
                        'message':'Error pendant  de l\'enregistrement '
                    }
        else:
            data={
                'success':False,
                'message':'Error password'
            }
    else:
                
                
        data={
        'success':False,
        'message':'Tous Les champs sont requis *',
    }
    return JsonResponse(data, safe=False)


def cat(request, id_cat):
    return render(request, 'pages/videos.html')

def video(request, id_video):
    return render(request, 'vpages/video_lecteur.html')
