# Generated by Django 4.0.4 on 2022-11-06 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_course_course_id_course_course_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conjunction_expression', models.CharField(max_length=1, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='api.course')),
                ('course_id_prereq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id_prereq', to='api.course')),
            ],
        ),
    ]