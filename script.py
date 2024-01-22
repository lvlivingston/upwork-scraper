# Exploring Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (use the path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Navigate to the Upwork page
driver.get("https://www.upwork.com/nx/find-work/saved-jobs")

# Wait for the page to load (increase wait time if needed)
driver.implicitly_wait(2)

# Find all h3 elements with the class 'job-tile-title'
job_title_elements = driver.find_elements(by=By.XPATH, value="//h3[@class='job-tile-title']")

# Extract and print text from each h3 element
for element in job_title_elements:
    text = element.text.strip()
    if text:  # Check if the text is not empty
        print(text)

# Close the browser window
driver.quit()