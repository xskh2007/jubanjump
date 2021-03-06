# Generated by Django 2.1.7 on 2019-02-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MongoSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbname', models.CharField(default='', max_length=128, verbose_name='dbname')),
                ('script', models.TextField(verbose_name='Script')),
                ('_result', models.TextField(blank=True, null=True, verbose_name='Result')),
                ('is_finished', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField(null=True)),
                ('date_finished', models.DateTimeField(null=True)),
            ],
        ),
    ]
