# Generated by Django 4.1.7 on 2023-04-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_agent_options_alter_guest_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='slug',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
