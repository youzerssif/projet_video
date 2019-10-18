from rest_framework import viewsets,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json


from .models import *
from .serializers import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class User_moduleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = User_module.objects.all()
    serializer_class = User_moduleSerializer

class VideosListe(APIView):
    def get(self, request):
        # print("#############",request.headers)
        print("##########",request.GET.get('key'))
        print("User    ##########",request.user)
        myUser=request.headers.get('User-Agent')
    
        videos = Video.objects.all()
        data = VideoSerializer(videos, many=True).data
        return Response(data)
# class VideoViewSet(viewsets.ModelViewSet):
#     filter_backends = (DynamicSearchFilter,)
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

class VideoDetail(APIView):
    def get(self, request, pk):
        apikey = request.GET.get('key')
        print(apikey)
        isSucces = False
        message = ''
        try:
            req = User_module.objects.filter(apikey=apikey)[:1].get()
            jeton = req.jeton_restant
            if jeton > 0:
                nouveau = jeton-1
                req.jeton_restant = nouveau
                req.save()
                isSucces = True
            else:
                isSucces = False
                message = 'Votre jeton est epuisé'
        except:
            isSucces = False
            message = 'Jeton incorrect'
            
        if isSucces:
            video = get_object_or_404(Video, pk=pk)
            data = VideoSerializer(video).data
        else:
            data = {
                'error': True,
                'message':message
            }
        # print("##########",request.GET.get('key'))
        # print("User    ##########",request.user)
        
        
       
        return Response(data)

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
class ModuleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer