# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronic_medicare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicConditionRegression',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('features', models.CharField(max_length=512)),
                ('target', models.CharField(max_length=512)),
                ('analysis_type', models.CharField(max_length=512)),
                ('description', models.TextField(max_length=2048, blank=True)),
                ('summary_html', models.CharField(max_length=8192, blank=True)),
                ('plot_html', models.CharField(max_length=8388608, blank=True)),
                ('aic', models.FloatField(max_length=64, blank=True, null=True)),
                ('bic', models.FloatField(max_length=64, blank=True, null=True)),
                ('num_observations', models.IntegerField(blank=True, null=True)),
                ('df_residuals', models.IntegerField(blank=True, null=True)),
                ('r_squared', models.FloatField(max_length=64, blank=True, null=True)),
                ('r_squared_adjusted', models.FloatField(max_length=64, blank=True, null=True)),
                ('f_statistic', models.FloatField(max_length=64, blank=True, null=True)),
                ('jarque_bera', models.FloatField(max_length=64, blank=True, null=True)),
                ('jarque_bera_prob', models.FloatField(max_length=64, blank=True, null=True)),
                ('skew', models.FloatField(max_length=64, blank=True, null=True)),
                ('kurtosis', models.FloatField(max_length=64, blank=True, null=True)),
                ('source_file', models.ForeignKey(to='chronic_medicare.AnalysisFile', related_name='regressions')),
            ],
        ),
    ]
