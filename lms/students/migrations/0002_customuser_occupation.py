# Generated by Django 5.0.2 on 2024-03-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
