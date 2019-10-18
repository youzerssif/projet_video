from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe


from . import models


class ModuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'jeton',
        'prix',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = ('status', 'date_add', 'date_update')


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'status',
        'image_view',
        'date_add',
        'date_update',
    )
    list_filter = ('status', 'date_add', 'date_update')
    
    def image_view(self, obj):
        return mark_safe('<img src="{url}"  width="100px" heigth="50px" /> '.format(url=obj.image.url))


class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'titre',
        'description',
        'video_view',
        'image',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = ('status', 'date_add', 'date_update')
    raw_id_fields = ('categorie',)
    
    

    def video_view(self, obj):
        return mark_safe('<video controls width="250"> <source src="{url}" type="video/mp4"> lecteur </video>'.format(url=obj.video.url))

class User_moduleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'module',
        'jeton',
        'apikey',
        'jeton_restant',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = ('status', 'date_add', 'date_update')
    raw_id_fields = ('user', 'module')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Module, ModuleAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Video, VideoAdmin)
_register(models.User_module, User_moduleAdmin)
