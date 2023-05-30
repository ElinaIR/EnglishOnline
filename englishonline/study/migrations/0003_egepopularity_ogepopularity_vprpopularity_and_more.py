# Generated by Django 4.2 on 2023-05-23 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0002_alter_userprofile_role_popularity'),
    ]

    operations = [
        migrations.CreateModel(
            name='EGEPopularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('ege_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.egevariant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OGEPopularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('oge_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.ogevariant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VPRPopularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vpr_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.vprvariant')),
            ],
        ),
        migrations.DeleteModel(
            name='Popularity',
        ),
    ]