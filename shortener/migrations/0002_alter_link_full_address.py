# Generated by Django 4.1.7 on 2023-03-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='full_address',
            field=models.TextField(),
        ),
    ]
