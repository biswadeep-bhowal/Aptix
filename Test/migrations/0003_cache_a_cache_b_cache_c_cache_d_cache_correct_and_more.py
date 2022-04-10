# Generated by Django 4.0.3 on 2022-04-10 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_cache'),
    ]

    operations = [
        migrations.AddField(
            model_name='cache',
            name='A',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='cache',
            name='B',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='cache',
            name='C',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='cache',
            name='D',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='cache',
            name='correct',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='cache',
            name='difficulty',
            field=models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='cache',
            name='qno',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cache',
            name='question',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
