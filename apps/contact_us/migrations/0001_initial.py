# Generated by Django 4.2 on 2024-12-09 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carousel', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_line1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=200, null=True)),
                ('landmark', models.CharField(blank=True, help_text='Nearby landmark', max_length=100, null=True)),
                ('city', models.CharField(blank=True, help_text='City Name', max_length=50, null=True)),
                ('state', models.CharField(blank=True, help_text='State Name', max_length=50, null=True)),
                ('country', models.CharField(blank=True, help_text='Country Name', max_length=50, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, help_text='Address Pincode', null=True)),
                ('mobile', models.TextField(blank=True, help_text='Comma-separated mobile numbers', null=True)),
                ('email', models.TextField(blank=True, help_text='Comma-separated email addresses', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Status')),
                ('is_default', models.BooleanField(default=False, help_text='Default Address')),
                ('full_address', models.TextField(blank=True, help_text='Full Address', max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ContactEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text="Enquiry person's first name", max_length=40)),
                ('last_name', models.CharField(help_text="Enquiry person's last name", max_length=40)),
                ('email', models.EmailField(help_text="Enquiry person's email", max_length=255)),
                ('phone_number', models.CharField(help_text="Enquiry person's mobile number", max_length=10)),
                ('message', models.TextField(blank=True, help_text='The Enquiry Message', max_length=1000, null=True)),
                ('enquiry_type', models.CharField(choices=[('GENERAL_ENQUIRY', 'GENERAL ENQUIRY'), ('OVERALL_PACKAGE', 'OVERALL PACKAGE'), ('BRAND_PARTNERS', 'BRAND PARTNERS'), ('OTHERS', 'OTHERS')], help_text='The Enquiry Type', max_length=50)),
                ('artist', models.ForeignKey(blank=True, help_text='The service enquiring about', null=True, on_delete=django.db.models.deletion.SET_NULL, to='carousel.carousel')),
                ('service', models.ForeignKey(blank=True, help_text='The service enquiring about', null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
            options={
                'verbose_name_plural': 'Enquiries (Contact Us)',
            },
        ),
    ]
