# Generated by Django 3.0.5 on 2020-05-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id_access', models.AutoField(primary_key=True, serialize=False)),
                ('title_access', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'db_table': 'access',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id_degree', models.AutoField(primary_key=True, serialize=False)),
                ('title_degree', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Наукова ступінь',
                'verbose_name_plural': 'Наукові ступені',
                'db_table': 'degree',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_department', models.AutoField(primary_key=True, serialize=False)),
                ('title_department', models.CharField(max_length=300, unique=True, verbose_name='Назва')),
                ('abbreviation', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Абревіатура')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедри',
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id_faculty', models.AutoField(primary_key=True, serialize=False)),
                ('title_faculty', models.CharField(max_length=300, unique=True, verbose_name='Назва')),
                ('abbreviation', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Абревіатура')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультети',
                'db_table': 'faculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id_institute', models.AutoField(primary_key=True, serialize=False)),
                ('title_institute', models.CharField(max_length=300, unique=True, verbose_name='Назва')),
                ('abbreviation', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Абревіатура')),
            ],
            options={
                'verbose_name': 'Інститут',
                'verbose_name_plural': 'Інститути',
                'db_table': 'institute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('title_post', models.CharField(max_length=300, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Посада',
                'verbose_name_plural': 'Посади',
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id_rank', models.AutoField(primary_key=True, serialize=False)),
                ('title_rank', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Звання',
                'verbose_name_plural': 'Звання',
                'db_table': 'rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id_scientist', models.AutoField(primary_key=True, serialize=False)),
                ('lastname_uk', models.CharField(max_length=200, verbose_name='Прізвище')),
                ('firstname_uk', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('middlename_uk', models.CharField(max_length=100, verbose_name="Ім'я по-батькові")),
                ('lastname_en', models.CharField(max_length=200, verbose_name='Прізвище (англ.)')),
                ('firstname_en', models.CharField(max_length=100, verbose_name="Ім'я (англ.)")),
                ('email', models.EmailField(blank=True, max_length=300, verbose_name='E-mail')),
                ('orcid', models.CharField(blank=True, max_length=25, verbose_name='ORCID')),
                ('google_scholar', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Google Schoalr')),
                ('h_index_google_scholar', models.PositiveSmallIntegerField(blank=True, verbose_name='h-індекс Google Scholar')),
                ('google_scholar_count_pub', models.PositiveSmallIntegerField(blank=True, verbose_name='Кількість публікацій Google Scholar')),
                ('publons', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Publons')),
                ('h_index_publons', models.PositiveSmallIntegerField(blank=True, verbose_name='h-індекс Publons')),
                ('publons_count_pub', models.PositiveSmallIntegerField(blank=True, verbose_name='Кількість публікацій Pulons')),
                ('scopusid', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Scopus ID')),
                ('h_index_scopus', models.PositiveSmallIntegerField(blank=True, verbose_name='h-індекс Scopus')),
                ('scopus_count_pub', models.PositiveSmallIntegerField(blank=True, verbose_name='Кількість публікацій Scopus')),
                ('pubs_google_scholar', models.TextField(blank=True, verbose_name='Публікації Google Scholar')),
                ('pubs_publons', models.TextField(blank=True, verbose_name='Публікації Pulons')),
                ('pubs_scopus', models.TextField(blank=True, verbose_name='Публікації Scopus')),
                ('date_update', models.DateField(auto_now=True, verbose_name='Дата оновленя')),
                ('authorization', models.BooleanField(default=False, verbose_name='Авторизація')),
                ('login', models.CharField(blank=True, max_length=120, verbose_name='Логін')),
                ('password', models.CharField(blank=True, max_length=50, verbose_name='Пароль')),
                ('profile_id', models.CharField(blank=True, max_length=4, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чернетка')),
            ],
            options={
                'verbose_name': 'Науковець',
                'verbose_name_plural': 'Науковці',
                'db_table': 'scientist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ScientistSpeciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Науковець - Спеціальність',
                'verbose_name_plural': 'Науковці - Спеціальності',
                'db_table': 'scientist_speciality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id_speciality', models.AutoField(primary_key=True, serialize=False)),
                ('speciality_title', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
                ('speciality_code', models.CharField(max_length=20, unique=True, verbose_name='Код спеціальності')),
            ],
            options={
                'verbose_name': 'Спеціальність',
                'verbose_name_plural': 'Спеціальності',
                'db_table': 'speciality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkState',
            fields=[
                ('id_state', models.AutoField(primary_key=True, serialize=False)),
                ('title_work_state', models.CharField(max_length=150, unique=True, verbose_name='Назва статусу')),
            ],
            options={
                'verbose_name': 'Робочий статус',
                'verbose_name_plural': 'Робочий статус',
                'db_table': 'work_state',
                'managed': False,
            },
        ),
    ]
