# Generated by Django 3.2 on 2021-05-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker_tracker',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
