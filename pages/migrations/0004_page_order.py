# Generated by Django 5.1.3 on 2025-02-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden'),
        ),
    ]
