# Generated by Django 3.2 on 2021-05-27 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0006_alter_worker_tracker_started_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker_tracker',
            old_name='running',
            new_name='running_status',
        ),
    ]
