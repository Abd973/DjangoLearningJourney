# Generated by Django 5.0.4 on 2024-05-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='male',
            name='females',
        ),
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
        migrations.DeleteModel(
            name='Female',
        ),
        migrations.DeleteModel(
            name='Male',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]