# Generated by Django 3.2.5 on 2021-07-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignmentapp', '0007_auto_20210730_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='student_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='teacher_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
