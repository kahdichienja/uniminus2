# Generated by Django 2.1.7 on 2020-08-11 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_qualifications_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_letter', models.FileField(upload_to='admletters')),
                ('birth_cert', models.FileField(upload_to='birthcert')),
                ('kcse_cert', models.FileField(upload_to='kcsecert')),
                ('result_slip', models.FileField(upload_to='resultslip')),
                ('national_id', models.FileField(blank=True, null=True, upload_to='nationalid')),
                ('sec_leaving_cert', models.FileField(blank=True, null=True, upload_to='leavingcert')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]