# Generated by Django 5.1.6 on 2025-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_myfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
