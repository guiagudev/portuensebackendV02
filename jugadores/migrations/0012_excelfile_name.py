# Generated by Django 5.1.6 on 2025-03-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0011_foldergroup_excelfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelfile',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
