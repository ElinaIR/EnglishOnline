# Generated by Django 4.2 on 2023-05-18 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_alter_card_last_wrong_alter_card_next_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, 'Student'), (1, 'Teacher')], default=(0, 'Student'))),
                ('decks', models.ManyToManyField(to='cards.deck')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
