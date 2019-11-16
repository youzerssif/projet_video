from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class Specialite(models.Model):
    """Model definition for Specialite."""
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="specialite/image")
    description = HTMLField('description')
    id_specialite = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Specialite."""

        verbose_name = 'Specialite'
        verbose_name_plural = 'Specialites'

    def __str__(self):
        """Unicode representation of Specialite."""
        return '{}'.format(self.nom ) # TODO


class UserSpecialite(models.Model):
    """Model definition for UserSpecialite."""
    user = models.ForeignKey(User,related_name='user_specialite',on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='specialiteuser')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for UserSpecialite."""

        verbose_name = 'UserSpecialite'
        verbose_name_plural = 'UserSpecialites'

    def __str__(self):
        """Unicode representation of UserSpecialite."""
        return '{}'.format(self.specialite ) # TODO

class Niveau(models.Model):
    """Model definition for Niveau."""

    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='specialiteniveau')
    nom = models.CharField(max_length=255)
    description = HTMLField('description')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Niveau."""

        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveaus'

    def __str__(self):
        """Unicode representation of Niveau."""
        return '{}'.format(self.nom ) # TODO


class Cours(models.Model):
    """Model definition for Cours."""

    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE,related_name='niveaucours')
    titre = models.CharField(max_length=255)
    description = HTMLField('description')
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='specialitecours')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Cours."""

        verbose_name = 'Cours'
        verbose_name_plural = 'Courss'

    def __str__(self):
        """Unicode representation of Cours."""
        return '{}'.format(self.titre) # TODO
    
    
class Ressources(models.Model):
    """Model definition for Ressources."""

    cours = models.ForeignKey(Cours, on_delete=models.CASCADE,related_name='coursressources')
    link = models.URLField()
    types = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Ressources."""

        verbose_name = 'Ressources'
        verbose_name_plural = 'Ressources'

    def __str__(self):
        """Unicode representation of Ressources."""
        return '{}'.format(self.cours) # TODO

    
class Exercice(models.Model):
    """Model definition for Exercice."""

    titre = models.CharField(max_length=255)
    description = HTMLField('description')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,related_name='niveauexercice')
    code_depart = models.TextField()
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='specialiteexercice')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Exercice."""

        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'

    def __str__(self):
        """Unicode representation of Exercice."""
        return '{}'.format(self.titre ) # TODO

class TestValidation(models.Model):
    """Model definition for TestValidation."""

    code_test = models.TextField()
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE,related_name='exercicetest')
    resultat = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TestValidation."""

        verbose_name = 'TestValidation'
        verbose_name_plural = 'TestValidations'

    def __str__(self):
        """Unicode representation of TestValidation."""
        return '{}'.format(self.resultat ) # TODO

class ResultatExercice(models.Model):
    """Model definition for ResultatExercice."""

    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE,related_name='exerciceresultat')
    nb_tentative = models.PositiveIntegerField()
    code = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userresultat')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for ResultatExercice."""

        verbose_name = 'ResultatExercice'
        verbose_name_plural = 'ResultatExercices'

    def __str__(self):
        """Unicode representation of ResultatExercice."""
        return '{}'.format(self.user ) # TODO

class ResultatCompo(models.Model):
    """Model definition for ResultatCompo."""

    resultat_exercice = models.ForeignKey(ResultatExercice, on_delete=models.CASCADE,related_name='resultexoresultcompo')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,related_name='niveauresultatcompo')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='resultatcompouser')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for ResultatCompo."""

        verbose_name = 'ResultatCompo'
        verbose_name_plural = 'ResultatCompos'

    def __str__(self):
        """Unicode representation of ResultatCompo."""
        return '{}'.format(self.user ) # TODO

