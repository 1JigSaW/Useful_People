# Generated by Django 3.2.4 on 2021-07-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=50)),
                ('start_training', models.DateField()),
                ('end_training', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('years_of_work', models.IntegerField()),
                ('mounth_of_work', models.IntegerField()),
                ('photo_work', models.ImageField(upload_to='photo_works')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('university', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos')),
                ('additional_information', models.TextField()),
                ('achievements', models.ManyToManyField(to='people.Achievements')),
                ('additional_education', models.ManyToManyField(to='people.Education')),
                ('experience', models.ManyToManyField(to='people.Experience')),
                ('skills', models.ManyToManyField(to='people.Skills')),
            ],
        ),
    ]
