from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'description',
        'id_specialite',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'image',
        'description',
        'id_specialite',
        'status',
        'date_add',
        'date_upd',
    )


class UserSpecialiteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'specialite',
        'status',
        'date_add',
        'date_upd',
        'id',
        'user',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )


class NiveauAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'specialite',
        'nom',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'specialite',
        'status',
        'date_add',
        'date_upd',
        'id',
        'specialite',
        'nom',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class CoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'niveau',
        'titre',
        'description',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'niveau',
        'specialite',
        'status',
        'date_add',
        'date_upd',
        'id',
        'niveau',
        'titre',
        'description',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )


class RessourcesAdmin(admin.ModelAdmin):

    list_display = ('id', 'cours', 'link', 'types')
    list_filter = ('cours', 'id', 'cours', 'link', 'types')


class ExerciceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'niveau',
        'code_depart',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'niveau',
        'specialite',
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'niveau',
        'code_depart',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )


class TestValidationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'code_test',
        'exercice',
        'resultat',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'exercice',
        'status',
        'date_add',
        'date_upd',
        'id',
        'code_test',
        'exercice',
        'resultat',
        'status',
        'date_add',
        'date_upd',
    )


class ResultatExerciceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'exercice',
        'nb_tentative',
        'code',
        'user',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'exercice',
        'user',
        'status',
        'date_add',
        'date_upd',
        'id',
        'exercice',
        'nb_tentative',
        'code',
        'user',
        'status',
        'date_add',
        'date_upd',
    )


class ResultatCompoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'resultat_exercice',
        'niveau',
        'user',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'resultat_exercice',
        'niveau',
        'user',
        'status',
        'date_add',
        'date_upd',
        'id',
        'resultat_exercice',
        'niveau',
        'user',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Specialite, SpecialiteAdmin)
_register(models.UserSpecialite, UserSpecialiteAdmin)
_register(models.Niveau, NiveauAdmin)
_register(models.Cours, CoursAdmin)
_register(models.Ressources, RessourcesAdmin)
_register(models.Exercice, ExerciceAdmin)
_register(models.TestValidation, TestValidationAdmin)
_register(models.ResultatExercice, ResultatExerciceAdmin)
_register(models.ResultatCompo, ResultatCompoAdmin)
