# Generated by Django 4.1.4 on 2022-12-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3000, verbose_name='Название')),
                ('text', models.CharField(max_length=100000, verbose_name='Текст')),
                ('img', models.ImageField(upload_to='img/')),
                ('pub_date', models.DateTimeField(verbose_name='дата публиккации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
