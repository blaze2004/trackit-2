# Generated by Django 4.0 on 2022-10-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shesh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereport',
            name='slug',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
