from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# The structure of the table is like this
# <table id='example2'>
#   <thead><thead/>
#   <tbody>
#     <tr>
#       <td><td/>
#       <td><td/>
#       <td><td/>
#       ...
#     <tr/>
#     <tr>
#       <td><td/>
#       <td><td/>
#       <td><td/>
#       ...
#     <tr/>
#   <tbody/>
# <table/>

table = soup.find('table', {'id': 'example2'})
data = table.find('tbody')
rows = data.find_all('tr')

countries_list = list()

for row in rows:
  country_dict = dict()

  country_dict['Country'] = row.find_all('td')[1].text
  country_dict['Population'] = int(row.find_all('td')[2].text.replace(',', ''))
  country_dict['Density'] = float(row.find_all('td')[5].text.replace(',', ''))
  country_dict['Land Area'] = int(row.find_all('td')[6].text.replace(',', ''))
  country_dict['Urban Population'] = float(row.find_all('td')[-1].text.strip('%'))
  
  countries_list.append(country_dict)

# print(countries_list)


countries_df = pd.DataFrame(countries_list)
countries_df.to_csv('./world-population/countries_data.csv', index=False)
countries_df.to_excel('./world-population/countries_data.xlsx', index=False)