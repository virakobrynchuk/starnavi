# Generated by Django 2.2.6 on 2019-10-28 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_title', models.CharField(max_length=100)),
                ('post_text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('post_likes', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_value', models.IntegerField()),
                ('like_date', models.DateTimeField(auto_now=True)),
                ('like_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('like_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
