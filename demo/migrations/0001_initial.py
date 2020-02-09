# Generated by Django 3.0.1 on 2020-01-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demoer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('lead', models.CharField(max_length=50)),
                ('need_shadow', models.BooleanField()),
                ('three_pillar', models.BooleanField()),
                ('apm', models.BooleanField()),
                ('logs', models.BooleanField()),
                ('custom_metrics', models.BooleanField()),
                ('notes', models.CharField(max_length=250)),
                ('max_mrr', models.IntegerField(choices=[(1400, '1400'), (2500, '2500'), (3500, '3500'), (5000, '5000')])),
            ],
        ),
    ]