# Generated by Django 5.0.1 on 2024-02-05 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pal_collector_app', '0002_work_traits_remove_weapons_pal_pals_breed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_cooling',
            new_name='cooling',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_farming',
            new_name='farming',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_gathering',
            new_name='gathering',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_generating',
            new_name='generating',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_handiwork',
            new_name='handiwork',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_kindling',
            new_name='kindling',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_lumbering',
            new_name='lumbering',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_medicine',
            new_name='medicine',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_mining',
            new_name='mining',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_planting',
            new_name='planting',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_transporting',
            new_name='transporting',
        ),
        migrations.RenameField(
            model_name='work_traits',
            old_name='trait_watering',
            new_name='watering',
        ),
    ]
