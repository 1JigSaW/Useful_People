# Generated by Django 3.2.4 on 2021-10-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20211025_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='photo_education',
            field=models.ImageField(upload_to='static/photo_education'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='photo_work',
            field=models.ImageField(upload_to='static/photo_works'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='photo',
            field=models.ImageField(upload_to='static/photos'),
        ),
    ]