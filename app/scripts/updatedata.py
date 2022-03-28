import os
import requests

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.conf import settings
from app.models import Scientist
from bs4 import BeautifulSoup as BS

# scientist = Scientist.objects.get(id=1)
# scientist.google_scholar
HOST_GS = 'https://scholar.google.com/'
URL_GS = 'https://scholar.google.com/citations?user=t2raBWsAAAAJ&hl=uk'
HOST_SCOPUS = 'https://www.scopus.com/'
URL_SCOPUS = 'https://www.scopus.com/authid/detail.uri?authorId=7103160485'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# Google Scholar
def get_content_gs(html):
    soup = BS(html, 'html.parser')
    h_index_all = soup.select_one('tr:nth-child(2) .gsc_rsb_sc1+ .gsc_rsb_std').text
    # articles_num = soup.select_one('.gsc_rsb_m_a:nth-child(1) span').text.split(' ')[0]
    print(h_index_all)


# Scopus
def get_content_scopus(html):
    #soup = BS(html, 'html.parser')
    response = requests.get(html)
    soup = BS(response.text, 'lxml')
    # articles_num = soup.select('h3.MetricSection-module__3Ly5L').text
    #articles_num = soup.select_one('div:nth-of-type(2).MetricSection-module__29mr7 h3')
    # h_index_all = soup.select_one('div:nth-child(3) MetricSection-module__29mr7 MetricSection-module__3Ly5L').text
    #print(articles_num)
    # find_all_info_scopus = soup.find("div", class_="vertical-highlight padding-size-12-l")
    find_all_info_scopus = soup.find("h2")
    print(soup)


# # Publons
# def get_content_publons(html):
#     soup = BS(html, 'html.parser')
#     citations_all = soup.select_one('tr:nth-child(1) .gsc_rsb_sc1+ .gsc_rsb_std').text
#     h_index_all = soup.select_one('tr:nth-child(2) .gsc_rsb_sc1+ .gsc_rsb_std').text
#     # articles_num = soup.select_one('.gsc_rsb_m_a:nth-child(1) span').text.split(' ')[0]
#     print(citations_all, h_index_all)

# html = get_html(URL_GS)
# print("GS")
# get_content_gs(html.text)
html = get_html(URL_SCOPUS)
print("Scopus")
# get_content_scopus(html.text)
url = 'https://www.scopus.com/authid/detail.uri?authorId=7103160485'
response = requests.get(url)
soup = BS(response.text, 'lxml')
quotes = soup.find('h2')

print(quotes.text)
# scientist.google_scholar_count_pub =
# scientist.h_index_google_scholar = 14
# scientist.save()  # ['google_scholar_count_pub', 'h_index_google_scholar']
#exec(open('/s2m/app/scripts/updatedata.py').read())