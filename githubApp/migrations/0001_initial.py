# Generated by Django 2.1.3 on 2018-11-22 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gitUser',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='links',
            fields=[
                ('link_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('linkTo', models.PositiveIntegerField()),
            ],
        ),
    ]
