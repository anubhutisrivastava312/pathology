# Generated by Django 4.0.6 on 2022-08-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Detail',
            fields=[
                ('Test_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Charge', models.IntegerField()),
                ('Test_Condition', models.CharField(max_length=100)),
            ],
        ),
    ]
