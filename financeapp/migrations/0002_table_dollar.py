# Generated by Django 3.2.4 on 2021-06-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='dollar',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
