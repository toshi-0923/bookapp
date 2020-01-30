# Generated by Django 3.0.2 on 2020-01-29 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate', '0003_auto_20200128_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='年月一覧')),
            ],
        ),
        migrations.AddField(
            model_name='aggregate',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='aggregate.Index'),
        ),
    ]