# Generated by Django 3.2.6 on 2021-09-01 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.user')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=256)),
                ('resume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(auto_now=True, verbose_name='End Date')),
                ('company_name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.user')),
            ],
        ),
    ]