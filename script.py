# Exploring Selenium with Upwork

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access Upwork credentials from environment variables
upwork_username = os.getenv("UPWORK_USERNAME")
upwork_password = os.getenv("UPWORK_PASSWORD")

# Set up ChromeOptions
chrome_options = Options()
chrome_options.binary_location = '../chrome-win64/chrome.exe'  # Update this path with your Chrome executable path
chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode

# Set up the WebDriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Upwork page
driver.get("https://www.upwork.com/nx/find-work/saved-jobs")

# Wait for the page to load (increase wait time if needed)
driver.implicitly_wait(2)

# Log into Upwork credentials from .env file
driver.find_element(By.NAME, "username").send_keys(upwork_username)
driver.find_element(By.NAME, "password").send_keys(upwork_password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for the login process to complete and a specific element to be present
wait = WebDriverWait(driver, 5) # Adjust the timeout as needed

# Find all h3 elements with the class 'job-tile-title'
job_title_elements = driver.find_elements(by=By.XPATH, value="//h3[@class='job-tile-title']")

# Iterate through each job title element and click on it
for job_title_element in job_title_elements:
    # Click on the h3 element to open the full job posting
    job_title_element.click()
    # Wait for the page to load after clicking (increase wait time if needed)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='job-title']")))
    # Perform actions on the opened job posting page, e.g., extract details
    
    # Go back to the main jobs page
    driver.back()

# Close the browser window
driver.quit()