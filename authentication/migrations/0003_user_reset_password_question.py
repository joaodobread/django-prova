# Generated by Django 4.1.3 on 2022-12-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_password_question',
            field=models.CharField(max_length=5),
            preserve_default=False,
        ),
    ]
