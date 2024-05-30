


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Optional for arguments

# Optional: If using arguments for ChromeDriver (e.g., headless mode)
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode

driver = webdriver.Chrome(options=options)  # Initialize the driver

# Your code here (interactions using the driver)
driver.get("https://finance.yahoo.com/quote/IBM/financials")

# Rest of your code using the driver


import pyautogui
import time
import os
from docx import Document


# Replace with the path to your Chrome WebDriver: perhaps not needed with Chrome 115 or later.
#driver = webdriver.Chrome("C:\Users\hello\Documents\chromedriver-win64")

# Navigate to the Yahoo Finance IBM financials page
driver.get("URL")

# Click on the "Breakdown" section using XPath
breakdown_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='P(6) Bdrs(5) Bgc($white) Ovx(a) Ovhidden Whs(nw)'][text()='Breakdown']"))
)
breakdown_button.click()

# Wait for 2 seconds
time.sleep(2)

# Press Ctrl+C to copy the financials data (simulates keyboard shortcut)
pyautogui.hotkey('ctrl', 'c')

# Create a new Word document using `python-docx`
doc = Document()
doc.add_paragraph("Initial Data (This can be empty or custom text)")
doc_path = "new_document.docx"
doc.save(doc_path)

# Launch the new document in Word
os.startfile(doc_path)

# Wait for Word to open
time.sleep(5)  # Adjust if Word takes more or less time to open

# Click on the Word window to bring it into focus
# Coordinates can be adjusted according to your screen setup
pyautogui.click(x=100, y=100)  # Replace with coordinates of your Word window

# Wait for 2 seconds
time.sleep(2)

# Press Ctrl+V to paste the copied financial data
pyautogui.hotkey('ctrl', 'v')


# Close the browser window
driver.quit()