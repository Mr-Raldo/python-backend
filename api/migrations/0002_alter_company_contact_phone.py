# Generated by Django 5.0.6 on 2024-06-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.IntegerField(max_length=10),
        ),
    ]