# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class SwSet(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate', blank=True, null=True)  # Field name made lowercase.
    setcode = models.CharField(db_column='SetCode', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sw_set'


class SwCard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    setid = models.ForeignKey(db_column='SetID', to="SwSet", on_delete=models.CASCADE)  # Field name made lowercase.
    aspects = models.CharField(db_column='Aspects', max_length=100, blank=True, null=True)  # Field name made lowercase.
    traits = models.CharField(db_column='Traits', max_length=100, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arena = models.CharField(db_column='Arena', max_length=20, blank=True, null=True)  # Field name made lowercase.
    artist = models.CharField(db_column='Artist', max_length=70, blank=True, null=True)  # Field name made lowercase.
    rarity = models.CharField(db_column='Rarity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cost = models.CharField(db_column='Cost', max_length=10, blank=True, null=True)  # Field name made lowercase.
    power = models.CharField(db_column='Power', max_length=10, blank=True, null=True)  # Field name made lowercase.
    health = models.CharField(db_column='Health', max_length=10, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='Keywords', max_length=150, blank=True, null=True)  # Field name made lowercase.
    frontimage = models.TextField(db_column='FrontImage', blank=True, null=True)  # Field name made lowercase.
    setcardid = models.IntegerField(db_column='SetCardID')  # Field name made lowercase.
    unique = models.CharField(db_column='Unique', max_length=10, blank=True, null=True)  # Field name made lowercase.
    doublesided = models.CharField(db_column='DoubleSided', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subtitle = models.CharField(db_column='Subtitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    backimage = models.TextField(db_column='BackImage', blank=True, null=True)  # Field name made lowercase.
    epicaction = models.CharField(db_column='EpicAction', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fronttext = models.CharField(db_column='FrontText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    backtext = models.CharField(db_column='BackText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    variant = models.CharField(db_column='Variant', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sw_card'

    def __str__(self):
        return self.name
