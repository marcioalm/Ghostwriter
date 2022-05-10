# Generated by Django 3.2.11 on 2022-03-25 17:49

# Django Imports
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rolodex', '0027_auto_20220205_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, help_text='Optional explanation for this invite', null=True, verbose_name='Comment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rolodex.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project invite',
                'verbose_name_plural': 'Project invites',
                'ordering': ['project_id', 'user_id'],
            },
        ),
        migrations.CreateModel(
            name='ClientInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, help_text='Optional explanation for this invite', null=True, verbose_name='Comment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rolodex.client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client invite',
                'verbose_name_plural': 'Client invites',
                'ordering': ['client_id', 'user_id'],
            },
        ),
    ]