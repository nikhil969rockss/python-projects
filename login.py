from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation():
    def __init__(self, URL) :
        self.URL = URL

        # define options, webdriver
        options = Options()
        options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=options) # type: ignore

    def load_page(self):
        self.driver.get(self.URL)
    
    def locate_by_Id(self, id):
        element = self.driver.find_element(By.ID,id)
        return element
    
    def locate_by_XPath(self, XPath):
        element = self.driver.find_element(By.XPATH,XPath)
        return element
    
    def execute(self, button):
        self.driver.execute_script("arguments[0].click();", button)

    def login_user(self, username, password):
        username_field = self.locate_by_Id("username")
        password_field = self.locate_by_Id("password")
        login_button = self.locate_by_XPath('//*[@id="login"]/button')

        #fill the form
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.execute(login_button)
    
    def exit(self):
        input("Press enter to quit browser ")
        self.driver.quit()


automate = WebAutomation('https://the-internet.herokuapp.com/login')
automate.load_page()
automate.login_user(username='tomsmith', password='SuperSecretPassword!')
automate.exit()