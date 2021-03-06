# Generated by Django 2.2.6 on 2019-11-16 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Courss',
            },
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('code_depart', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Exercice',
                'verbose_name_plural': 'Exercices',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Niveau',
                'verbose_name_plural': 'Niveaus',
            },
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='specialite/image')),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('id_specialite', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Specialite',
                'verbose_name_plural': 'Specialites',
            },
        ),
        migrations.CreateModel(
            name='UserSpecialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialiteuser', to='editor.Specialite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specialite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserSpecialite',
                'verbose_name_plural': 'UserSpecialites',
            },
        ),
        migrations.CreateModel(
            name='TestValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_test', models.TextField()),
                ('resultat', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicetest', to='editor.Exercice')),
            ],
            options={
                'verbose_name': 'TestValidation',
                'verbose_name_plural': 'TestValidations',
            },
        ),
        migrations.CreateModel(
            name='ResultatExercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_tentative', models.PositiveIntegerField()),
                ('code', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciceresultat', to='editor.Exercice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userresultat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ResultatExercice',
                'verbose_name_plural': 'ResultatExercices',
            },
        ),
        migrations.CreateModel(
            name='ResultatCompo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='niveauresultatcompo', to='editor.Niveau')),
                ('resultat_exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultexoresultcompo', to='editor.ResultatExercice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultatcompouser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ResultatCompo',
                'verbose_name_plural': 'ResultatCompos',
            },
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('types', models.CharField(max_length=255)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursressources', to='editor.Cours')),
            ],
            options={
                'verbose_name': 'Ressources',
                'verbose_name_plural': 'Ressources',
            },
        ),
        migrations.AddField(
            model_name='niveau',
            name='specialite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialiteniveau', to='editor.Specialite'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='niveauexercice', to='editor.Niveau'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='specialite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialiteexercice', to='editor.Specialite'),
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='niveaucours', to='editor.Niveau'),
        ),
        migrations.AddField(
            model_name='cours',
            name='specialite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialitecours', to='editor.Specialite'),
        ),
    ]
