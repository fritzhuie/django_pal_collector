# Generated by Django 5.0.1 on 2024-02-05 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pal_collector_app', '0003_rename_trait_cooling_work_traits_cooling_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pals',
            name='breed',
        ),
    ]