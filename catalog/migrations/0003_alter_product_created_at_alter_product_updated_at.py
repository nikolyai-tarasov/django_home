# Generated by Django 5.1.2 on 2024-10-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]