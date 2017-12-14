# Generated by Django 2.0 on 2017-12-19 12:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('value_type', models.CharField(choices=[('int', 'int'), ('string', 'string'), ('boolean', 'boolean'), ('date', 'date')], max_length=32, verbose_name='value type')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'attribute',
                'verbose_name_plural': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='PlanProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='attributes')),
            ],
            options={
                'verbose_name': 'plan project',
                'verbose_name_plural': 'plan projects',
            },
        ),
        migrations.CreateModel(
            name='ValueChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256, verbose_name='value')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_choices', to='plans.Attribute', verbose_name='attribute')),
            ],
            options={
                'verbose_name': 'value choice',
                'verbose_name_plural': 'value choices',
            },
        ),
        migrations.AlterUniqueTogether(
            name='valuechoice',
            unique_together={('attribute', 'slug')},
        ),
    ]
