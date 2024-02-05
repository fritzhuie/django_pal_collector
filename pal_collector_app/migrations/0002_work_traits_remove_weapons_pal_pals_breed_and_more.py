# Generated by Django 5.0.1 on 2024-02-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pal_collector_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pal_number', models.CharField(default='', max_length=6)),
                ('trait_kindling', models.IntegerField(default=0)),
                ('trait_planting', models.IntegerField(default=0)),
                ('trait_handiwork', models.IntegerField(default=0)),
                ('trait_lumbering', models.IntegerField(default=0)),
                ('trait_medicine', models.IntegerField(default=0)),
                ('trait_transporting', models.IntegerField(default=0)),
                ('trait_watering', models.IntegerField(default=0)),
                ('trait_generating', models.IntegerField(default=0)),
                ('trait_gathering', models.IntegerField(default=0)),
                ('trait_mining', models.IntegerField(default=0)),
                ('trait_cooling', models.IntegerField(default=0)),
                ('trait_farming', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='weapons',
            name='pal',
        ),
        migrations.AddField(
            model_name='pals',
            name='breed',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pals',
            name='element_1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pals',
            name='element_2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pals',
            name='food',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pals',
            name='pal_number',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='weapons',
            name='weapon_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pals',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.CreateModel(
            name='My_pals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(default='', max_length=60)),
                ('pal_number', models.CharField(default='', max_length=6)),
                ('weapon', models.ManyToManyField(to='pal_collector_app.weapons')),
            ],
        ),
    ]
