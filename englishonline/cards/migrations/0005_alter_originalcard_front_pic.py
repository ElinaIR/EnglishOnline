# Generated by Django 4.2 on 2023-05-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_attempt_user_alter_card_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalcard',
            name='front_pic',
            field=models.FileField(blank=True, upload_to='cards/pictures/'),
        ),
    ]
