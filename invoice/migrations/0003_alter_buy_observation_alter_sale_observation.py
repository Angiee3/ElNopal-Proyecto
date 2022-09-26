# Generated by Django 4.0.3 on 2022-09-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_rename_provider_buy_user_buy_observation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='observation',
            field=models.CharField(choices=[('Devolución', 'Devolución'), ('Cambio', 'Cambio'), ('Otro', 'Otro')], max_length=15, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='observation',
            field=models.CharField(choices=[('Devolución', 'Devolución'), ('Cambio', 'Cambio'), ('Otro', 'Otro')], max_length=15, verbose_name='Observaciones'),
        ),
    ]
