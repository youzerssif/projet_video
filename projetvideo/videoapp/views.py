from django.shortcuts import render

# Create your views here.
def home(request):

    data={}
    return render(request, 'pages/home.html',data)


def acc(request):
    return render(request, 'pages/acc.html')


def login(request):
    return render(request, 'pages/login.html')


def register(request):
    return render(request, 'pages/register.html')


def cat(request, id_cat):
    return render(request, 'pages/videos.html')

def video(request, id_video):
    return render(request, 'vpages/video_lecteur.html')