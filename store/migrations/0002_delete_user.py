# Generated by Django 4.0.4 on 2022-10-03 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_remove_sale_username'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
