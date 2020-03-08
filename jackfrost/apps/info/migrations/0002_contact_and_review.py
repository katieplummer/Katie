# Generated by Django 2.2.4 on 2020-03-07 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_carouselimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, null=True)),
                ('stars', models.FloatField(blank=True, default=0.0, null=True)),
                ('date_posted', models.DateTimeField(blank=True, default=None, null=True)),
                ('message', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]