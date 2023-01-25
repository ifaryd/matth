# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actualites(models.Model):
    id = models.AutoField()
    miniature = models.TextField(blank=True, null=True)
    contenu = models.TextField()
    video = models.TextField(blank=True, null=True)
    langue_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actualites'


class Assemblees(models.Model):
    id = models.AutoField()
    nom = models.CharField(blank=True, null=True)
    ville_id = models.IntegerField()
    localisation = models.TextField(blank=True, null=True)
    addresse = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assemblees'


class Cantiques(models.Model):
    id = models.AutoField()
    titre = models.TextField()
    lien_audio = models.TextField()
    nom_fichier = models.TextField(blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantiques'


class ChargeUsers(models.Model):
    id = models.AutoField()
    charge_id = models.IntegerField()
    user_id = models.IntegerField()
    pays_id = models.IntegerField(blank=True, null=True)
    assemblee_id = models.IntegerField(blank=True, null=True)
    principal = models.TextField()  # This field type is a guess.
    position_chantre = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charge_users'


class Charges(models.Model):
    id = models.AutoField()
    libelle = models.CharField()
    description = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charges'


class Concordances(models.Model):
    id = models.AutoField()
    verset_from_id = models.IntegerField()
    verset_to_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concordances'


class Confirmes(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    pays_id = models.IntegerField()
    video_id = models.IntegerField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirmes'


class FailedJobs(models.Model):
    id = models.AutoField()
    uuid = models.CharField(unique=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class LanguePays(models.Model):
    id = models.AutoField()
    langue_id = models.IntegerField()
    pays_id = models.IntegerField()
    principal = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'langue_pays'


class Langues(models.Model):
    id = models.AutoField()
    libelle = models.CharField()
    initial = models.CharField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'langues'


class Migrations(models.Model):
    id = models.AutoField()
    migration = models.CharField()
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField()
    token = models.CharField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Pays(models.Model):
    id = models.AutoField()
    nom = models.CharField()
    sigle = models.CharField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays'


class PersonalAccessTokens(models.Model):
    id = models.AutoField()
    tokenable_type = models.CharField()
    tokenable_id = models.IntegerField()
    name = models.CharField()
    token = models.CharField(unique=True)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Photos(models.Model):
    id = models.AutoField()
    url = models.TextField()
    lieu = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photos'


class Predications(models.Model):
    id = models.AutoField()
    titre = models.CharField()
    sous_titre = models.CharField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    lien_audio = models.TextField(blank=True, null=True)
    nom_audio = models.TextField(blank=True, null=True)
    lien_video = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    chapitre = models.CharField(blank=True, null=True)
    couverture = models.TextField(blank=True, null=True)
    sermon_similaire = models.TextField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predications'


class Temoignages(models.Model):
    id = models.AutoField()
    titre = models.TextField(blank=True, null=True)
    lien_video = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temoignages'


class Types(models.Model):
    id = models.AutoField()
    libelle = models.CharField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class Users(models.Model):
    id = models.AutoField()
    first_name = models.CharField()
    last_name = models.CharField(blank=True, null=True)
    telephone = models.CharField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    remember_token = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versets(models.Model):
    id = models.AutoField()
    numero = models.IntegerField()
    contenu = models.TextField()
    info = models.TextField(blank=True, null=True)
    predication_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versets'


class Videos(models.Model):
    id = models.AutoField()
    titre = models.TextField()
    url = models.TextField()
    lieu = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    langue_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos'


class Villes(models.Model):
    id = models.AutoField()
    libelle = models.CharField()
    description = models.TextField(blank=True, null=True)
    pays_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villes'
