# Exploring Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (use the path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Navigate to the Upwork page
driver.get("https://www.upwork.com/nx/find-work/saved-jobs")

# Wait for the page to load (increase wait time if needed)
driver.implicitly_wait(2)

# Example: Typing text into a search box (replace 'search_query' with the actual element name or attribute)
text_box = driver.find_element(by=By.NAME, value="search_query")
text_box.send_keys("Selenium")

# Example: Clicking a submit button (replace 'submit_button' with the actual element name or attribute)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
submit_button.click()

# Example: Retrieving text from an element (replace 'result_message' with the actual element name or attribute)
message = driver.find_element(by=By.ID, value="result_message")
text = message.text

# Print the retrieved text
print("Retrieved Text:")
print(text)

# Close the browser window
driver.quit()