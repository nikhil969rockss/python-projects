from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

URL="https://demoqa.com/"


# define driver and options
options = Options()
download_path = os.getcwd() + "/images"
prefs = {'download.default_directory': download_path}
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(options=options) # type: ignore

# Load the webpage
driver.get(URL)

class LocateElement():
    def __init__(self):
        pass
    
    def locate_by_Id(self, id:str):
        element = driver.find_element(By.ID, id)
        return element
    
    def locate_by_XPath(self, XPath:str):
        element = driver.find_element(By.XPATH, XPath)
        return element
    
    def execute(self, button):
        driver.execute_script("arguments[0].click();", button)

#Locate the upload and download section
locator = LocateElement()
element_link = locator.locate_by_XPath(XPath='/html/body/div[1]/div[1]/div/div[2]/div/a[1]')
locator.execute(button=element_link)

upload_download_tab = locator.locate_by_XPath(XPath='/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/ul/li[8]/a')
locator.execute(upload_download_tab)

download_button = locator.locate_by_Id('downloadButton')
locator.execute(button=download_button)

input("Press Enter to close brower ")
driver.quit()