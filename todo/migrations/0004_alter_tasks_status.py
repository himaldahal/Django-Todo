# Generated by Django 4.1.7 on 2023-03-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('0', 'Uncompleted'), ('1', 'Completed')], default='0', max_length=1),
        ),
    ]