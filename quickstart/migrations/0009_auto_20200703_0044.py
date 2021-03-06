# Generated by Django 3.0.8 on 2020-07-03 00:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_auto_20200702_2000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.AddField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
