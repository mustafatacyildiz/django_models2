# Generated by Django 4.0.4 on 2022-05-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_framework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('frameworks', models.ManyToManyField(to='relations.framework')),
            ],
        ),
    ]
