# Generated by Django 3.2.4 on 2021-10-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='first_name_u',
            field=models.CharField(default='sd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name_u',
            field=models.CharField(default='sd', max_length=50),
            preserve_default=False,
        ),
    ]
