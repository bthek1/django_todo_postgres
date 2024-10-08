# Generated by Django 5.0.3 on 2024-09-05 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_inputfield_floatinputfield_integerinputfield_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputfield',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='inputs',
        ),
        migrations.RemoveField(
            model_name='integerinputfield',
            name='inputfield_ptr',
        ),
        migrations.RemoveField(
            model_name='textinputfield',
            name='inputfield_ptr',
        ),
        migrations.DeleteModel(
            name='FloatInputField',
        ),
        migrations.DeleteModel(
            name='IntegerInputField',
        ),
        migrations.DeleteModel(
            name='InputField',
        ),
        migrations.DeleteModel(
            name='TextInputField',
        ),
    ]
