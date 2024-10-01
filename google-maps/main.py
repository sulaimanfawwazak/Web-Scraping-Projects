from playwright.sync_api import sync_playwright # To automate the browser
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse

@dataclass # This decorator makes us don't have to write the dunder methods (__init__, __eq__, __repr__, etc.)
class Business:
  name: str = None
  address: str = None
  website: str = None
  phone_nuumber: str = None

@dataclass
class BusinessList:
  # This line is to make an array of `Business` object`
  business_list: list[Business] = field(default_factory=list) # The `field` is to initialize a new array for every instance ever

  # Function to return pandas dataframe
  def dataframe(self):
    return pd.json_normalize((asdict(business) for business in self.business_list), sep='_')
  
  # Function to save the dataframe as Excel
  def saveToExcel(self, filename):
    self.dataframe().to_excel(f'{filename}.xlsx', index=False)
  
  # Function to save the dataframe as CSV
  def saveToCSV(self, filename):
    self.dataframe().to_csv(f'{filename}.csv', index=False)

def main():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://www.google.com/maps', timeout=60000) # Time in milliseconds
    page.wait_for_timeout(5000) 

    page.locator('//input[@id="searchboxinput"]').fill(search_for)
    page.wait_for_timeout(3000)

    page.keyboard.press('Enter')
    page.wait_for_timeout(5000)

    listings = page.locator('//div[@role="article"]').all()
    print(f'Number of listings: {len(listings)}')

    business_list = BusinessList()

    for listing in listings[:5]: # Only take 5 lists
      listing.click()
      page.wait_for_timeout(5000) # Wait for 5 seconds

      name_xpath = '//h1[contains(@class, "fontHeadlineLarge")]/span[2]'
      address_xpath = '//button[@adta-item-id="address"]//div[contains(@class, "font)]'
      website_xpath = ''
      phone_number_xpath = ''


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--search', type=str)
  parser.add_argument('-l', '--location', type=str)
  args = parser.parse_args()

  if args.location and args.search:
    search_for = f'{args.search} {args.location}'
  else:
    search_for = 'dentist new york'

  main()