# Generated by Django 4.0.6 on 2022-07-20 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfc_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nfc_details',
            old_name='lattitude',
            new_name='latitude',
        ),
    ]