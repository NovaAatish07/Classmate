# Generated by Django 3.2.5 on 2021-08-01 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assignmentapp', '0013_semester_sub_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sem_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='semester_ref2', to='Assignmentapp.semester', verbose_name='Semester No'),
        ),
    ]
