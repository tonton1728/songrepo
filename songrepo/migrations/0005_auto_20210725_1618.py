# Generated by Django 3.2.5 on 2021-07-25 16:18

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songrepo', '0004_partitions_partition_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='partition_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partition_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/data/partitions'), upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='partitions',
            name='partition_files',
        ),
        migrations.AddField(
            model_name='partitions',
            name='partition_files',
            field=models.ManyToManyField(to='songrepo.partition_file'),
        ),
    ]