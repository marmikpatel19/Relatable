# Generated by Django 4.0.4 on 2022-11-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_prerequisite_course_id_dependency'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='dependency',
            index=models.Index(fields=['course_id'], name='api_depende_course__02b924_idx'),
        ),
        migrations.AddIndex(
            model_name='prerequisite',
            index=models.Index(fields=['course_id'], name='api_prerequ_course__1f9486_idx'),
        ),
    ]