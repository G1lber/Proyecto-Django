# Generated by Django 5.1.3 on 2025-02-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
