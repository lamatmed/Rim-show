# Generated by Django 5.0.6 on 2024-07-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='100', max_length=300),
            preserve_default=False,
        ),
    ]
