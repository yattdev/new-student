# Generated by Django 4.1.7 on 2023-04-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_agent_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='slug',
            field=models.CharField(default='', max_length=255),
        ),
    ]