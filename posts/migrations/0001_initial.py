# Generated by Django 3.2 on 2022-03-30 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.CharField(max_length=8000)),
                ('large', models.CharField(max_length=8000)),
            ],
            options={
                'verbose_name_plural': 'Post photos',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('text', models.TextField(max_length=10000)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postphotos')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]