# Generated by Django 3.0.8 on 2020-07-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=120)),
                ('answer', models.TextField()),
            ],
        ),
    ]
