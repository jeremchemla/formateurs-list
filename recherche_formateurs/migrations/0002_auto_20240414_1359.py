# Generated by Django 3.2.16 on 2024-04-14 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recherche_formateurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='secteur',
            name='code_postal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
    model_name='secteur',
    name='region',
    field=models.ForeignKey(default='ile de france', on_delete=django.db.models.deletion.CASCADE, related_name='secteurs', to='recherche_formateurs.Region'),
    preserve_default=False,
),
    ]
