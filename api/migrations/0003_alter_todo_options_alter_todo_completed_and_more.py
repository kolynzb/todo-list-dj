# Generated by Django 4.0.3 on 2023-08-01 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, help_text='Designates whether Job Post is a Draft.'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=225, verbose_name='Todo Text'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=225, verbose_name='Todo Title'),
        ),
    ]
