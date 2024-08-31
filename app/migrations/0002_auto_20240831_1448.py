# Generated by Django 3.2.24 on 2024-08-31 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitemdamage',
            options={'verbose_name': 'Sistema de Alerta', 'verbose_name_plural': 'Sistemas de Alertas'},
        ),
        migrations.CreateModel(
            name='sistemSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sistema', to='app.sitemdamage')),
            ],
        ),
    ]
