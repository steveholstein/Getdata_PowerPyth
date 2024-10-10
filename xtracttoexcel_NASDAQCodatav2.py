

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure Chrome options
options = Options()
# Uncomment the following line if you want to run Chrome in headless mode
# options.add_argument('--headless')

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# URL of the webpage to scrape
url = "https://www.nasdaq.com/market-activity/stocks/ibm"

# Open the webpage
driver.get(url)

# Wait for a few seconds to allow the page to load (you can adjust the sleep time as necessary)
time.sleep(5)

# Get the page source and close the browser
page_source = driver.page_source
driver.quit()

# Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the page title (as an example)
page_title = soup.title.string

# Find the specific data you want to extract
# Here, I'm extracting all text content as an example
text_content = soup.get_text(separator='\n', strip=True)

# Save the extracted data to a file
with open("ibm_stock_data.txt", "w", encoding='utf-8') as file:
    file.write(page_title + "\n\n")
    file.write(text_content)

print("Data has been saved to ibm_stock_data.txt")

