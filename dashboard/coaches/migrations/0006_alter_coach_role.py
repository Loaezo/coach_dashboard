# Generated by Django 3.2 on 2021-04-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0005_alter_coach_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='role',
            field=models.CharField(choices=[('Talent Placement Coach', 'Talent Placement Coach'), ('Tech Coach', 'Tech Coach'), ('Academic Coach', 'Academic Coach')], max_length=100),
        ),
    ]
