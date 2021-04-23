# Generated by Django 3.2 on 2021-04-23 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='coach_id',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='email',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='name',
        ),
        migrations.AddField(
            model_name='coach',
            name='coach',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coach',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
