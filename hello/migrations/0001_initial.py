# Generated by Django 4.1.9 on 2023-06-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('position', models.CharField(default='', max_length=50, null=True)),
                ('created_at', models.CharField(default='', max_length=50, null=True)),
                ('updated_at', models.CharField(default='', max_length=50, null=True)),
                ('width', models.CharField(default='', max_length=50, null=True)),
                ('height', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('position', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('body_html', models.CharField(default='', max_length=100, null=True)),
                ('vendor', models.CharField(default='', max_length=100, null=True)),
                ('created_at', models.CharField(default='', max_length=100, null=True)),
                ('handle', models.CharField(default='', max_length=100, null=True)),
                ('updated_at', models.CharField(default='', max_length=100, null=True)),
                ('published_at', models.CharField(default='', max_length=100, null=True)),
                ('template_suffix', models.CharField(default='', max_length=100, null=True)),
                ('status', models.CharField(default='', max_length=100, null=True)),
                ('published_scope', models.CharField(default='', max_length=100, null=True)),
                ('tags', models.CharField(default='', max_length=100, null=True)),
                ('admin_graphql_api_id', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compare_at_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inventory_management', models.CharField(default='', max_length=255, null=True)),
                ('option1', models.CharField(blank=True, max_length=255, null=True)),
                ('option2', models.CharField(blank=True, max_length=255, null=True)),
                ('option3', models.CharField(blank=True, max_length=255, null=True)),
                ('inventory_item_id', models.PositiveIntegerField(default=0, null=True)),
                ('inventory_quantity', models.PositiveIntegerField(default=0, null=True)),
                ('old_inventory_quantity', models.PositiveIntegerField(default=0, null=True)),
                ('admin_graphql_api_id', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
    ]
