# Generated by Django 4.0.3 on 2022-04-10 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CN',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='QUESTION ID')),
                ('question', models.CharField(max_length=1024, null=True, verbose_name='QUESTION')),
                ('A', models.CharField(max_length=128, null=True)),
                ('B', models.CharField(max_length=128, null=True)),
                ('C', models.CharField(max_length=128, null=True)),
                ('D', models.CharField(max_length=128, null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Correct Choice')),
                ('difficulty', models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1, verbose_name='Difficulty Level')),
            ],
            options={
                'verbose_name_plural': 'CN',
            },
        ),
        migrations.CreateModel(
            name='DBMS',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='QUESTION ID')),
                ('question', models.CharField(max_length=1024, null=True, verbose_name='QUESTION')),
                ('A', models.CharField(max_length=128, null=True)),
                ('B', models.CharField(max_length=128, null=True)),
                ('C', models.CharField(max_length=128, null=True)),
                ('D', models.CharField(max_length=128, null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Correct Choice')),
                ('difficulty', models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1, verbose_name='Difficulty Level')),
            ],
            options={
                'verbose_name_plural': 'DBMS',
            },
        ),
        migrations.CreateModel(
            name='JAVA',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='QUESTION ID')),
                ('question', models.CharField(max_length=1024, null=True, verbose_name='QUESTION')),
                ('A', models.CharField(max_length=128, null=True)),
                ('B', models.CharField(max_length=128, null=True)),
                ('C', models.CharField(max_length=128, null=True)),
                ('D', models.CharField(max_length=128, null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Correct Choice')),
                ('difficulty', models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1, verbose_name='Difficulty Level')),
            ],
            options={
                'verbose_name_plural': 'JAVA',
            },
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='QUESTION ID')),
                ('question', models.CharField(max_length=1024, null=True, verbose_name='QUESTION')),
                ('A', models.CharField(max_length=128, null=True)),
                ('B', models.CharField(max_length=128, null=True)),
                ('C', models.CharField(max_length=128, null=True)),
                ('D', models.CharField(max_length=128, null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Correct Choice')),
                ('difficulty', models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1, verbose_name='Difficulty Level')),
            ],
            options={
                'verbose_name_plural': 'OS',
            },
        ),
        migrations.CreateModel(
            name='PYTHON',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='QUESTION ID')),
                ('question', models.CharField(max_length=1024, null=True, verbose_name='QUESTION')),
                ('A', models.CharField(max_length=128, null=True)),
                ('B', models.CharField(max_length=128, null=True)),
                ('C', models.CharField(max_length=128, null=True)),
                ('D', models.CharField(max_length=128, null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Correct Choice')),
                ('difficulty', models.CharField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=1, max_length=1, verbose_name='Difficulty Level')),
            ],
            options={
                'verbose_name_plural': 'PYTHON',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('OS', 'OS'), ('DBMS', 'DBMS'), ('CN', 'CN')], default='JAVA', max_length=32, verbose_name='Subject')),
                ('score', models.PositiveIntegerField(default=0, verbose_name='Score')),
                ('date', models.DateField(auto_now=True)),
                ('responses', models.CharField(default='', max_length=256, verbose_name='Responses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Profiles.student')),
            ],
        ),
    ]
