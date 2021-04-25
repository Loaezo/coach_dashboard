# Generated by Django 3.2 on 2021-04-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='role',
            field=models.CharField(choices=[('Tech Coach', 'Tech Coach'), ('Academic Coach', 'Academic Coach'), ('Talent Placement Coach', 'Talent Placement Coach')], max_length=100),
        ),
    ]
