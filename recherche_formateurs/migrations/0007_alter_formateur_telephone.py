# Generated by Django 3.2.16 on 2024-04-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recherche_formateurs', '0006_formateur_national'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formateur',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
