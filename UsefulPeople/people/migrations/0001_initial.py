# Generated by Django 3.2.4 on 2021-10-28 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_c', models.CharField(choices=[('D', 'Dialog'), ('C', 'Chat')], default='D', max_length=1)),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=50)),
                ('start_training', models.DateField()),
                ('end_training', models.DateField()),
                ('photo_education', models.ImageField(upload_to='static/photo_education')),
            ],
            options={
                'verbose_name': 'Дополнительное образование',
                'verbose_name_plural': 'Дополнительные образования',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('years_of_work', models.IntegerField()),
                ('mounth_of_work', models.IntegerField()),
                ('photo_work', models.ImageField(upload_to='static/photo_works')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работ',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('university', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='static/photos')),
                ('additional_information', models.TextField()),
                ('achievements', models.ManyToManyField(to='people.Achievements')),
                ('additional_education', models.ManyToManyField(to='people.Education')),
                ('experience', models.ManyToManyField(to='people.Experience')),
                ('skills', models.ManyToManyField(to='people.Skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_readed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.useraccount')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.chat')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['pub_date'],
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(to='people.UserAccount'),
        ),
    ]
