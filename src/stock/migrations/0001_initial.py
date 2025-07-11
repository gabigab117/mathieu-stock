# Generated by Django 5.2 on 2025-07-07 13:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='order.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('in_stock', models.IntegerField(verbose_name='Quantity')),
                ('in_transit', models.IntegerField(verbose_name='In transit')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='order.company', verbose_name='Company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='catalog.product', verbose_name='Product')),
            ],
            options={
                'indexes': [models.Index(fields=['company', 'product'], name='stock_inven_company_413ffe_idx')],
                'unique_together': {('company', 'product')},
            },
        ),
    ]
