# Generated by Django 5.0.2 on 2024-03-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(choices=[('Facilitator', 'Facilitator'), ('Student', 'Student'), ('Staff', 'Staff')], max_length=12),
        ),
    ]
