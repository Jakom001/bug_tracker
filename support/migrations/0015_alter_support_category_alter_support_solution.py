# Generated by Django 4.0.6 on 2022-07-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0014_alter_support_category_alter_support_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='category',
            field=models.CharField(choices=[('1', 'Network'), ('2', 'Printer'), ('3', 'Computer'), ('4', 'CCTV'), ('5', 'Software'), ('6', 'Data/Files')], default=1, max_length=24),
        ),
        migrations.AlterField(
            model_name='support',
            name='solution',
            field=models.TextField(default='', max_length=500, verbose_name='Solution/Remarks'),
        ),
    ]
