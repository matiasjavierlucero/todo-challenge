# Generated by Django 2.2 on 2021-10-20 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='desc',
            new_name='description',
        ),
    ]
