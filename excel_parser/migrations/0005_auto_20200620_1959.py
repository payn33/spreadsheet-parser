# Generated by Django 3.0.7 on 2020-06-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_parser', '0004_auto_20200620_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='MDA_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='budget',
            name='project_recipient_name',
            field=models.CharField(max_length=120),
        ),
    ]
