# Generated by Django 4.2 on 2023-05-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_rename_ege_variant_egepopularity_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(choices=[(0, 'Student'), (1, 'Teacher')], default=0),
        ),
    ]
