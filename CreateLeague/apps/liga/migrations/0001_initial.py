# Generated by Django 4.1.3 on 2023-02-25 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, verbose_name='Fecha eliminación')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_equipos', models.IntegerField(blank=True, default=0)),
                ('formato', models.IntegerField(choices=[(0, 'LIGUILLA'), (1, 'ELIMINACIÓN DIRECTA'), (2, 'COPA')], default=0)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Modelo base',
                'verbose_name_plural': 'Modelos base',
                'abstract': False,
            },
        ),
    ]
