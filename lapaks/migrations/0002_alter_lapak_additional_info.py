# Generated by Django 3.2.13 on 2022-06-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapaks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lapak',
            name='additional_info',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]