# Generated by Django 2.2.12 on 2020-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVS_PoCFinCrime', '0013_auto_20200527_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='ACCOUNT_ON_HOLD_FLAG',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='ORIGINATION_DATE',
            field=models.DateField(blank=True, null=True),
        ),
    ]
