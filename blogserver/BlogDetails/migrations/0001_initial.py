# Generated by Django 3.1.5 on 2021-01-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('TopicName', models.CharField(max_length=100, unique=True)),
                ('Image', models.CharField(max_length=100, unique=True)),
                ('TopicDescription', models.CharField(max_length=2000, unique=True)),
                ('CreationTime', models.DateField()),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
