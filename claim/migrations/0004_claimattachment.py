# Generated by Django 2.1.11 on 2019-10-28 06:40

import core.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0003_claimofficer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom')),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('date', core.fields.DateField(blank=True, null=True)),
                ('filename', models.TextField(blank=True, null=True)),
                ('mime', models.TextField(blank=True, null=True)),
                ('document', models.TextField(blank=True, null=True)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attachments', to='claim.Claim')),
            ],
            options={
                'db_table': 'claim_ClaimAttachment',
                'managed': True,
            },
        ),
    ]