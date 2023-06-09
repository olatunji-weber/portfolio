# Generated by Django 4.2 on 2023-04-10 23:42

from django.db import migrations, models
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='course',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='date',
            new_name='endDate',
        ),
        migrations.AddField(
            model_name='education',
            name='fieldOfStudy',
            field=models.CharField(default='Computer Science', max_length=256),
        ),
        migrations.AddField(
            model_name='education',
            name='startDate',
            field=models.DateField(default=date(2007, 9, 7)),
            preserve_default=False,
        ),
    ]
