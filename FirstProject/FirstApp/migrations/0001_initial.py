# Generated by Django 3.0.6 on 2020-06-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Eid', models.CharField(max_length=8)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
    ]
