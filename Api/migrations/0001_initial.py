# Generated by Django 3.2.4 on 2021-06-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commonName', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=10)),
                ('fifa_id', models.CharField(max_length=10)),
            ],
        ),
    ]
