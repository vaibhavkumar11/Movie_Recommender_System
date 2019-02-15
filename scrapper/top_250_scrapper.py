import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
title = html_soup.find_all('td', 'titleColumn')

all_links = []
for i in title:
    link = i.a['href'][7:16]
    all_links.append(link)

with open('250links.csv', 'w') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    wr.writerow(['links'])
    for val in all_links:
        wr.writerow([val])
