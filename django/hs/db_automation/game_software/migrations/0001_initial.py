# Generated by Django 5.1.4 on 2025-01-07 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSoftware',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'game_software',
            },
        ),
        migrations.CreateModel(
            name='GameSoftwareDescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('gameSoftware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='game_software.gamesoftware')),
            ],
            options={
                'db_table': 'game_software_description',
            },
        ),
        migrations.CreateModel(
            name='GameSoftwareImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=100, null=True)),
                ('gameSoftware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='game_software.gamesoftware')),
            ],
            options={
                'db_table': 'game_software_image',
            },
        ),
        migrations.CreateModel(
            name='GameSoftwarePrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('gameSoftware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='game_software.gamesoftware')),
            ],
            options={
                'db_table': 'game_software_price',
            },
        ),
    ]