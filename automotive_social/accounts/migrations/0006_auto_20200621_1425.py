# Generated by Django 3.0.3 on 2020-06-21 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_last_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='last_location',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
