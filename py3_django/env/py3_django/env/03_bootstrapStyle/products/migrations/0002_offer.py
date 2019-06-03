# Generated by Django 2.2 on 2019-06-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
