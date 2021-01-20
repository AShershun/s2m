from django.contrib import admin
from .models import Degree, Department, Faculty, Institute, Post, Rank, Scientist, Speciality, WorkState
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.gis import forms


# CKEditor
class ScientistAdminForm(forms.ModelForm):
    pubs_google_scholar = forms.CharField(label="Публікації Google Scholar", widget=CKEditorUploadingWidget(),
                                          required=False)
    pubs_publons = forms.CharField(label="Публікації Pulons", widget=CKEditorUploadingWidget(), required=False)
    pubs_scopus = forms.CharField(label="Публікації Scopus", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Scientist
        fields = '__all__'


@admin.register(Scientist)
class ScientistAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "orcid", "profile_id", "draft", "date_update")
    list_display_links = ("name",)
    list_filter = ("department__faculty__institute", "speciality")
    search_fields = (
        "profile_id", "lastname_uk", "lastname_en", "email", "post__title_post", "degree__title_degree",
        "rank__title_rank",
        "speciality__speciality_title", "speciality__speciality_code", "work_state__title_work_state")
    readonly_fields = ("profile_id",)
    save_on_top = True
    list_editable = ("draft",)
    list_per_page = 100
    fieldsets = (
        ("Основна інформація", {
            "fields": ("lastname_uk", "firstname_uk", "middlename_uk", "lastname_en", "firstname_en", "email")
        }),
        (None, {
            "fields": ("department", "post", "rank", "degree", "speciality", "work_state")
        }),
        ("Наукометричні показники", {
            "fields": ("orcid", ("google_scholar", "h_index_google_scholar", "google_scholar_count_pub"),
                       ("publons", "h_index_publons", "publons_count_pub"),
                       ("scopusid", "h_index_scopus", "scopus_count_pub"), "pubs_google_scholar", "pubs_publons",
                       "pubs_scopus")
        }),
        ("Авторизація", {
            "classes": ("collapse",),
            "fields": ("authorization", ("login", "password"))
        }),
        (None, {
            "fields": ("profile_id", "draft")
        }),
    )
    form = ScientistAdminForm

    def get_queryset(self, request):
        queryset = super(ScientistAdmin, self).get_queryset(request)
        queryset = queryset.order_by('lastname_uk')
        return queryset

    def name(self, obj):
        return "%s %s %s" % (obj.lastname_uk, obj.firstname_uk, obj.middlename_uk)

    name.short_description = "ПІБ"


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("title_institute", "abbreviation")


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("title_faculty", "abbreviation")
    list_filter = ("institute",)

    def get_queryset(self, request):
        queryset = super(FacultyAdmin, self).get_queryset(request)
        queryset = queryset.order_by('title_faculty')
        return queryset


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title_department", "abbreviation")
    list_filter = ("faculty__institute",)

    def get_queryset(self, request):
        queryset = super(DepartmentAdmin, self).get_queryset(request)
        queryset = queryset.order_by('title_department')
        return queryset


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("title_degree",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title_post",)


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ("title_rank",)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("speciality_title", "speciality_code")


@admin.register(WorkState)
class WorkStateAdmin(admin.ModelAdmin):
    list_display = ("title_work_state",)


admin.site.site_title = "S2M"
admin.site.site_header = "S2M Адміністрування"
