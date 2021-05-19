# Generated by Django 3.2 on 2021-05-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20210508_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.Category'),
        ),
    ]
