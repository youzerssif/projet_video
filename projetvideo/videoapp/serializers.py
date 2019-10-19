from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
import simplejson as json

from .models import *

class VideoListingField(serializers.RelatedField):
    def to_representation(self, value):
        data= {
            'id': value.id ,
            'titre': value.titre,
            'description': value.description,
            'image': value.image.url
            }
        #duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return data

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

    video_categorie = VideoListingField(many=True, read_only=True, required=False)

    class Meta:
        model = Categorie
        fields = '__all__'


class ModuleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = Module
        fields = '__all__'


