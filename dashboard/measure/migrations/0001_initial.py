# Generated by Django 4.1.6 on 2023-02-13 15:45

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
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('measure_year', models.IntegerField()),
                ('population', models.TextField()),
                ('exclusions', models.TextField()),
                ('denominator', models.TextField()),
                ('numerator', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
