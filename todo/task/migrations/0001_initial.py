# Generated by Django 2.2 on 2021-10-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'todo'), (1, 'in_progress'), (2, 'complete')], default=0)),
            ],
        ),
    ]
