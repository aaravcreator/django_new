# Generated by Django 4.2.13 on 2024-06-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contactdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
