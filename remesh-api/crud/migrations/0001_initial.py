# Generated by Django 3.2.4 on 2021-06-25 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='start date')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date and time sent')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.conversation')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='signup date')),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date and time sent')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.message')),
            ],
        ),
    ]
