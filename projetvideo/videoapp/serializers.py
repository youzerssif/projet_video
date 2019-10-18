from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import *


class User_moduleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User_module
        fields = '__all__'
        

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    modules = User_moduleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'
         
class VideoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'



class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # video_categorie = VideoSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Categorie
        fields = '__all__'


class ModuleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = Module
        fields = '__all__'


