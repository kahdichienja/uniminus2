# Generated by Django 2.1.7 on 2020-08-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200809_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='birth_cert_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='ethinicity',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='id_passport_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='physicaly_impaired',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
