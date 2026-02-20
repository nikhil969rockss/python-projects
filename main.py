from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=options)
driver.get('https://demoqa.com')

input("Press enter to quit browser")
driver.quit()