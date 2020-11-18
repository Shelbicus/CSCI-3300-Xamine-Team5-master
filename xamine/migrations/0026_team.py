# Generated by Django 3.0.5 on 2020-04-18 02:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xamine', '0025_auto_20200417_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('radiologists', models.ManyToManyField(blank=True, related_name='radiol_teams', to=settings.AUTH_USER_MODEL)),
                ('technicians', models.ManyToManyField(blank=True, related_name='tech_teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
