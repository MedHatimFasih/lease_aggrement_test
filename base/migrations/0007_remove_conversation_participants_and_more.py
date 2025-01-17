# Generated by Django 5.0.6 on 2024-07-20 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_conversation_property_conversation_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='participants',
        ),
        migrations.AddField(
            model_name='conversation',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_conversations', to='base.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sent_conversations', to='base.user'),
            preserve_default=False,
        ),
    ]
