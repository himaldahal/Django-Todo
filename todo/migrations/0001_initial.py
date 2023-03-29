# Generated by Django 4.1.7 on 2023-03-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='', max_length=600)),
                ('status', models.CharField(choices=[(0, 'Uncompleted'), (1, 'Completed')], default=0, max_length=2)),
            ],
        ),
    ]