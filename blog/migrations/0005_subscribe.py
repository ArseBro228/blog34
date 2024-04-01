# Generated by Django 5.0.2 on 2024-03-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, verbose_name='Пошта для розсилки')),
            ],
            options={
                'verbose_name': 'Підписка',
                'verbose_name_plural': 'Підписки',
            },
        ),
    ]
