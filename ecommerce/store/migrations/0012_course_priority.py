# Generated by Django 5.0 on 2024-06-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_tutorial_module_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
