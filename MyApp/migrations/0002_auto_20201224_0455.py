# Generated by Django 3.1.3 on 2020-12-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='presence_num',
            field=models.IntegerField(),
        ),
    ]
