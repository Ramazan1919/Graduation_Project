# Generated by Django 3.1.3 on 2020-12-31 10:45

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
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Port_Type', models.CharField(choices=[('Liman', 'Liman'), ('Sehir', 'Sehir'), ('Okyanus', 'Okyanus')], default='Liman', max_length=10)),
                ('name', models.CharField(max_length=25)),
                ('Continent', models.CharField(max_length=25)),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
