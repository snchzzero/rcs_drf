# Generated by Django 4.1.2 on 2022-10-30 17:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1700), django.core.validators.MaxValueValidator(2030)])),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='DRF.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='DRF.album')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('album', 'order')},
            },
        ),
    ]
