# Generated by Django 2.2.4 on 2020-03-07 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_event_and_event_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date']},
        ),
    ]