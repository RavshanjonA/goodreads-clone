# Generated by Django 5.0.7 on 2024-07-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_genre_alter_users_avatar_bookreview_bookshelf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='middle_name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
    ]
