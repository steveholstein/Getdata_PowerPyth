

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document
from selenium.webdriver.common.by import By
import openpyxl
import time

# Initialize Chrome with options, if needed
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode

# Initialize the driver
driver = webdriver.Chrome(options=options)

urlinf = "https://finance.yahoo.com/quote/IBM/financials"
urlinf = "https://www.asx.com.au/markets/company/BHP"


# Navigate to the Yahoo Finance IBM financials page
driver.get(urlinf)

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

# Create a new Excel workbook and add the extracted text
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Financial Data"

# Write the financial data to the Excel sheet, cell by cell
for row_num, row_data in enumerate(financial_data.split('\n'), 1):
    ws.cell(row=row_num, column=1, value=row_data)

# Save the Excel workbook
xlname = 'financial_data_2.xlsx'
wb.save(xlname)

print(f"Text has been copied and saved to 'financial_data.docx' and '{xlname}'")

# Note: you may need to install openpyxl using: pip install selenium python-docx openpyxl


