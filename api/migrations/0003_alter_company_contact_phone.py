# Generated by Django 5.0.6 on 2024-06-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_company_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.IntegerField(),
        ),
    ]