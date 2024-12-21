# Generated by Django 5.1.4 on 2024-12-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('dependants', models.PositiveBigIntegerField(null=True)),
                ('applicants_income', models.PositiveBigIntegerField(null=True)),
                ('coapplicants_income', models.PositiveBigIntegerField(null=True)),
                ('loan_amount', models.PositiveBigIntegerField(null=True)),
                ('credit_history', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('marital_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('education_status', models.CharField(choices=[('Graduated', 'Graduated'), ('Non_Graduate', 'Non_Graduate')], max_length=50, null=True)),
                ('self_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semi-Urban', 'Semi-Urban'), ('Urban', 'Urban')], max_length=100, null=True)),
                ('loan_status', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
