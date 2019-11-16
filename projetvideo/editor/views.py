from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# Create your views here.
def editor(request):
    data={}

    return render(request, 'pages/editor.html',data)


def postCode(request):
    url = 'https://tpcg.tutorialspoint.com/tpcg.php'
    cod = request.POST.get('contentA')
    print('code----------' ,cod)

    
    
    
    data = {
        'lang': 'python',
        'device': '',
        'code': cod,
        'stdinput': '',
        'ext': 'py',
        'compile': '0',
        'execute': 'python main.py',
        'mainfile': 'main.py',
        'uid': '5116890',
    }
    req = requests.post(url, data = data)
    resultat = req.text
    print(resultat)
    # print(req.status_code)
    # print(req.text)
    datas = {
        'succes':True,
        'resultat': resultat
    }
    return JsonResponse(datas, safe=False)
#django-admin-interface

def niveau(request,id):
    
    # niveau = Test.objects.filter(exercice__id = id )
    exercice = Exercice.ojects.all()
    data={
        # 'niveau':niveau,
        'exercice':exercice,
    }

    return render(request, 'pages/niveau.html',data)