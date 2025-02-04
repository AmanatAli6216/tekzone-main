# Generated by Django 4.2.6 on 2023-10-20 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0005_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posApp.supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='suppliername',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
