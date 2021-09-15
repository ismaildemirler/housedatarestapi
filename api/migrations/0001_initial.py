# Generated by Django 3.2.4 on 2021-07-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.UUIDField()),
                ('price', models.IntegerField()),
                ('transaction_date', models.DateField()),
                ('post_code', models.CharField(max_length=50)),
                ('home_type', models.CharField(max_length=1)),
                ('unknown1', models.CharField(max_length=1)),
                ('unknown2', models.CharField(max_length=1)),
                ('paon', models.CharField(max_length=150)),
                ('saon', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('locality', models.CharField(max_length=150)),
                ('town', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('county', models.CharField(max_length=150)),
                ('unknown3', models.CharField(max_length=1)),
                ('unknown4', models.CharField(max_length=1)),
            ],
        ),
    ]
