# Generated by Django 3.2.8 on 2021-11-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hist_alt_carteira',
            name='operacao',
            field=models.CharField(blank=True, choices=[('C', 'Compra'), ('V', 'Venda')], help_text='Tipo de Operação', max_length=1),
        ),
    ]