# Generated by Django 4.1.7 on 2023-03-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_employee_student_alter_student_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='econtact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='eemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ename',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='eid',
            new_name='sid',
        ),
    ]
