# Generated by Django 2.1.7 on 2019-02-24 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]