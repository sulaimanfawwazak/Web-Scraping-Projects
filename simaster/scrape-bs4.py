import requests
from bs4 import BeautifulSoup

URL = 'https://simaster.ugm.ac.id/elearning/pembelajaran/detail/g73uWCWRBCRctCGQhhS6V-jZvaaMXa-YgQqT_wUCtc4='

try:
  response = requests.get(URL)

except Exception as e:
  print(e)

soup = BeautifulSoup(response.text, 'html.parser')

entries = soup.find_all('div', class_='widget-support-tickets-item')

for entry in entries:
  name = entry.find('b').text.strip()
  nim = entry.find('span').text.strip()

  print(f'Name: {name} | NIM: {nim}')