# Generated by Django 4.1.2 on 2022-10-30 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRF', '0008_alter_track_options_alter_track_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='draft',
        ),
    ]