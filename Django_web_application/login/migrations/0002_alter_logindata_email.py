# Generated by Django 4.1.10 on 2023-09-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
