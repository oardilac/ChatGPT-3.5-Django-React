# Generated by Django 4.2.1 on 2023-06-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0002_chatbot_item_requestmodeltexto_submitfiles_url_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="FileMetadata",
        ),
        migrations.DeleteModel(
            name="Item",
        ),
        migrations.DeleteModel(
            name="UrlResponse",
        ),
    ]
