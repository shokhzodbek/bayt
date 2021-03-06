# Generated by Django 3.2.4 on 2021-06-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0009_auto_20210616_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endvalue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autodate', models.DateTimeField(auto_now_add=True)),
                ('cashmoneys', models.IntegerField(blank=True, default=0, null=True)),
                ('plasticmoneys', models.IntegerField(blank=True, default=0, null=True)),
                ('accountnumbermoneys', models.IntegerField(blank=True, default=0, null=True)),
                ('dollars', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
