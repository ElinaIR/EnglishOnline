# Generated by Django 4.2 on 2023-05-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_remove_mark_card_alter_card_last_wrong_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
