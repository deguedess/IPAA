# Generated by Django 3.2.8 on 2021-11-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0013_merge_0008_simulacao_0012_delete_simulacao_cenario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='sequencia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
