# Generated by Django 4.1.2 on 2022-10-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRF', '0002_alter_track_options_remove_album_artist_track_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='order',
            field=models.IntegerField(),
        ),
    ]