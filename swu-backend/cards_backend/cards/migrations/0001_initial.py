# Generated by Django 5.1 on 2024-08-29 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SwSet',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('releasedate', models.DateTimeField(blank=True, db_column='ReleaseDate', null=True)),
                ('setcode', models.CharField(blank=True, db_column='SetCode', max_length=3, null=True)),
            ],
            options={
                'db_table': 'sw_set',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SwCard',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=35)),
                ('aspects', models.CharField(blank=True, db_column='Aspects', max_length=100, null=True)),
                ('traits', models.CharField(blank=True, db_column='Traits', max_length=100, null=True)),
                ('card_type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('arena', models.CharField(blank=True, db_column='Arena', max_length=20, null=True)),
                ('artist', models.CharField(blank=True, db_column='Artist', max_length=70, null=True)),
                ('rarity', models.CharField(blank=True, db_column='Rarity', max_length=50, null=True)),
                ('cost', models.CharField(blank=True, db_column='Cost', max_length=10, null=True)),
                ('power', models.CharField(blank=True, db_column='Power', max_length=10, null=True)),
                ('health', models.CharField(blank=True, db_column='Health', max_length=10, null=True)),
                ('keywords', models.CharField(blank=True, db_column='Keywords', max_length=150, null=True)),
                ('frontimage', models.TextField(blank=True, db_column='FrontImage', null=True)),
                ('setcardid', models.IntegerField(db_column='SetCardID')),
                ('unique', models.CharField(blank=True, db_column='Unique', max_length=10, null=True)),
                ('doublesided', models.CharField(blank=True, db_column='DoubleSided', max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, db_column='Subtitle', max_length=45, null=True)),
                ('backimage', models.TextField(blank=True, db_column='BackImage', null=True)),
                ('epicaction', models.CharField(blank=True, db_column='EpicAction', max_length=500, null=True)),
                ('fronttext', models.CharField(blank=True, db_column='FrontText', max_length=500, null=True)),
                ('backtext', models.CharField(blank=True, db_column='BackText', max_length=500, null=True)),
                ('variant', models.CharField(blank=True, db_column='Variant', max_length=100, null=True)),
                ('setid', models.ForeignKey(db_column='SetID', on_delete=django.db.models.deletion.CASCADE, to='cards.swset')),
            ],
            options={
                'db_table': 'sw_card',
                'managed': True,
            },
        ),
    ]
