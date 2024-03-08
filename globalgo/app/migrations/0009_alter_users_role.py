# Generated by Django 5.0.2 on 2024-03-06 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.ForeignKey(db_column='role_id', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.role'),
        ),
    ]