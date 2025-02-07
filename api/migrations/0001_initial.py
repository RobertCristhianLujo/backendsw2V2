# Generated by Django 5.1.3 on 2024-11-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clienteName', models.CharField(max_length=200)),
                ('clienteEmail', models.EmailField(blank=True, max_length=200, null=True)),
                ('clientePhone', models.CharField(blank=True, max_length=15, null=True)),
                ('clienteAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('clienteImage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productoName', models.CharField(max_length=200)),
                ('productoDescription', models.CharField(blank=True, max_length=200)),
                ('productoPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productoImage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
