# Generated by Django 4.0.3 on 2022-04-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
        ('Test', '0002_alter_cn_options_alter_dbms_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Result',
        ),
    ]