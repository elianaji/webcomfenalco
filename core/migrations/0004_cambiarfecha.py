# Generated by Django 3.2.19 on 2023-07-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_desbloqueo_fechaexpi'),
    ]

    operations = [
        migrations.CreateModel(
            name='cambiarfecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cambiarfecha', models.DateField()),
            ],
        ),
    ]
