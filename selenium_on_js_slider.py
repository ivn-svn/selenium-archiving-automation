from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time

# Initialize the driver
driver = webdriver.Chrome(executable_path='\\chromedriver.exe')  # Change this to the driver you're using, e.g., webdriver.Firefox() for Firefox

# Navigate to the webpage
driver.get("https://...")

counter = 0

try:
    # Wait for the cookie acceptance button to become visible
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'the-id-comes-here')))
    # Click the button
    button.click()
    print("Cookie Accepted")
except NoSuchElementException:
    print("Cookie acceptance button not found")
except ElementNotInteractableException:
    print("Cookie acceptance button not interactable")



try:
    while True:
        try:
            button = driver.find_element_by_id('the-other-id-comes-here')
            # check if button is displayed and then click it
            if button.is_displayed():
                button.click()
                print("Popup closed") # If there is a pop up, this will clean it out.
        except NoSuchElementException:
            print("Popup close button not found")
        try:
            # find the flip button and click it to flip the page
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'eagle-arrows__right')))
            button.click()
            time.sleep(2)

            counter += 1
            # screenshot the page
            driver.get_screenshot_as_file(f"screenshot_{counter}.png")
            print(f"Screenshot {counter} saved")
        except ElementNotInteractableException:
            print("Element not interactable, trying to handle overlay")
            overlay_button = driver.find_element_by_id('overlay_button_id')
            overlay_button.click()
except TimeoutException:
    print("Button not found or not visible")

# Close the driver
driver.quit()
