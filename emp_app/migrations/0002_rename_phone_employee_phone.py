# Generated by Django 4.1.7 on 2023-04-10 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Phone',
            new_name='phone',
        ),
    ]
