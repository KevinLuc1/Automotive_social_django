# Generated by Django 3.0.3 on 2020-06-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replies', '0003_auto_20200621_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='last_clicked_pk',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
