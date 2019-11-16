from django.shortcuts import render , Http404
import requests
import json
from django.http import JsonResponse
from .models import *

# Create your views here.
def editor(request,exo):
    try :
        exercice = Exercice.objects.filter(id=exo)[:1].get
    except:
        raise Http404('erreur 404')
    data={
        'exos':exercice
    }

    return render(request, 'pages/editor.html',data)


def postCode(request):
    # url pour avoir le token
    base_url_post = 'https://api.judge0.com//submissions?base64_encoded=false&wait=false'

 
    # url = 'https://tpcg.tutorialspoint.com/tpcg.php'
    cod = request.POST.get('contentA')
    print('code----------' ,cod)

    
    
    
    # data = {
    #     'lang': 'python',
    #     'device': '',
    #     'code': cod,
    #     'stdinput': '',
    #     'ext': 'py',
    #     'compile': '0',
    #     'execute': 'python main.py',
    #     'mainfile': 'main.py',
    #     'uid': '5116890',
    # }
    # https://api.judge0.com//submissions/9f046ab5-cda4-4dda-92e7-25878eab11c5?base64_encoded=false&wait=false
    data = {
        'source_code': cod,
        'language_id': 35,
        'code': cod,
        'expected_output': '6',
    }
    req = requests.post(base_url_post, data = data)
    token = req.text
    data = json.loads(token)
    token= data['token']
    print(token)
    base_url_get = 'https://api.judge0.com/submissions/{}?base64_encoded=false'.format(token)
    reqapi=requests.get(base_url_get)
    resultat = reqapi.text
    datapi = json.loads(resultat)

    while datapi['status']['id'] == 1 or datapi['status']['id'] == 2 :

        reqapi=requests.get(base_url_get)

    if datapi['status']['id'] == 3:
        resultat = "Resultat Valide"
    else:
        resultat=datapi['status']['description']
    
    print(resultat)
    # print(reqapi.status_code)
    # print(req.text)
    datas = {
        'succes':True,
        'resultat': resultat
    }
    return JsonResponse(datas, safe=False)
#django-admin-interface

def niveau(request):
    

    exercice = Exercice.objects.all()
    data={
        # 'niveau':niveau,
        'exercice':exercice,
    }

    return render(request, 'pages/niveau.html',data)