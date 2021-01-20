# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Access(models.Model):
    id_access = models.AutoField(primary_key=True)
    title_access = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'access'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Degree(models.Model):
    id_degree = models.AutoField(primary_key=True)
    title_degree = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'degree'


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    title_department = models.CharField(unique=True, max_length=-1)
    abbreviation = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty')

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faculty(models.Model):
    id_faculty = models.AutoField(primary_key=True)
    title_faculty = models.CharField(unique=True, max_length=-1)
    institute = models.ForeignKey('Institute', models.DO_NOTHING, db_column='institute')
    abbreviation = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty'


class Institute(models.Model):
    id_institute = models.AutoField(primary_key=True)
    title_institute = models.CharField(unique=True, max_length=-1)
    abbreviation = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institute'


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title_post = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'post'


class Rank(models.Model):
    id_rank = models.AutoField(primary_key=True)
    title_rank = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'rank'


class Scientist(models.Model):
    id_scientist = models.AutoField(primary_key=True)
    lastname_uk = models.CharField(max_length=-1)
    firstname_uk = models.CharField(max_length=-1)
    middlename_uk = models.CharField(max_length=-1)
    lastname_en = models.CharField(max_length=-1)
    firstname_en = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1, blank=True, null=True)
    orcid = models.CharField(max_length=-1, blank=True, null=True)
    publons = models.CharField(max_length=-1, blank=True, null=True)
    scopusid = models.CharField(max_length=-1, blank=True, null=True)
    h_index_scopus = models.SmallIntegerField(blank=True, null=True)
    google_scholar = models.CharField(max_length=-1, blank=True, null=True)
    h_index_google_scholar = models.SmallIntegerField(blank=True, null=True)
    publons_count_pub = models.SmallIntegerField(blank=True, null=True)
    scopus_count_pub = models.SmallIntegerField(blank=True, null=True)
    google_scholar_count_pub = models.SmallIntegerField(blank=True, null=True)
    rank = models.ForeignKey(Rank, models.DO_NOTHING, db_column='rank')
    degree = models.ForeignKey(Degree, models.DO_NOTHING, db_column='degree')
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='post', blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    work_state = models.ForeignKey('WorkState', models.DO_NOTHING, db_column='work_state')
    pubs_publons = models.TextField(blank=True, null=True)
    pubs_scopus = models.TextField(blank=True, null=True)
    pubs_google_scholar = models.TextField(blank=True, null=True)
    date_update = models.DateField(blank=True, null=True)
    authorization = models.BooleanField()
    login = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    profile_id = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    draft = models.BooleanField(blank=True, null=True)
    h_index_publons = models.SmallIntegerField(blank=True, null=True)
    access = models.ForeignKey(Access, models.DO_NOTHING, db_column='access', blank=True, null=True)
    auth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scientist'


class ScientistSpeciality(models.Model):
    scientist = models.ForeignKey(Scientist, models.DO_NOTHING)
    speciality = models.ForeignKey('Speciality', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scientist_speciality'


class Speciality(models.Model):
    id_speciality = models.AutoField(primary_key=True)
    speciality_title = models.CharField(unique=True, max_length=-1)
    speciality_code = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'speciality'


class UserData(models.Model):
    id_user_data = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'user_data'


class WorkState(models.Model):
    id_state = models.AutoField(primary_key=True)
    title_work_state = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'work_state'
