# Generated by Django 5.1.4 on 2024-12-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_alter_approvals_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvals',
            name='loan_term',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
