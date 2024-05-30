from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document
import pyperclip
import time

start_time = time.ctime()
print("Time:", start_time)
# Initialize Chrome with options, if needed
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode

# Initialize the driver
driver = webdriver.Chrome(options=options)

# Navigate to the Yahoo Finance IBM financials page
driver.get("URL")

# Allow some time for the page to load
time.sleep(5)

# Wait for 7 seconds to allow user to highlight and copy text
time.sleep(7)

# Retrieve the text from the clipboard
copied_text = pyperclip.paste()

# Close the browser
driver.quit()

# Create a new Word document and add the copied text
doc = Document()
doc.add_paragraph(copied_text)
doc.save('copied_text.docx')

print("Text has been copied and saved to 'copied_text.docx'")
finish_time = time.ctime()
print("Time:", finish_time)
