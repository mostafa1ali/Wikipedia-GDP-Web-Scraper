import requests 
import pandas as pd
from bs4 import BeautifulSoup
import csv
import re

url = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

def clean_footnotes(text):
    return re.sub(r'\[\d+\]', '', text)

def convertion(gdp_str):
    if pd.isna(gdp_str) or gdp_str in ('_', '-', '—', '', '—'):  
        return None
    return int(str(gdp_str).replace(',', ''))

def Scrape(url):
    src = url.content
    soup = BeautifulSoup(src, 'lxml')

    tables = soup.find_all('table', {'class' : 'wikitable'})
    imf_table = tables[0]
    
    headers = []
    headers_row = imf_table.find('tr')
    for header in headers_row.find_all('th'):
        headers.append(header.text.strip())
    
    countries = []
    gdps = []
    for row in imf_table.find_all('tr')[2:]:
        country = row.contents[1].text.strip()
        gdp = row.contents[3].text.strip()

        country = clean_footnotes(country)
        gdp = clean_footnotes(gdp)
        gdp = convertion(gdp)

        countries.append(country)
        gdps.append(gdp)

    df = pd.DataFrame({'Country/Territory': countries, 'GDP (US$ millions)': gdps})
    
    df.to_csv('Wikipedia_GDeP.csv', index=False, encoding='utf-8')



def main():
    Scrape(url)

main()