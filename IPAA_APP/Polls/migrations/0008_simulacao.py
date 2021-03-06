# Generated by Django 3.2.8 on 2021-11-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0007_alter_usuario_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Informe o nome da simulação', max_length=100)),
                ('descricao', models.CharField(help_text='Informe a descrição da simulação', max_length=300, null=True)),
                ('data_inicial', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
            ],
        ),
    ]
