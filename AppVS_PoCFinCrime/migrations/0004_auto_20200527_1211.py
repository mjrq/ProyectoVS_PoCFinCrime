# Generated by Django 2.2.12 on 2020-05-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVS_PoCFinCrime', '0003_auto_20200527_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='BALANCE_DATE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
