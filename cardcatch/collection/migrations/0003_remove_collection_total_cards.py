# Generated by Django 5.0.6 on 2024-06-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_alter_entry_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='total_cards',
        ),
    ]