from rest_framework import viewsets,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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