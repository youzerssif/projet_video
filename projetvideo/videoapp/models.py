from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Module(models.Model):

    titre = models.CharField(max_length=150)
    jeton = models.PositiveIntegerField()
    image = models.ImageField( upload_to='images/module/', blank=True, null=True)
    prix = models.FloatField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_update = models.DateTimeField(auto_now=False,)

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.titre
    

class Categorie(models.Model):
    """Model definition for Categorie."""

    titre = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField()
    image = models.ImageField( upload_to='images/categorie/', blank=True, null=True)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_update = models.DateTimeField(auto_now=False,)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.titre



class Video(models.Model):
    """Model definition for Video."""

    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='video_categorie')
    titre = models.CharField(max_length=150)
    description = models.TextField()
    video = models.URLField()
    image = models.ImageField( upload_to='images/categorie/', blank=True, null=True)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_update = models.DateTimeField(auto_now=False,)

    class Meta:
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        """Unicode representation of Video."""
        return self.titre

class User_module(models.Model):
    """Model definition for User_module."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modules')
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='users')
    jeton = models.PositiveIntegerField()
    apikey = models.CharField(max_length=225,null=True)
    jeton_restant = models.PositiveIntegerField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_update = models.DateTimeField(auto_now=False,)

    class Meta:
        """Meta definition for User_module."""

        verbose_name = 'User_module'
        verbose_name_plural = 'User_modules'


