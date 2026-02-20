from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL="https://the-internet.herokuapp.com/login"

# define options, webdriver
options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=options)

#Load the web page
driver.get(URL)

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"username")))
password_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button')
print(login_button)

#fill the fields
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
#execute the button us js script
driver.execute_script("arguments[0].click();",login_button)

input("Press enter to quit browser ")
driver.quit()