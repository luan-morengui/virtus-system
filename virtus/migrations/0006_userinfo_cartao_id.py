# Generated by Django 5.0.6 on 2024-12-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtus', '0005_userinfo_cargo_userinfo_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='cartao_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]