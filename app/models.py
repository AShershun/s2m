from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class Institute(models.Model):
    id_institute = models.AutoField(primary_key=True)
    title_institute = models.CharField('Назва', unique=True, max_length=300)
    abbreviation = models.CharField('Абревіатура', unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'institute'
        verbose_name = 'Інститут'
        verbose_name_plural = 'Інститути'

    def __str__(self):
        return self.title_institute


class Faculty(models.Model):
    id_faculty = models.AutoField(primary_key=True)
    title_faculty = models.CharField('Назва', unique=True, max_length=300)
    institute = models.ForeignKey('Institute', on_delete=models.CASCADE, db_column='institute', to_field='id_institute',
                                  verbose_name="Інститут")
    abbreviation = models.CharField('Абревіатура', unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'faculty'
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультети'

    def __str__(self):
        return self.title_faculty


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    title_department = models.CharField('Назва', unique=True, max_length=300)
    abbreviation = models.CharField('Абревіатура', unique=True, max_length=50, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, db_column='faculty', to_field='id_faculty',
                                verbose_name="Факультет")

    class Meta:
        managed = False
        db_table = 'department'
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедри'

    def __str__(self):
        return self.title_department


class Degree(models.Model):
    id_degree = models.AutoField(primary_key=True)
    title_degree = models.CharField('Назва', unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'degree'
        verbose_name = 'Наукова ступінь'
        verbose_name_plural = 'Наукові ступені'

    def __str__(self):
        return self.title_degree


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title_post = models.CharField('Назва', unique=True, max_length=300)

    class Meta:
        managed = False
        db_table = 'post'
        verbose_name = 'Посада'
        verbose_name_plural = 'Посади'

    def __str__(self):
        return self.title_post


class Rank(models.Model):
    id_rank = models.AutoField(primary_key=True)
    title_rank = models.CharField('Назва', unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'rank'
        verbose_name = 'Наукове звання'
        verbose_name_plural = 'Наукові звання'

    def __str__(self):
        return '%s' % self.title_rank


class Speciality(models.Model):
    id_speciality = models.AutoField(primary_key=True)
    speciality_title = models.CharField('Назва', unique=True, max_length=200)
    speciality_code = models.CharField('Код спеціальності', unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'speciality'
        verbose_name = 'Спеціальність'
        verbose_name_plural = 'Спеціальності'

    def __str__(self):
        return '%s' % self.speciality_title


class Scientist(models.Model):
    id_scientist = models.AutoField(primary_key=True)
    lastname_uk = models.CharField('Прізвище', max_length=200)
    firstname_uk = models.CharField('Ім\'я', max_length=100)
    middlename_uk = models.CharField('Ім\'я по-батькові', max_length=100)
    lastname_en = models.CharField('Прізвище (англ.)', max_length=200)
    firstname_en = models.CharField('Ім\'я (англ.)', max_length=100)
    email = models.EmailField('E-mail', max_length=300, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='department',
                                   to_field='id_department', verbose_name="Кафедра")
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, db_column='rank', to_field='id_rank', blank=True,
                             verbose_name="Наукове звання")
    degree = models.ForeignKey('Degree', on_delete=models.CASCADE, db_column='degree', to_field='id_degree', blank=True,
                               verbose_name="Наукова ступінь")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, db_column='post', to_field='id_post', blank=True,
                             verbose_name="Посада")
    speciality = models.ManyToManyField('Speciality', blank=True, verbose_name="Спеціальність")
    work_state = models.ForeignKey('WorkState', on_delete=models.CASCADE, db_column='work_state', to_field='id_state',
                                   verbose_name="Робочий статус", default="Працює")
    orcid = models.CharField('ORCID', max_length=25, help_text="0000-0002-1398-1472", blank=True)
    google_scholar = models.CharField('Google Scholar', max_length=200, blank=True, null=False, unique=False,
                                      help_text="citations?user=EF1_85cAAAAJ&hl=ru")
    h_index_google_scholar = models.PositiveSmallIntegerField('h-індекс Google Scholar', default=0)
    google_scholar_count_pub = models.PositiveSmallIntegerField('Кількість публікацій Google Scholar', default=0)
    publons = models.CharField('Publons', max_length=100, blank=True, null=False, unique=False, help_text="P-2507-2015")
    h_index_publons = models.PositiveSmallIntegerField('h-індекс WoS', default=0)
    publons_count_pub = models.PositiveSmallIntegerField('Кількість публікацій WoS', default=0)
    scopusid = models.CharField('Scopus ID', max_length=200, blank=True, null=False, unique=False,
                                help_text="24337331300")
    h_index_scopus = models.PositiveSmallIntegerField('h-індекс Scopus', default=0)
    scopus_count_pub = models.PositiveSmallIntegerField('Кількість публікацій Scopus', default=0)
    pubs_google_scholar = models.TextField('Публікації Google Scholar', blank=True)
    pubs_publons = models.TextField('Публікації Pulons', blank=True, null=False)
    pubs_scopus = models.TextField('Публікації Scopus', blank=True, null=False)
    date_update = models.DateField("Дата оновленя", auto_now=True, null=False)
    authorization = models.BooleanField('Авторизація', default=False)
    login = models.CharField('Логін', max_length=120, blank=True)
    password = models.CharField('Пароль', max_length=50, blank=True)
    profile_id = models.CharField('Код користувача', max_length=4, editable=True, unique=True, blank=True)
    draft = models.BooleanField('Чернетка', default=False)

    class Meta:
        managed = False
        db_table = 'scientist'
        verbose_name = 'Науковець'
        verbose_name_plural = 'Науковці'

    def save(self):
        super(Scientist, self).save()
        if not self.profile_id:
            self.profile_id = str(self.id_scientist)
            self.profile_id = self.profile_id.zfill(4)
            super(Scientist, self).save()

    # def get_absolute_url(self):
    #     return reverse("profile", kwargs={"profile_id": self.profile_id})

    # def get_fio(self):
    #     return '%s %s %s' % (self.lastname_uk, self.firstname_uk, self.middlename_uk)

    def __str__(self):
        return '%s %s %s' % (self.lastname_uk, self.firstname_uk, self.middlename_uk)


class ScientistSpeciality(models.Model):
    id = models.AutoField(primary_key=True)
    scientist_id = models.ForeignKey(Scientist, db_column='scientist_id', on_delete=models.CASCADE, null=True,
                                     to_field='id_scientist', verbose_name="Науковець")
    speciality_id = models.ForeignKey(Speciality, db_column='speciality_id', on_delete=models.CASCADE, null=True,
                                      to_field='id_speciality', verbose_name="Спеціальність")

    class Meta:
        managed = False
        db_table = 'scientist_speciality'
        verbose_name = 'Науковець - Спеціальність'
        verbose_name_plural = 'Науковці - Спеціальності'


class WorkState(models.Model):
    id_state = models.AutoField(primary_key=True)
    title_work_state = models.CharField('Назва статусу', unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'work_state'
        verbose_name = 'Робочий статус'
        verbose_name_plural = 'Робочий статус'

    def __str__(self):
        return '%s' % self.title_work_state
