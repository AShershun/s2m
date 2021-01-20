import csv
import xlwt
from app.models import Degree, Department, Faculty, Institute, Post, Rank, Scientist, Speciality
from django.views.generic.base import View
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# def login(request):
#     if request.method == 'POST':


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user =
#     else:
#         return render(request, 'mainPage.html')
# pass

class MainPage(View):
    """Дані вчених для побудови графіку"""

    def get(self, request):
        google_scholar = Scientist.objects.all().order_by('google_scholar_count_pub').filter(google_scholar_count_pub__isnull=False, draft=False).reverse()[:10]
        publons = Scientist.objects.all().order_by('publons_count_pub').filter(publons_count_pub__isnull=False,
                                                                               draft=False).reverse()[:10]
        scopus = Scientist.objects.all().order_by('scopus_count_pub').filter(scopus_count_pub__isnull=False,
                                                                             draft=False).reverse()[:10]

        # Google Scholar Data
        scientist_google_scholar = []
        google_scholar_count_pub = []
        google_scholar_profile_id = []

        for i in range(10):
            google_scholar_name = (
                    google_scholar[i].lastname_uk + " " + google_scholar[i].firstname_uk + " " + google_scholar[i].middlename_uk)
            scientist_google_scholar.append(google_scholar_name)
            google_scholar_pub = google_scholar[i].google_scholar_count_pub
            google_scholar_count_pub.append(google_scholar_pub)
            google_scholar_id = google_scholar[i].profile_id
            google_scholar_profile_id.append(google_scholar_id)

        # Publons Data
        scientist_publons = []
        publons_count_pub = []
        publons_profile_id = []

        for i in range(10):
            publons_name = (publons[i].lastname_uk + " " + publons[i].firstname_uk + " " + publons[i].middlename_uk)
            scientist_publons.append(publons_name)
            publons_pub = publons[i].publons_count_pub
            publons_count_pub.append(publons_pub)
            publons_id = publons[i].profile_id
            publons_profile_id.append(publons_id)

        # Scopus Data
        scientist_scopus = []
        scopus_count_pub = []
        scopus_profile_id = []

        for i in range(10):
            scopus_name = (scopus[i].lastname_uk + " " + scopus[i].firstname_uk + " " + scopus[i].middlename_uk)
            scientist_scopus.append(scopus_name)
            scopus_pub = scopus[i].scopus_count_pub
            scopus_count_pub.append(scopus_pub)
            scopus_id = scopus[i].profile_id
            scopus_profile_id.append(scopus_id)

        context = {
            'scientist_google_scholar_1': scientist_google_scholar[0],
            'scientist_google_scholar_2': scientist_google_scholar[1],
            'scientist_google_scholar_3': scientist_google_scholar[2],
            'scientist_google_scholar_4': scientist_google_scholar[3],
            'scientist_google_scholar_5': scientist_google_scholar[4],
            'scientist_google_scholar_6': scientist_google_scholar[5],
            'scientist_google_scholar_7': scientist_google_scholar[6],
            'scientist_google_scholar_8': scientist_google_scholar[7],
            'scientist_google_scholar_9': scientist_google_scholar[8],
            'scientist_google_scholar_10': scientist_google_scholar[9],
            'google_scholar_count_pub_1': google_scholar_count_pub[0],
            'google_scholar_count_pub_2': google_scholar_count_pub[1],
            'google_scholar_count_pub_3': google_scholar_count_pub[2],
            'google_scholar_count_pub_4': google_scholar_count_pub[3],
            'google_scholar_count_pub_5': google_scholar_count_pub[4],
            'google_scholar_count_pub_6': google_scholar_count_pub[5],
            'google_scholar_count_pub_7': google_scholar_count_pub[6],
            'google_scholar_count_pub_8': google_scholar_count_pub[7],
            'google_scholar_count_pub_9': google_scholar_count_pub[8],
            'google_scholar_count_pub_10': google_scholar_count_pub[9],
            'google_scholar_profile_id_1': google_scholar_profile_id[0],
            'google_scholar_profile_id_2': google_scholar_profile_id[1],
            'google_scholar_profile_id_3': google_scholar_profile_id[2],
            'google_scholar_profile_id_4': google_scholar_profile_id[3],
            'google_scholar_profile_id_5': google_scholar_profile_id[4],
            'google_scholar_profile_id_6': google_scholar_profile_id[5],
            'google_scholar_profile_id_7': google_scholar_profile_id[6],
            'google_scholar_profile_id_8': google_scholar_profile_id[7],
            'google_scholar_profile_id_9': google_scholar_profile_id[8],
            'google_scholar_profile_id_10': google_scholar_profile_id[9],
            'scientist_publons_1': scientist_publons[0],
            'scientist_publons_2': scientist_publons[1],
            'scientist_publons_3': scientist_publons[2],
            'scientist_publons_4': scientist_publons[3],
            'scientist_publons_5': scientist_publons[4],
            'scientist_publons_6': scientist_publons[5],
            'scientist_publons_7': scientist_publons[6],
            'scientist_publons_8': scientist_publons[7],
            'scientist_publons_9': scientist_publons[8],
            'scientist_publons_10': scientist_publons[9],
            'publons_count_pub_1': publons_count_pub[0],
            'publons_count_pub_2': publons_count_pub[1],
            'publons_count_pub_3': publons_count_pub[2],
            'publons_count_pub_4': publons_count_pub[3],
            'publons_count_pub_5': publons_count_pub[4],
            'publons_count_pub_6': publons_count_pub[5],
            'publons_count_pub_7': publons_count_pub[6],
            'publons_count_pub_8': publons_count_pub[7],
            'publons_count_pub_9': publons_count_pub[8],
            'publons_count_pub_10': publons_count_pub[9],
            'publons_profile_id_1': publons_profile_id[0],
            'publons_profile_id_2': publons_profile_id[1],
            'publons_profile_id_3': publons_profile_id[2],
            'publons_profile_id_4': publons_profile_id[3],
            'publons_profile_id_5': publons_profile_id[4],
            'publons_profile_id_6': publons_profile_id[5],
            'publons_profile_id_7': publons_profile_id[6],
            'publons_profile_id_8': publons_profile_id[7],
            'publons_profile_id_9': publons_profile_id[8],
            'publons_profile_id_10': publons_profile_id[9],
            'scientist_scopus_1': scientist_scopus[0],
            'scientist_scopus_2': scientist_scopus[1],
            'scientist_scopus_3': scientist_scopus[2],
            'scientist_scopus_4': scientist_scopus[3],
            'scientist_scopus_5': scientist_scopus[4],
            'scientist_scopus_6': scientist_scopus[5],
            'scientist_scopus_7': scientist_scopus[6],
            'scientist_scopus_8': scientist_scopus[7],
            'scientist_scopus_9': scientist_scopus[8],
            'scientist_scopus_10': scientist_scopus[9],
            'scopus_count_pub_1': scopus_count_pub[0],
            'scopus_count_pub_2': scopus_count_pub[1],
            'scopus_count_pub_3': scopus_count_pub[2],
            'scopus_count_pub_4': scopus_count_pub[3],
            'scopus_count_pub_5': scopus_count_pub[4],
            'scopus_count_pub_6': scopus_count_pub[5],
            'scopus_count_pub_7': scopus_count_pub[6],
            'scopus_count_pub_8': scopus_count_pub[7],
            'scopus_count_pub_9': scopus_count_pub[8],
            'scopus_count_pub_10': scopus_count_pub[9],
            'scopus_profile_id_1': scopus_profile_id[0],
            'scopus_profile_id_2': scopus_profile_id[1],
            'scopus_profile_id_3': scopus_profile_id[2],
            'scopus_profile_id_4': scopus_profile_id[3],
            'scopus_profile_id_5': scopus_profile_id[4],
            'scopus_profile_id_6': scopus_profile_id[5],
            'scopus_profile_id_7': scopus_profile_id[6],
            'scopus_profile_id_8': scopus_profile_id[7],
            'scopus_profile_id_9': scopus_profile_id[8],
            'scopus_profile_id_10': scopus_profile_id[9],

        }
        return render(request, "mainPage.html", context)


class ScientistsPage(ListView):
    """Перелік вчених"""
    model = Scientist
    queryset = Scientist.objects.order_by('lastname_uk').filter(draft=False)
    template_name = "scientistsPage.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scientists_counter'] = self.queryset.count()
        return context


class Search(ListView):
    """Пошук вчених"""
    paginate_by = 10
    template_name = "scientistsPage.html"

    def get_queryset(self):
        queryset = ""
        select = self.request.GET.get('select')
        filter_dropdown_menu = self.request.GET.get('filter')
        if "pib" in select:
            if "fullname_up" in filter_dropdown_menu:
                queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                    'lastname_uk')
            else:
                if "fullname_down" in filter_dropdown_menu:
                    queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                        'lastname_uk').reverse()
                else:
                    if "gsh_down" in filter_dropdown_menu:
                        queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                            'h_index_google_scholar')
                    else:
                        if "gsh_up" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                                'h_index_google_scholar').reverse()
                        else:
                            if "ph_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by('h_index_publons')
                            else:
                                if "ph_up" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                                        'h_index_publons').reverse()
                                else:
                                    if "sh_down" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by('h_index_scopus')
                                    else:
                                        if "sh_up" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                                                'h_index_scopus').reverse()
        else:

            if "department" in select:
                if "fullname_up" in filter_dropdown_menu:
                    queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                        'lastname_uk')
                else:
                    if "fullname_down" in filter_dropdown_menu:
                        queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                            'lastname_uk').reverse()
                    else:
                        if "gsh_down" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                                'h_index_google_scholar')
                        else:
                            if "gsh_up" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                                    'h_index_google_scholar').reverse()
                            else:
                                if "ph_down" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                                        'h_index_publons')
                                else:
                                    if "ph_up" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by(
                                            'h_index_publons').reverse()
                                    else:
                                        if "sh_down" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get(
                                                    "q")).order_by('h_index_scopus')
                                        else:
                                            if "sh_up" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get(
                                                        "q")).order_by('h_index_scopus').reverse()
            else:

                if "speciality" in select:
                    if "fullname_up" in filter_dropdown_menu:
                        queryset = Scientist.objects.filter(draft=False, lastname_uk__icontains=self.request.GET.get("q")).order_by(
                            'lastname_uk')
                    else:
                        if "fullname_down" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by(
                                'lastname_uk').reverse()
                        else:
                            if "gsh_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by(
                                    'h_index_google_scholar')
                            else:
                                if "gsh_up" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by(
                                        'h_index_google_scholar').reverse()
                                else:
                                    if "ph_down" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by(
                                            'h_index_publons')
                                    else:
                                        if "ph_up" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get(
                                                    "q")).order_by(
                                                'h_index_publons').reverse()
                                        else:
                                            if "sh_down" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get(
                                                        "q")).order_by(
                                                    'h_index_scopus')
                                            else:
                                                if "sh_up" in filter_dropdown_menu:
                                                    queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get(
                                                            "q")).order_by(
                                                        'h_index_scopus').reverse()
                else:

                    if "orcid" in select:
                        if "fullname_up" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by('lastname_uk')
                        else:
                            if "fullname_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by('lastname_uk').reverse()
                            else:
                                if "gsh_down" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                        'h_index_google_scholar')
                                else:
                                    if "gsh_up" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                            'h_index_google_scholar').reverse()
                                    else:
                                        if "ph_down" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                                'h_index_publons')
                                        else:
                                            if "ph_up" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                                    'h_index_publons').reverse()
                                            else:
                                                if "sh_down" in filter_dropdown_menu:
                                                    queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                                        'h_index_scopus')
                                                else:
                                                    if "sh_up" in filter_dropdown_menu:
                                                        queryset = Scientist.objects.filter(draft=False, orcid__icontains=self.request.GET.get("q")).order_by(
                                                            'h_index_scopus').reverse()

        return queryset


class ProfilePage(View):
    """Сторінка вченого"""

    def get(self, request, profile_id):
        profile_scientist = Scientist.objects.get(profile_id=profile_id)
        context = {
            'scientist': profile_scientist
        }
        return render(request, 'profilePage.html', context)


def information(request):
    """Сторінка довідки"""
    return render(request, 'informationPage.html')


def report(request):
    """Сторінка звітів"""
    return render(request, 'reportPage.html')


def export(request):
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename=download.csv'
    writer.writerow(
        ['Кафедра', 'ПІБ', 'ПІБ En', 'ORCID', 'Google Scholar', 'GS h-index', 'GS кількість публікацій', 'Publons',
         'Publons h-index', 'Publons кідькість публікацій', 'Scopus', 'Scopus h-index', 'Scopus кількість публікацій'])

    for scientist in Scientist.objects.filter(draft=False).values_list('department__title_department',
                                                                       'lastname_uk', 'lastname_en', 'orcid',
                                                                       'google_scholar',
                                                                       'h_index_google_scholar',
                                                                       'google_scholar_count_pub',
                                                                       'publons', 'h_index_publons',
                                                                       'publons_count_pub', 'scopusid',
                                                                       'h_index_scopus', 'scopus_count_pub'):
        writer.writerow(scientist)

    return response


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Report.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Звіт')
    font_style = xlwt.easyxf(
        'font: bold on; font: name Times New Roman; font: height 260; align: vert centre; align: horiz center; align: wrap yes; borders: left thin, right thin, top thin, bottom thin')
    columns = ['Факультет (Інститут)', 'Кафедра, відділ тощо',
               'Прізвище ім\'я, по батькові науково-педагогічного працівника', 'ID Scopus', 'Індекс Гірша Scopus',
               'ID Web of Science',
               'Індекс Гірша Web of Science']
    row_num = 0

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.easyxf(
        ' font: name Times New Roman; font: height 240; align: vert centre; align: horiz center; align: wrap yes; borders: left thin, right thin, top thin, bottom thin')
    rows = Scientist.objects.filter(draft=False).order_by('lastname_uk').values_list(
        'department__faculty__title_faculty', 'department__title_department',
        'lastname_uk',
        'scopusid',
        'h_index_scopus',
        'publons', 'h_index_publons'
    )

    for row in rows:
        row_num += 1
        ws.row(row_num).height = 256 * 6
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    ws.col(0).width = 256 * 24
    ws.col(1).width = 256 * 22
    ws.col(2).width = 256 * 52
    ws.col(3).width = 256 * 15
    ws.col(4).width = 256 * 16
    ws.col(5).width = 256 * 16
    ws.col(6).width = 256 * 19
    ws.row(0).height = 256 * 5
    wb.save(response)

    return response


