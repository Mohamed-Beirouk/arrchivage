# Generated by Django 4.1.1 on 2022-09-20 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appel_offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('adresse', models.CharField(default='', editable=False, max_length=100)),
                ('poste', models.CharField(max_length=10)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Avis_passation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('poste', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Comptabilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Courrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='', editable=False, max_length=100)),
                ('receiver', models.CharField(default='', editable=False, max_length=100)),
                ('titre', models.CharField(default='', editable=False, max_length=100)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('objet', models.TextField(default='', editable=False, max_length=400)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=10)),
                ('sexe', models.CharField(max_length=10)),
                ('image', models.ImageField(default='', null=True, upload_to='static/')),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('adresse', models.CharField(default='', editable=False, max_length=100)),
                ('poste', models.CharField(max_length=10)),
                ('date_n', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ppm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='Ordre_mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('objet', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now_add=True)),
                ('localisation', models.CharField(default='', editable=False, max_length=100)),
                ('file', models.FileField(upload_to='static/')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('description', models.TextField(default='', editable=False, max_length=400)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now_add=True)),
                ('salaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file', models.FileField(upload_to='static/')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(default='', editable=False, max_length=100)),
                ('reference', models.CharField(default='', editable=False, max_length=100)),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='static/')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.employee')),
            ],
        ),
    ]
