#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL="https://demoqa.com/"
# define driver and options
options = Options()
options.add_argument("--disable-search-engine-choice-screen")
# options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=options)

# Load the website
driver.get(URL)

# This method showing me error
# book_store_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/a[6]')))
# book_store_button.click()

#Locate the book_store button and click
book_store_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/a[6]')
driver.execute_script("arguments[0].click();", book_store_button)


# Locate the Login and click
login_page_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[6]/div/ul/li[1]/a')
driver.execute_script("arguments[0].click();", login_page_button)


# Extracting fields from the login form
username_field = driver.find_element(By.ID, "userName")
password_field = driver.find_element(By.ID, "password")

#Filling form
username_field.send_keys("nikhil969")
password_field.send_keys("Nikhil969rock@")
login_button = driver.find_element(By.ID, "login")
driver.execute_script("arguments[0].click()", login_button)

#Locate the form 
elements_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]')
elements_button.click()
text_box_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/ul/li[1]/a')
driver.execute_script("arguments[0].click()", text_box_button)

# extracting the form elements 
full_name_field = driver.find_element(By.ID, "userName")
email_field = driver.find_element(By.ID, "userEmail")
current_add_field = driver.find_element(By.ID, "currentAddress")
permanant_add_field = driver.find_element(By.ID, "permanentAddress")
submit_button = driver.find_element(By.ID,"submit")

#filling the fields
full_name_field.send_keys("Nikhil Singh")
email_field.send_keys("nikhil@gmail.com")
current_add_field.send_keys("nikhil shah road c3")
permanant_add_field.send_keys("nikhil shah road c3")

driver.execute_script("arguments[0].click();", submit_button)
driver.execute_script("arguments[0].click()", text_box_button)



input("Press Enter to close the browser ")
driver.quit()