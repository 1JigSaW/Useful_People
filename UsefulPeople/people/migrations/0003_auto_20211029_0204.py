# Generated by Django 3.2.8 on 2021-10-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20211028_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='photo_education',
            field=models.ImageField(blank=True, null=True, upload_to='static/photo_education'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='photo_work',
            field=models.ImageField(blank=True, null=True, upload_to='static/photo_works'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='achievements',
            field=models.ManyToManyField(blank=True, to='people.Achievements'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='additional_education',
            field=models.ManyToManyField(blank=True, to='people.Education'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='experience',
            field=models.ManyToManyField(blank=True, to='people.Experience'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='skills',
            field=models.ManyToManyField(blank=True, to='people.Skills'),
        ),
    ]
