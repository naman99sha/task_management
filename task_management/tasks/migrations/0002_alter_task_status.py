# Generated by Django 5.1.2 on 2024-10-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Completed', 'completed')], default='Pending', max_length=50),
        ),
    ]
