# Generated by Django 5.2.1 on 2025-06-02 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_booking', '0007_remove_sport_club_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='club_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Club', to='app_booking.sportsclub'),
        ),
    ]
