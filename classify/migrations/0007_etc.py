# Generated by Django 5.0.6 on 2024-07-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0006_adult_casino_copyright_hosts_normal_whitelist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
    ]
