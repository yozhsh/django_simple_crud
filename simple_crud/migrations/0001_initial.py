# Generated by Django 2.2.6 on 2019-10-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
                ('notes', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
