from playwright.sync_api import sync_playwright

user_data_dir = '/home/pwnwas/.config/google-chrome'
# user_data_dir = '/home/pwnwas/.config/chromium'

def run(playwright):
  browser = playwright.chromium.launch_persistent_context(
    user_data_dir,
    headless=False)
  
  if not browser.pages:
    print(f'No pages open!')
    return 
  
  page = browser.pages[0]

  print(f'Current url: {page.url}')

  try:
    page.goto('https://simaster.ugm.ac.id/elearning/pembelajaran/detail/g73uWCWRBCRctCGQhhS6V-jZvaaMXa-YgQqT_wUCtc4=')
    page.wait_for_selector("#panelPeserta", timeout=10000)

    names = page.locator('div.widget-support-tickets-item b')
    nims = page.locator('div.widget-support-tickets-item span')

    if names.count() == 0 or nims.count() == 0:
      print(f'No names or nims found!')
      return

    for i in range(names.count()):
      name = names.nth(i).inner_text().strip()
      nim = nims.nth(i).inner_text().strip()

      print(f'Name: {name} | NIM: {nim}')

    # browser.close()
  except Exception as e:
    print(f'Error: {e}')

with sync_playwright() as playwright:
  run(playwright)