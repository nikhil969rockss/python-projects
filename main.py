#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation():
    def __init__(self, URL) :
        self.URL = URL

        # define driver and options
        self.options = Options()
        self.options.add_argument("--disable-search-engine-choice-screen")

        #changing default download path..
        download_path = os.getcwd() + '/images'
        prefs = {'download.default_directory':download_path}
        self.options.add_experimental_option('prefs', prefs)

        #optional Brave Browser
        # options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

        self.driver = webdriver.Chrome(options=self.options) # type: ignore 
    
    def load_page(self):
        """This function is to load the website"""
        self.driver.get(self.URL)
    
    def element_by_id(self,id:str):
        """Locate the element in the page\n
        Using id of the element
        """
        element = self.driver.find_element(By.ID,id)
        return element

    def element_by_XPath(self,XPath:str):
        """Locate the element in the page\n Usign XPath of the element"""
        element = self.driver.find_element(By.XPATH,XPath)
        return element
    
    def execute(self, button):
        """To execute the javascript for click the button"""
        self.driver.execute_script("arguments[0].click();", button)

    def login_form(self,username:str, password:str):
        """To fill the form in the website according the page elements"""
        #Locate the book_store button and click
        book_store_button = self.element_by_XPath('//*[@id="root"]/div[1]/div/div[2]/div/a[6]')
        self.execute(book_store_button)

        # Locate the Login and click
        login_page_button = self.element_by_XPath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[6]/div/ul/li[1]/a')
        self.execute(login_page_button)

        # Extracting fields from the login form
        username_field = self.element_by_id("userName")
        password_field = self.element_by_id("password")
        login_button = self.element_by_id("login")
        
        #Filling form
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.execute(login_button)

    def fill_form(self,full_name,email, current_add, permanent_add):
        """Fill form in the website page in the element tab section"""
        #navigate to form page
        element_tab_button = self.element_by_XPath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]')
        self.execute(element_tab_button)

        text_box_tab = self.element_by_XPath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/ul/li[1]/a')
        self.execute(text_box_tab)

        #extracting from fields
        full_name_field = self.element_by_id('userName')
        email_field = self.element_by_id('userEmail')
        current_add_field = self.element_by_id('currentAddress')
        permanant_add_field = self.element_by_id('permanentAddress')
        submit_button = self.element_by_id('submit')

        #fill the form details
        full_name_field.send_keys(full_name)
        email_field.send_keys(email)
        current_add_field.send_keys(current_add)
        permanant_add_field.send_keys(permanent_add)

        self.execute(submit_button)
        self.execute(text_box_tab)
    
    def exit(self):
        input("Press Enter to close the browser ")
        self.driver.quit()   

class DownLoadImgAutomation(WebAutomation):
    def __init__(self, URL):
        super().__init__(URL)
    
    def download_image(self):
        """Download the image from upload and download section of the page"""
        # navigate to upload and download
        
        upload_download_tab = self.element_by_XPath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/ul/li[8]/a')
        self.execute(upload_download_tab)

        download_button = self.element_by_id('downloadButton')
        self.execute(button=download_button)


# This method showing me error
# book_store_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/a[6]')))
# book_store_button.click()

automate = DownLoadImgAutomation(URL='https://demoqa.com')
automate.load_page()
automate.login_form(username='nikhil969',password='Nikhil969rock@')
automate.fill_form(full_name='Nikhil Singh', email='nikhil@gmail.com',
                   current_add='nikhil shah bahadur prataph sing road',
                   permanent_add='nikhil shah bahadur prataph sing road')
automate.download_image()
automate.exit()