# Generated by Django 3.0.4 on 2020-03-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='advices',
            field=models.ManyToManyField(to='app.Advice'),
        ),
    ]