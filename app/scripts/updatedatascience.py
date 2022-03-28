import os
import requests
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'standalone_example.settings')
# django.setup()

from django.conf import settings
from app.models import *
# from bs4 import BeautifulSoup as BS

from django.db import models

# scopus_scientists = Scientist.objects.all()
# for i in scopus_scientists:
#     print(scopus_scientists)
# exec(open('/s2m/app/scripts/updatedatascience.py').read())