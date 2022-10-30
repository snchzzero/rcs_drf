# Generated by Django 4.1.2 on 2022-10-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRF', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='track',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('album', 'order')},
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]