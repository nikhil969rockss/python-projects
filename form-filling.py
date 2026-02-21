#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomation():
    def __init__(self, URL) :
        self.URL = URL
        # define driver and options
        options = Options()
        options.add_argument("--disable-search-engine-choice-screen")
        #optional Brave Browser
        # options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        self.driver = webdriver.Chrome(options=options) # type: ignore 
    
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


# This method showing me error
# book_store_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/a[6]')))
# book_store_button.click()

automate = WebAutomation(URL='https://demoqa.com')
automate.load_page()
automate.login_form(username='nikhil969',password='Nikhil969rock@')
automate.fill_form(full_name='Nikhil Singh', email='nikhil@gmail.com',
                   current_add='nikhil shah bahadur prataph sing road',
                   permanent_add='nikhil shah bahadur prataph sing road')
automate.exit()




