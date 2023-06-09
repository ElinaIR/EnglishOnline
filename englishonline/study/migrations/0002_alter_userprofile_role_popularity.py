# Generated by Django 4.2 on 2023-05-18 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(choices=[(0, 'Student'), (1, 'Teacher')], default=(0, 'Student')),
        ),
        migrations.CreateModel(
            name='Popularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_type', models.CharField(choices=[('ege', 'ЕГЭ'), ('oge', 'ОГЭ'), ('vpr', 'ВПР')], max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('ege_variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.egevariant')),
                ('oge_variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.ogevariant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vpr_variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.vprvariant')),
            ],
        ),
    ]
