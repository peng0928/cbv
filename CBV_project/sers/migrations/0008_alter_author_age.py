# Generated by Django 3.2.13 on 2022-06-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sers', '0007_auto_20220613_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(),
        ),
    ]
