# Generated by Django 3.2 on 2021-05-21 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_alter_portfolio_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='ticker',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='charts.stocks', unique=True),
        ),
    ]