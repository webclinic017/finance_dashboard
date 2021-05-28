# Generated by Django 3.2 on 2021-05-21 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_auto_20210521_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='id',
            field=models.BigAutoField(auto_created=True, default=999, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.stocks'),
        ),
    ]