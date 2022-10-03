# Generated by Django 4.1.1 on 2022-10-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_appel_offre_adresse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='passation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=100)),
                ('numeromarche', models.TextField(max_length=400)),
                ('reference', models.CharField(max_length=100)),
                ('financement', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
    ]
