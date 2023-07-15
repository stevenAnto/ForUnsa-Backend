# Generated by Django 4.2.2 on 2023-07-02 04:29

import apps.forum.models.post
import apps.forum.models.report
import apps.forum.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-likes_count']},
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='posts', validators=[apps.forum.validators.MaxWeightValidator]),
        ),
        migrations.AddField(
            model_name='post',
            name='approval_status',
            field=models.ForeignKey(default=apps.forum.models.post.ApprovalStatus.get_default_status, on_delete=django.db.models.deletion.SET_DEFAULT, to='forum.approvalstatus'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_tyoe',
            field=models.ForeignKey(default=apps.forum.models.report.ReportType.get_default_type, on_delete=django.db.models.deletion.SET_DEFAULT, to='forum.reporttype'),
        ),
    ]
