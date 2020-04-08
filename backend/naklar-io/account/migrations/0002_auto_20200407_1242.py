# Generated by Django 3.0.5 on 2020-04-07 10:42

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('MA', 'männlich'), ('FE', 'weiblich'), ('DI', 'divers')], default='', max_length=2, verbose_name='Geschlecht'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutordata',
            name='verification_file',
            field=models.FileField(null=True, upload_to=account.models.tutor_upload_path, verbose_name='Vefizierungsdatei'),
        ),
        migrations.AddField(
            model_name='tutordata',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Verifiziert'),
        ),
    ]
