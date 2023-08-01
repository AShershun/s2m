# import io
# import csv
import openpyxl
import pandas as pd
import pybliometrics

from datetime import datetime

from .forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from django.db.models.functions import Concat
from django.db.models import F, Value
from .models import Department, PublicationScopus, Scientist, Speciality, PublicationWos, ScientistPublicationScopus, ScientistPublicationWos
from openpyxl.styles import Alignment, Font, Border
#from pybliometrics.scopus import ScopusAuthor
from pybliometrics.scopus import *
from wos import *


class MainPage(View):
    """Отримання даних вчених для побудови графіку"""

    def get(self, request):
        google_scholar_h = Scientist.objects.all().order_by('h_index_google_scholar', 'lastname_uk').filter(
            h_index_google_scholar__isnull=False, draft=False).reverse()[:10]
        scopus_h = Scientist.objects.all().order_by('h_index_scopus', 'lastname_uk').filter(h_index_scopus__isnull=False, draft=False).reverse()[:10]
        publons_h = Scientist.objects.all().order_by('h_index_publons', 'lastname_uk').filter(h_index_publons__isnull=False, draft=False).reverse()[:10]
        publons = Scientist.objects.all().order_by('publons_count_pub', 'lastname_uk').filter(publons_count_pub__isnull=False, draft=False).reverse()[:10]
        scopus = Scientist.objects.all().order_by('scopus_count_pub', 'lastname_uk').filter(scopus_count_pub__isnull=False, draft=False).reverse()[:10]

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
            # Publons Publications Top
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

            # Scopus Publications Top
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

            # Scopus h index
            'scientist_scopus_h_1': (scopus_h[0].lastname_uk + " " + scopus_h[0].firstname_uk + " " + scopus_h[0].middlename_uk),
            'scientist_scopus_h_2': (scopus_h[1].lastname_uk + " " + scopus_h[1].firstname_uk + " " + scopus_h[1].middlename_uk),
            'scientist_scopus_h_3': (scopus_h[2].lastname_uk + " " + scopus_h[2].firstname_uk + " " + scopus_h[2].middlename_uk),
            'scientist_scopus_h_4': (scopus_h[3].lastname_uk + " " + scopus_h[3].firstname_uk + " " + scopus_h[3].middlename_uk),
            'scientist_scopus_h_5': (scopus_h[4].lastname_uk + " " + scopus_h[4].firstname_uk + " " + scopus_h[4].middlename_uk),
            'scientist_scopus_h_6': (scopus_h[5].lastname_uk + " " + scopus_h[5].firstname_uk + " " + scopus_h[5].middlename_uk),
            'scientist_scopus_h_7': (scopus_h[6].lastname_uk + " " + scopus_h[6].firstname_uk + " " + scopus_h[6].middlename_uk),
            'scientist_scopus_h_8': (scopus_h[7].lastname_uk + " " + scopus_h[7].firstname_uk + " " + scopus_h[7].middlename_uk),
            'scientist_scopus_h_9': (scopus_h[8].lastname_uk + " " + scopus_h[8].firstname_uk + " " + scopus_h[8].middlename_uk),
            'scientist_scopus_h_10': (scopus_h[9].lastname_uk + " " + scopus_h[9].firstname_uk + " " + scopus_h[9].middlename_uk),
            'scopus_h_1': scopus_h[0].h_index_scopus,
            'scopus_h_2': scopus_h[1].h_index_scopus,
            'scopus_h_3': scopus_h[2].h_index_scopus,
            'scopus_h_4': scopus_h[3].h_index_scopus,
            'scopus_h_5': scopus_h[4].h_index_scopus,
            'scopus_h_6': scopus_h[5].h_index_scopus,
            'scopus_h_7': scopus_h[6].h_index_scopus,
            'scopus_h_8': scopus_h[7].h_index_scopus,
            'scopus_h_9': scopus_h[8].h_index_scopus,
            'scopus_h_10': scopus_h[9].h_index_scopus,
            'scopus_profile_id_h_1': scopus_h[0].profile_id,
            'scopus_profile_id_h_2': scopus_h[1].profile_id,
            'scopus_profile_id_h_3': scopus_h[2].profile_id,
            'scopus_profile_id_h_4': scopus_h[3].profile_id,
            'scopus_profile_id_h_5': scopus_h[4].profile_id,
            'scopus_profile_id_h_6': scopus_h[5].profile_id,
            'scopus_profile_id_h_7': scopus_h[6].profile_id,
            'scopus_profile_id_h_8': scopus_h[7].profile_id,
            'scopus_profile_id_h_9': scopus_h[8].profile_id,
            'scopus_profile_id_h_10': scopus_h[9].profile_id,

            # Publons h index
            'scientist_publons_h_1': (publons_h[0].lastname_uk + " " + publons_h[0].firstname_uk + " " + publons_h[0].middlename_uk),
            'scientist_publons_h_2': (publons_h[1].lastname_uk + " " + publons_h[1].firstname_uk + " " + publons_h[1].middlename_uk),
            'scientist_publons_h_3': (publons_h[2].lastname_uk + " " + publons_h[2].firstname_uk + " " + publons_h[2].middlename_uk),
            'scientist_publons_h_4': (publons_h[3].lastname_uk + " " + publons_h[3].firstname_uk + " " + publons_h[3].middlename_uk),
            'scientist_publons_h_5': (publons_h[4].lastname_uk + " " + publons_h[4].firstname_uk + " " + publons_h[4].middlename_uk),
            'scientist_publons_h_6': (publons_h[5].lastname_uk + " " + publons_h[5].firstname_uk + " " + publons_h[5].middlename_uk),
            'scientist_publons_h_7': (publons_h[6].lastname_uk + " " + publons_h[6].firstname_uk + " " + publons_h[6].middlename_uk),
            'scientist_publons_h_8': (publons_h[7].lastname_uk + " " + publons_h[7].firstname_uk + " " + publons_h[7].middlename_uk),
            'scientist_publons_h_9': (publons_h[8].lastname_uk + " " + publons_h[8].firstname_uk + " " + publons_h[8].middlename_uk),
            'scientist_publons_h_10': (publons_h[9].lastname_uk + " " + publons_h[9].firstname_uk + " " + publons_h[9].middlename_uk),
            'publons_h_1': publons_h[0].h_index_publons,
            'publons_h_2': publons_h[1].h_index_publons,
            'publons_h_3': publons_h[2].h_index_publons,
            'publons_h_4': publons_h[3].h_index_publons,
            'publons_h_5': publons_h[4].h_index_publons,
            'publons_h_6': publons_h[5].h_index_publons,
            'publons_h_7': publons_h[6].h_index_publons,
            'publons_h_8': publons_h[7].h_index_publons,
            'publons_h_9': publons_h[8].h_index_publons,
            'publons_h_10': publons_h[9].h_index_publons,
            'publons_profile_id_h_1': publons_h[0].profile_id,
            'publons_profile_id_h_2': publons_h[1].profile_id,
            'publons_profile_id_h_3': publons_h[2].profile_id,
            'publons_profile_id_h_4': publons_h[3].profile_id,
            'publons_profile_id_h_5': publons_h[4].profile_id,
            'publons_profile_id_h_6': publons_h[5].profile_id,
            'publons_profile_id_h_7': publons_h[6].profile_id,
            'publons_profile_id_h_8': publons_h[7].profile_id,
            'publons_profile_id_h_9': publons_h[8].profile_id,
            'publons_profile_id_h_10': publons_h[9].profile_id,

            # Google Scholar h index
            'scientist_google_scholar_h_1': (
                google_scholar_h[0].lastname_uk + " " + google_scholar_h[0].firstname_uk + " " + google_scholar_h[0].middlename_uk),
            'scientist_google_scholar_h_2': (
                google_scholar_h[1].lastname_uk + " " + google_scholar_h[1].firstname_uk + " " + google_scholar_h[1].middlename_uk),
            'scientist_google_scholar_h_3': (
                google_scholar_h[2].lastname_uk + " " + google_scholar_h[2].firstname_uk + " " + google_scholar_h[2].middlename_uk),
            'scientist_google_scholar_h_4': (
                google_scholar_h[3].lastname_uk + " " + google_scholar_h[3].firstname_uk + " " + google_scholar_h[3].middlename_uk),
            'scientist_google_scholar_h_5': (
                google_scholar_h[4].lastname_uk + " " + google_scholar_h[4].firstname_uk + " " + google_scholar_h[4].middlename_uk),
            'scientist_google_scholar_h_6': (
                google_scholar_h[5].lastname_uk + " " + google_scholar_h[5].firstname_uk + " " + google_scholar_h[5].middlename_uk),
            'scientist_google_scholar_h_7': (
                google_scholar_h[6].lastname_uk + " " + google_scholar_h[6].firstname_uk + " " + google_scholar_h[6].middlename_uk),
            'scientist_google_scholar_h_8': (
                google_scholar_h[7].lastname_uk + " " + google_scholar_h[7].firstname_uk + " " + google_scholar_h[7].middlename_uk),
            'scientist_google_scholar_h_9': (
                google_scholar_h[8].lastname_uk + " " + google_scholar_h[8].firstname_uk + " " + google_scholar_h[8].middlename_uk),
            'scientist_google_scholar_h_10': (
                google_scholar_h[9].lastname_uk + " " + google_scholar_h[9].firstname_uk + " " + google_scholar_h[9].middlename_uk),
            'google_scholar_h_1': google_scholar_h[0].h_index_google_scholar,
            'google_scholar_h_2': google_scholar_h[1].h_index_google_scholar,
            'google_scholar_h_3': google_scholar_h[2].h_index_google_scholar,
            'google_scholar_h_4': google_scholar_h[3].h_index_google_scholar,
            'google_scholar_h_5': google_scholar_h[4].h_index_google_scholar,
            'google_scholar_h_6': google_scholar_h[5].h_index_google_scholar,
            'google_scholar_h_7': google_scholar_h[6].h_index_google_scholar,
            'google_scholar_h_8': google_scholar_h[7].h_index_google_scholar,
            'google_scholar_h_9': google_scholar_h[8].h_index_google_scholar,
            'google_scholar_h_10': google_scholar_h[9].h_index_google_scholar,
            'google_scholar_profile_id_h_1': google_scholar_h[0].profile_id,
            'google_scholar_profile_id_h_2': google_scholar_h[1].profile_id,
            'google_scholar_profile_id_h_3': google_scholar_h[2].profile_id,
            'google_scholar_profile_id_h_4': google_scholar_h[3].profile_id,
            'google_scholar_profile_id_h_5': google_scholar_h[4].profile_id,
            'google_scholar_profile_id_h_6': google_scholar_h[5].profile_id,
            'google_scholar_profile_id_h_7': google_scholar_h[6].profile_id,
            'google_scholar_profile_id_h_8': google_scholar_h[7].profile_id,
            'google_scholar_profile_id_h_9': google_scholar_h[8].profile_id,
            'google_scholar_profile_id_h_10': google_scholar_h[9].profile_id,

        }
        return render(request, "mainPage.html", context)


class ScientistsPage(ListView):
    """Перелік вчених"""

    model = Scientist
    queryset = Scientist.objects.order_by('lastname_uk').filter(draft=False)
    context_object_name = "scientist_list"
    template_name = "scientistsPage.html"
    paginate_by = 15

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['scientists_counter'] = self.queryset.count()
        context['form'] = SelectForm(initial={
            'select': self.request.GET.get('select', ''),
        })

        return context


class Search(ListView):
    """Пошук вчених та сортування за ознаками"""

    context_object_name = "scientist_list"
    paginate_by = 15
    template_name = "scientistsPage.html"

    def get_queryset(self):
        queryset = ""
        select = self.request.GET.get('select')
        filter_dropdown_menu = self.request.GET.get('filter')
        if "fullname" in select:
            if "fullname_up" in filter_dropdown_menu:
                queryset = Scientist.objects.annotate(
                    fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by("lastname_uk")
            else:
                if "fullname_down" in filter_dropdown_menu:
                    queryset = Scientist.objects.annotate(
                        fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('lastname_uk').reverse()
                else:
                    if "gsh_down" in filter_dropdown_menu:
                        queryset = Scientist.objects.annotate(
                            fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar')
                    else:
                        if "gsh_up" in filter_dropdown_menu:
                            queryset = Scientist.objects.annotate(
                                fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar').reverse()
                        else:
                            if "ph_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.annotate(fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('h_index_publons')
                            else:
                                if "ph_up" in filter_dropdown_menu:
                                    queryset = Scientist.objects.annotate(fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by().order_by('h_index_publons').reverse()
                                else:
                                    if "sh_down" in filter_dropdown_menu:
                                        queryset = Scientist.objects.annotate(fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('h_index_scopus')
                                    else:
                                        if "sh_up" in filter_dropdown_menu:
                                            queryset = Scientist.objects.annotate(fullname_uk=Concat(F('lastname_uk'), Value(' '), F('firstname_uk'), Value(' '), F('middlename_uk'))).filter(draft=False, fullname_uk__icontains=self.request.GET.get("q")).order_by('h_index_scopus').reverse()
        else:

            if "department" in select:
                if "fullname_up" in filter_dropdown_menu:
                    queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('lastname_uk')
                else:
                    if "fullname_down" in filter_dropdown_menu:
                        queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('lastname_uk').reverse()
                    else:
                        if "gsh_down" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar')
                        else:
                            if "gsh_up" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar').reverse()
                            else:
                                if "ph_down" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_publons')
                                else:
                                    if "ph_up" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_publons').reverse()
                                    else:
                                        if "sh_down" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_scopus')
                                        else:
                                            if "sh_up" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, department__title_department__icontains=self.request.GET.get("q")).order_by('h_index_scopus').reverse()
            else:

                if "speciality" in select:
                    if "fullname_up" in filter_dropdown_menu:
                        queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('lastname_uk')
                    else:
                        if "fullname_down" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('lastname_uk').reverse()
                        else:
                            if "gsh_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar')
                            else:
                                if "gsh_up" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar').reverse()
                                else:
                                    if "ph_down" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_publons')
                                    else:
                                        if "ph_up" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_publons').reverse()
                                        else:
                                            if "sh_down" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_scopus')
                                            else:
                                                if "sh_up" in filter_dropdown_menu:
                                                    queryset = Scientist.objects.filter(draft=False, speciality__speciality_title__icontains=self.request.GET.get("q")).order_by('h_index_scopus').reverse()
                else:

                    if "keyword" in select:
                        if "fullname_up" in filter_dropdown_menu:
                            queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('lastname_uk')
                        else:
                            if "fullname_down" in filter_dropdown_menu:
                                queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('lastname_uk').reverse()
                            else:
                                if "gsh_down" in filter_dropdown_menu:
                                    queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar')
                                else:
                                    if "gsh_up" in filter_dropdown_menu:
                                        queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_google_scholar').reverse()
                                    else:
                                        if "ph_down" in filter_dropdown_menu:
                                            queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_publons')
                                        else:
                                            if "ph_up" in filter_dropdown_menu:
                                                queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_publons').reverse()
                                            else:
                                                if "sh_down" in filter_dropdown_menu:
                                                    queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_scopus')
                                                else:
                                                    if "sh_up" in filter_dropdown_menu:
                                                        queryset = Scientist.objects.filter(draft=False, speciality__keyword__keyword_title__icontains=self.request.GET.get("q")).order_by('h_index_scopus').reverse()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['scientists_counter'] = self.get_queryset().count()
        context['form'] = SelectForm(initial={
            'select': self.request.GET.get('select', ''),
        })
        return context


@login_required(login_url='/accounts/login/')
def update_scientists_records(request):
    scientists = Scientist.objects.all().filter(draft=False)
    for scientist in scientists:
        scopus_id = scientist.scopusid
        # print("Update " + scientist.profile_id + scientist.lastname_uk)
        if scopus_id:
            try:
                scopus_author = AuthorRetrieval(scopus_id)

                # Зміненя даних у БД index, кількості
                scientist.h_index_scopus = scopus_author.h_index
                scientist.scopus_count_pub = scopus_author.document_count
                scientist.save()
                print("Success!!!!!!!")

            except Exception as e:
                print(f"Error updating data for {scientist.lastname_uk}: {e}")
        # else:
        #     print("Empty")

    return HttpResponse("Update completed successfully.")


''


class ProfilePage(View):
    """Сторінка вченого з усіма його даними"""

    def get(self, request, profile_id):
        profile_scientist = Scientist.objects.get(profile_id=profile_id)
        context = {
            'scientist': profile_scientist,
        }
        return render(request, 'profilePage.html', context)

    def post(self, request, profile_id):
        #api_scpopus_key = '5e5dc847f87e9db2f294456be2b932e4'

        # Web of Science

        # wos_api_key = 'your_web_of_science_api_key'
        # wos_id = Scientist.objects.get(profile_id=profile_id).publons
        # if wos_id:
        #     # wos_client = WosClient()

        #     # author_info = wos_client.retrieve_author(wos_id)

        #     # h_index = author_info.get('h_index', 0)
        #     # publication_count = author_info.get('document_count', 0)

        #     # # Обновляем поля в базе данных Django
        #     # scientist = Scientist.objects.get(profile_id=profile_id)
        #     # scientist.h_index_wos = h_index
        #     # scientist.publication_count_wos = publication_count
        #     # scientist.save()
        #     client = WosClient(wos_api_key)

        #     # Получаем данные о публикациях автора по его WOS ID
        #     query = f"AU_ID({wos_id})"
        #     response = client.search(query)

        #     if response.get('records_found', 0) > 0:
        #         record = response['records'][0]

        #         h_index = record.get('h_index', 0)
        #         publication_count = record.get('document_count', 0)

        #         scientist = Scientist.objects.get(profile_id=profile_id)
        #         scientist.h_index_publons = h_index
        #         scientist.publons_count_pub = publication_count
        #         scientist.save()

        # Scopus
        # Отримання необхідного scopusid за profile_id
        scopus_id = Scientist.objects.get(profile_id=profile_id).scopusid
        if scopus_id:
            scopus_author = AuthorRetrieval(scopus_id)

            # Зміненя даних у БД та збереження
            scientist = Scientist.objects.get(profile_id=profile_id)
            scientist.h_index_scopus = scopus_author.h_index
            scientist.scopus_count_pub = scopus_author.document_count
            scientist.save()

        return redirect('profile', profile_id=profile_id)


def information(request):
    """Сторінка довідки"""
    return render(request, 'informationPage.html')


def report(request):
    """Сторінка звітів"""
    return render(request, 'reportPage.html')


@login_required(login_url='/accounts/login/')
def export_xlsx(request):
    '''Генерація файлу .xlsx з данми кожного вченого окрім тих які позначені як draft'''

    # Створюємо  Workbook
    workbook = openpyxl.Workbook()

    # Створюємо лист (worksheet)
    worksheet = workbook.active
    worksheet.title = "Звіт"

    queryset = Scientist.objects.filter(draft=False).prefetch_related(
        'department__faculty').order_by('lastname_uk')

    # Створюємо порожній DataFrame для зберігання даних
    data = pd.DataFrame(columns=['Факультет (Інститут)', 'Кафедра, відділ тощо', 'ПІБ', 'ID Scopus', 'Індекс Гірша Scopus',
                                 'Кількість публікацій Scopus', 'ID Web of Science',
                                 'Індекс Гірша Web of Science', 'Кількість публікацій WoS', 'Публікації Scopus', 'Публікації WoS'])

    # Заповнюємо DataFrame даними із queryset
    for scientist in queryset:

        full_name = ' '.join(
            [scientist.lastname_uk, scientist.firstname_uk, scientist.middlename_uk])
        title_department = scientist.department.title_department if scientist.department else ''
        title_faculty = scientist.department.faculty.title_faculty if scientist.department.faculty else ''

        # Отримуємо всі назви публікацій та об'єднуємо їх в один рядок
        scopus_publication_titles = ',\n'.join(
            [f"{index+1}. {publication.publication_title}" for index, publication in enumerate(scientist.publication_wos.all())])
        wos_publication_titles = ',\n'.join(
            [f"{index+1}. {publication.publication_title}" for index, publication in enumerate(scientist.publication_scopus.all())])

        # Додаємо дані в DataFrame
        data.loc[len(data)] = [title_faculty, title_department, full_name, scientist.scopusid, scientist.h_index_scopus,
                               scientist.scopus_count_pub, scientist.publons, scientist.h_index_publons,
                               scientist.publons_count_pub, scopus_publication_titles, wos_publication_titles]

    # worksheet.column_dimensions.group('A', 'B', hidden=True, outline_level=0)
    worksheet.column_dimensions['A'].width = 40
    worksheet.column_dimensions['B'].width = 35

    # worksheet.column_dimensions.group('C', 'D', hidden=True, outline_level=0)
    worksheet.column_dimensions['C'].width = 40
    worksheet.column_dimensions['D'].width = 18

    # worksheet.column_dimensions.group('E', 'I', hidden=True, outline_level=0)
    worksheet.column_dimensions['E'].width = 18
    worksheet.column_dimensions['F'].width = 18
    worksheet.column_dimensions['G'].width = 18
    worksheet.column_dimensions['H'].width = 18
    worksheet.column_dimensions['I'].width = 18

    # worksheet.column_dimensions.group('J', 'K', hidden=True, outline_level=0)
    worksheet.column_dimensions['J'].width = 85
    worksheet.column_dimensions['K'].width = 85

    # Форматування комірок
    border = Border(left=openpyxl.styles.Side(border_style='thin'), right=openpyxl.styles.Side(
        border_style='thin'), top=openpyxl.styles.Side(border_style='thin'), bottom=openpyxl.styles.Side(border_style='thin'))
    alignment = Alignment(horizontal='center',
                          vertical='center', wrap_text=True)
    font = Font(size=12)

    # Встановлення висоти комірок
    endRow = 800
    for i in range(0, endRow):
        worksheet.row_dimensions[i+1].height = 58

    # Заповнюємо таблицю Excel даними з DataFrame
    start_row_index = 2
    for row in data.itertuples(index=False):
        row_index = start_row_index
        for col_index, value in enumerate(row, start=1):
            cell = worksheet.cell(row=row_index, column=col_index)
            cell.value = value

        start_row_index += 1

    # Застосовуємо форматування для кожного стовпця
    for column in worksheet.columns:
        for cell in column:
            cell.border = border
            cell.alignment = alignment
            cell.font = font

    headers = ['Факультет (Інститут)', 'Кафедра, відділ тощо', 'ПІБ', 'ID Scopus', 'Індекс Гірша Scopus',
               'Кількість публікацій Scopus', 'ID Web of Science',
               'Індекс Гірша Web of Science', 'Кількість публікацій WoS', 'Публікації Scopus', 'Публікації WoS']

    # Застосовуємо форматування для першого рядка
    row_index = 1
    for col_index, header in enumerate(headers, start=1):
        cell = worksheet.cell(row=row_index, column=col_index)
        cell.value = header
        cell.font = Font(bold=True, size=13)

    for cell in worksheet['D'][1:]:
        cell.font = Font(underline='single', color='0563C1')
        cell.hyperlink = f"https://www.scopus.com/authid/detail.uri?authorId={cell.value}"

    for cell in worksheet['G'][1:]:
        cell.font = Font(underline='single', color='0563C1')
        cell.hyperlink = f"https://publons.com/researcher/{cell.value}"

    filename = "Zvit" + datetime.now().strftime("_%d_%m_%Y") + ".xlsx"
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    workbook.save(response)

    return response


@login_required(login_url='/accounts/login/')
def naukometria_xlsx(request):
    '''Генерація файлу .xlsx з данми кожного вченого окрім тих які позначені як draft'''

    # Створюємо  Workbook
    workbook = openpyxl.Workbook()

    # Створюємо лист (worksheet)
    worksheet = workbook.active
    worksheet.title = "Наукометрія"

    queryset = Scientist.objects.filter(draft=False).prefetch_related(
        'department__faculty__institute').order_by('lastname_uk')

    # Створюємо порожній DataFrame для зберігання даних
    data = pd.DataFrame(columns=['Інститут', 'Кафедра', 'ПІБ', 'Ступінь', 'Посади', 'Google Scholar', 'GS h-index', 'Кількість публікацій GS',
                        'ORCID', 'ID Scopus', 'Scopus h-index', 'Кількість публікацій Scopus', 'Researcher ID', 'WoS h-index', 'Кількість публікацій WoS'])

    # Заповнюємо DataFrame даними із queryset
    for scientist in queryset:

        full_name = ' '.join(
            [scientist.lastname_uk, scientist.firstname_uk, scientist.middlename_uk])
        title_department = scientist.department.title_department if scientist.department else ''
        title_institute = scientist.department.faculty.institute.abbreviation if scientist.department.faculty.institute else ''
        title_degree = scientist.degree.title_degree if scientist.degree else ''
        title_post = scientist.post.title_post if scientist.post else ''

        if len(data) > 0:
            data.loc[len(data)] = [title_institute, title_department, full_name, title_degree, title_post, scientist.google_scholar, scientist.h_index_google_scholar, scientist.google_scholar_count_pub, scientist.orcid, scientist.scopusid, scientist.h_index_scopus,
                                   scientist.scopus_count_pub, scientist.publons, scientist.h_index_publons,
                                   scientist.publons_count_pub]
        else:
            data.loc[0] = [title_institute, title_department, full_name, title_degree, title_post, scientist.google_scholar, scientist.h_index_google_scholar, scientist.google_scholar_count_pub, scientist.orcid, scientist.scopusid, scientist.h_index_scopus,
                           scientist.scopus_count_pub, scientist.publons, scientist.h_index_publons,
                           scientist.publons_count_pub]

    # worksheet.column_dimensions.group('A', 'B', hidden=True, outline_level=0)
    worksheet.column_dimensions['A'].width = 18
    worksheet.column_dimensions['B'].width = 18

    # worksheet.column_dimensions.group('C', 'D', hidden=True, outline_level=0)
    worksheet.column_dimensions['C'].width = 24
    worksheet.column_dimensions['D'].width = 14

    # worksheet.column_dimensions.group('E', 'I', hidden=True, outline_level=0)
    worksheet.column_dimensions['E'].width = 12
    worksheet.column_dimensions['F'].width = 10
    worksheet.column_dimensions['G'].width = 10
    worksheet.column_dimensions['H'].width = 16
    worksheet.column_dimensions['I'].width = 22
    worksheet.column_dimensions['J'].width = 16

    # worksheet.column_dimensions.group('J', 'K', hidden=True, outline_level=0)
    worksheet.column_dimensions['K'].width = 12
    worksheet.column_dimensions['L'].width = 16
    worksheet.column_dimensions['M'].width = 16
    worksheet.column_dimensions['N'].width = 10
    worksheet.column_dimensions['O'].width = 16

    # Форматування комірок
    border = Border(left=openpyxl.styles.Side(border_style='thin'), right=openpyxl.styles.Side(
        border_style='thin'), top=openpyxl.styles.Side(border_style='thin'), bottom=openpyxl.styles.Side(border_style='thin'))
    alignment = Alignment(horizontal='center',
                          vertical='center', wrap_text=True)
    font = Font(size=12)

    # Встановлення висоти комірок
    endRow = 800
    for i in range(0, endRow):
        worksheet.row_dimensions[i+1].height = 58

    # Заповнюємо таблицю Excel даними з DataFrame
    start_row_index = 2
    for row in data.itertuples(index=False):
        row_index = start_row_index
        for col_index, value in enumerate(row, start=1):
            cell = worksheet.cell(row=row_index, column=col_index)
            cell.value = value

        start_row_index += 1

    # Застосовуємо форматування для кожного стовпця
    for column in worksheet.columns:
        for cell in column:
            cell.border = border
            cell.alignment = alignment
            cell.font = font

    headers = ['Інститут', 'Кафедра', 'ПІБ', 'Ступінь', 'Посади', 'Google Scholar', 'GS h-index', 'Кількість публікацій GS', 'ORCID',
               'ID Scopus', 'Scopus h-index', 'Кількість публікацій Scopus', 'Researcher ID', 'WoS h-index', 'Кількість публікацій WoS']

    # Застосовуємо форматування для першого рядка
    row_index = 1
    for col_index, header in enumerate(headers, start=1):
        cell = worksheet.cell(row=row_index, column=col_index)
        cell.value = header
        cell.font = Font(bold=True, size=12)

    for cell in worksheet['F'][1:]:
        cell.font = Font(underline='single', color='0563C1')
        cell.hyperlink = f"https://scholar.google.com/{cell.value}"
        if cell.value:
            cell.value = 'Link'

    for cell in worksheet['J'][1:]:
        cell.font = Font(underline='single', color='0563C1')
        cell.hyperlink = f"https://www.scopus.com/authid/detail.uri?authorId={cell.value}"

    for cell in worksheet['M'][1:]:
        cell.font = Font(underline='single', color='0563C1')
        cell.hyperlink = f"https://publons.com/researcher/{cell.value}"

    for cell in worksheet['A'][1:]:
        cell.font = Font(size=11)

    for cell in worksheet['B'][1:]:
        cell.font = Font(size=10)

    for cell in worksheet['D'][1:]:
        cell.font = Font(size=10)

    for cell in worksheet['E'][1:]:
        cell.font = Font(size=10)

    for cell in worksheet['I'][1:]:
        cell.font = Font(size=11, underline='single', color='0563C1')
        cell.hyperlink = f"https://orcid.org/{cell.value}"

    filename = "Scientometrics" + datetime.now().strftime("_%d_%m_%Y") + ".xlsx"
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    workbook.save(response)

    return response
