

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document
from selenium.webdriver.common.by import By
import time

# Initialize Chrome with options, if needed
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode

# Initialize the driver
driver = webdriver.Chrome(options=options)

# Navigate to the Yahoo Finance IBM financials page
driver.get("URL")

# Allow some time for the page to load
time.sleep(5)

# Extract the financial data
financial_data = driver.find_element(By.TAG_NAME, "body").text

# Close the browser
driver.quit()

# Create a new Word document and add the extracted text
doc = Document()
doc.add_paragraph(financial_data)
doc.save('financial_data.docx')

print("Text has been copied and saved to 'financial_data.docx'")


