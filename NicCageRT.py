import pandas as pd
import requests
import bs4
import lxml

session = requests.Session()
session.headers['User-Agent']

res = requests.get('https://www.rottentomatoes.com/celebrity/nicolas_cage')

soup = bs4.BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={'data-qa': 'celebrity-filmography-movies'})
table_body = table.find('tbody')

# Collect title, box office, release year, RT score and audience score using list comprehension
# Note: I choose to insert "NULL" because None is converted to 0 when uploaded into MySQL Workbench.
data_title = [item['data-title']
              for item in table.find_all('tr', attrs={'data-title': True})]
data_boxoffice = ['NULL' if item['data-boxoffice'] == '' else item['data-boxoffice']
                  for item in table.find_all('tr', attrs={'data-boxoffice': True})]
data_year = [item['data-year']
             for item in table.find_all('tr', attrs={'data-year': True})]

# The critic and audience scores will collect zero if no reviews were made made for the film.
# This is an issue since some of the movies have a zero rating because they were rated poorly
# by either critics or the audience. Therefore, additional parcing was needed in order to
# accurately reflect this discrepancy.
data_tomatometer = ['NULL' if (item.find_all('span', attrs={'data-tomatometer': 0}) and item.find_all('span', attrs={
                               'class': 'celebrity-filmography__no-score'})) else item['data-tomatometer'] for item in table.findAll('tr', attrs={'data-tomatometer': True})]

data_audiencescore = ['NULL' if (item.find_all('span', attrs={'data-audiencescore': 0}) and item.find_all('span', attrs={
                                 'class': 'celebrity-filmography__no-score'})) else item['data-audiencescore'] for item in table.findAll('tr', attrs={'data-audiencescore': True})]

# Create single list from collected data
data = list(zip(data_title, data_boxoffice, data_year,
            data_tomatometer, data_audiencescore))

# Create pandas dataframe from list
df = pd.DataFrame(
    data, columns=['Title', 'Boxoffice', 'ReleaseYear', 'RTScore', 'AudienceScore'])

# Save datafraome to .csv file
df.to_csv('NicCageRT_csv.csv')

# Save datafraome to excel file
df.to_csv('NicCageRT_xlsx.xlsx')
