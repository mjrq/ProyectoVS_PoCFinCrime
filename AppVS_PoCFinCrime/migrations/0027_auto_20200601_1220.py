# Generated by Django 2.2.12 on 2020-06-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVS_PoCFinCrime', '0026_auto_20200601_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='ACCOUNT_PURPOSE',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='COLLECTED_BALANCE',
            field=models.FloatField(null=True),
        ),
    ]
