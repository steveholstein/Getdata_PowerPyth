


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

# Replace with the path to your Chrome WebDriver: perhaps not needed with Chrome 115 or later.
#driver = webdriver.Chrome("C:\Users\hello\Documents\chromedriver-win64")

# Navigate to the Yahoo Finance IBM financials page
driver.get("https://finance.yahoo.com/quote/IBM/financials")

# Click on the "Breakdown" section using XPath
breakdown_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='P(6) Bdrs(5) Bgc($white) Ovx(a) Ovhidden Whs(nw)'][text()='Breakdown']"))
)
breakdown_button.click()

# Wait for 2 seconds
time.sleep(2)

# Press Ctrl+C to copy the financials data (simulates keyboard shortcut)
pyautogui.hotkey('ctrl', 'c')

# Switch focus to the Word document (assuming the second window is Word)
# Change the following line if Word has a different title or window position
pyautogui.click(x=100, y=100)  # Replace with coordinates of your Word window

# Wait for 2 seconds
time.sleep(2)

# Press Ctrl+V to paste the copied financials data
pyautogui.hotkey('ctrl', 'v')

# Close the browser window
driver.quit()