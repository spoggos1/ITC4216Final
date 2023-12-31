# Generated by Django 4.2.2 on 2023-07-21 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.CharField(max_length=100)),
                ('item_image', models.ImageField(blank=True, upload_to='uploads/')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemcategory', to='compware.category')),
                ('item_subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsubcategory', to='compware.subcategory')),
            ],
        ),
    ]
