# Generated by Django 4.2.6 on 2023-10-17 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=16, verbose_name='phone number')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('header', models.CharField(max_length=1000)),
                ('sub_header', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='media/Banners/')),
                ('btn_link', models.CharField(max_length=1000)),
                ('btn_text', models.CharField(max_length=1000)),
                ('btn_color', models.CharField(max_length=255)),
                ('btn_text_color', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingFeeZone',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField()),
                ('location', models.TextField()),
                ('coordinates', models.JSONField()),
                ('image', models.ImageField(upload_to='media/Site-Addresses/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('handle', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=1000)),
                ('caption', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('avatar', models.ImageField(upload_to='media/Testimonial/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=255)),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Site Name', max_length=255)),
                ('maintenance_mode', models.BooleanField(default=False)),
                ('phone_number', models.TextField(blank=True)),
                ('site_email', models.EmailField(blank=True, max_length=254)),
                ('site_percentage', models.DecimalField(decimal_places=2, default=5.0, max_digits=9)),
                ('appstore_link', models.URLField(blank=True)),
                ('playstore_link', models.URLField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('working_hours', models.TextField(blank=True, null=True)),
                ('addresses', models.ManyToManyField(blank=True, to='administrator.siteaddress')),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=4)),
                ('tel', models.CharField(max_length=4)),
                ('is_active', models.BooleanField(default=True)),
                ('shipping_zones', models.ManyToManyField(blank=True, related_name='countries', to='administrator.shippingfeezone')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]