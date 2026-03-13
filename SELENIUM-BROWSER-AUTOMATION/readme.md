# Introduction with selenium browser automation

## Steps to follow
- install ``` pip install selenium```
- inside ```main.py```
    - import the webriver from selenium
    - import Options class from 
      selenium.webdriver.chrome.options
    - instantiate the Option() class with options
      variable
    - pass the binary path of exe file for Brave
      browser or whatever browser you want
      optons.binary_location =
      - **For Mac**
        - ```/Applications/Brave Browser.app/Contents/MacOS/Brave Browser```
    - webdriver.Chrome(options=options)
    - driver.get(url)
    - hold the browser using input() function
    - driver.quit()

# Login in website through selenium
  ### Steps to follow
  - import the required classes and function
  ```.py
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By
  ```
  - after importing define options variable with Option()
    class
  - pass the -flag --disable-search-engine-choice-screen
    in ```.add_argument()``` method
  - pass the **Brave Browser** exe file location to 
    ```.binary_location=``` field in the options variable
  - call the ```Webdriver.Chrome(options=options)``` in driver 
    variable
  - load the webpage using ```driver.get(url)```
  - extract the field for username and password 
    using the ```WebriverWait(driver, 10).unit() ```
    pass ```EC.visibility_of_element_located()``` inside it
    pass(By.ID,"username") inside the abouve function
    "username" is the ID name inspect the field and extract
    out the id, you can use different methods as well
  - do same with password field
  - with login button you can do the same, but
    ads running on webpage might block the button at first
    so try ```driver.find_element(By.XPATH, '//*[@id="login"]/button')``` here you can use .XPATH
    method
  - now pass the username according the website using
    ```.send_keys()``` method
  - for click execution js method is executed as follow
    ```driver.execute_script("arguments[0].click();",login_button)```
  - fake input() method to stop the execution while user presses enter
  - ```driver.quit()```



# Filling Form Using Selenium
  ## Steps to follow
  - require all the neccessary classes and
    functions like ```webdriver```,```Options```,
    ```WebDriveWait```,```expected_condtions as EC```, ```By```
  
  - add options argument --disable-search-engine-choice-screen

  - add binary_location for your custom browser 
    exe file
  - pass this options variable to ```webdriver.Chrome()``` class and save it to variable
  - load the webpage via ```driver.get(url)``` method
  - locate the first link to click use the ```driver.find_element(By.method,"")``` method to locate the button or particular field
  - for clicking the button use the ```driver.execute_script("arguments[0].click()", button)```
   method
  - extract the form fields like these methods 
    use By.XPATH, By.ID selector to select the element
  - use ```.send_keys()``` method to pass the usernam, password, email fullname or whatever you have details to the form,
  - execute the submit script as mentoined abover
  
# Download file using Selenium
## Steps to follow
- import the necessary classes and functions
  like ```webdriver```,```Options```,
     ```By``` from selenium
- instatiate the option variable with Option class
- add arguments, binary_location of browser if any other browser you want to use
- change the default location of the dowload image using ```prefs = {'download.default_directory': download_path}``` here the ```download_path = os.getcwd() + '/images'```
- add this ```options.add_experimental_option('prefs',prefs)```
- instatiate the ```webdriver.Chrome(options=options)``` with driver variable
- now load the data using ```driver.get(url)```
- ***Opting OOPs concept***
- create class LocateElement() inside which define __init__ fucntion with pass
now define locate_by_Id, locate_by_XPath function in this class
- in locate_by_Id function ``` element = driver.find_element(By.ID, id)``` id is receive in parameter
- same for function locate_by_XPath ```element = driver.find_element(By.ID, XPath)``` XPath is receive in parameter
- define execute function for calling the button click
- inside execute function ```driver.execute_script("arguments[0].click()", button)``` button is receive in parameter of the function
- locate the button of required webpage using inspect, go to upload and download section
- click the ```locator.execute(button)``` method to click the button


***Refactor the code in OOPs format***

## 🖥️ GUI Based Web Automation Tool (Tkinter + Selenium)

## 📌 Introduction

This project is a GUI-based Web Automation Tool built using:

- Tkinter for Desktop GUI
- Selenium for Browser Automation
- Threading to prevent GUI freezing

The application performs:

- Login to a website
- Automatic form filling
- Browser close control from GUI

Target Website:
https://demoqa.com


---

# 🧰 Requirements

## Install Required Libraries

```bash
pip install selenium
```

Tkinter comes pre-installed with Python.


---

# 📂 Project Structure (OOP Based)

```
project/
│
├── main.py              # Selenium automation logic
├── app.py               # Tkinter GUI code
├── chromedriver.exe     # Chrome driver
└── README.md
```


---

# 🧠 How GUI Works (app.py)

## 1️⃣ Import Required Modules

```python
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from main import WebAutomation
```


---

## 2️⃣ Create Main App Class (OOP Concept)

```python
class App:
```

- Constructor receives root window
- All UI elements initialized inside `__init__`
- WebAutomation class object is created

```python
self.automate = WebAutomation(URL='https://demoqa.com')
```


---

## 3️⃣ GUI Components

### Login Section
- Username Entry
- Password Entry

### Form Section
- Full Name
- Email
- Current Address
- Permanent Address

### Buttons
- Start Automation
- Clear
- Close Browser

### Status Label
Displays:
- Idle
- Running
- Completed
- Failed
- Browser Closed


---

# 🧵 Threading Concept

## Why Threading?

If Selenium runs in the main thread:

- GUI freezes
- Window stops responding

So we use:

```python
thread = Thread(target=self.run_automation)
thread.daemon = True
thread.start()
```

Thread runs automation in background.


---

# 🚀 Automation Execution Flow

## Method: start_thread()

- Creates new thread
- Target function: `run_automation()`


---

## Method: run_automation()

### Steps:

1. Disable submit button

```python
self.submit_btn.config(state="disabled")
```

2. Update status label → Running

3. Get all form values

4. Validate inputs:

```python
if not all([username, password, fullname, email, current, permanent]):
```

5. Call automation methods:

```python
self.automate.load_page()
self.automate.login_form(username, password)
self.automate.fill_form(fullname, email, current, permanent)
```

6. On success → Status Completed  
7. On error → Show messagebox  

8. Enable submit button again


---

# 🌐 Selenium Automation (main.py)

## 1️⃣ Required Imports

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
```


---

## 2️⃣ Create WebAutomation Class

```python
class WebAutomation:
```

### Constructor

```python
def __init__(self, URL):
```

- Stores URL
- Configures Chrome options
- Initializes driver


---

## 3️⃣ Load Webpage

```python
driver.get(url)
```


---

## 4️⃣ Login Automation

### Steps:

Locate username field:

```python
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "userName"))
)
```

Send username:

```python
.send_keys(username)
```

Locate password field and send password.

Locate login button:

```python
driver.find_element(By.XPATH, '//*[@id="login"]/button')
```

Click using JavaScript:

```python
driver.execute_script("arguments[0].click();", login_button)
```


---

## 5️⃣ Form Filling Automation

### Steps:

- Locate form link
- Click using execute_script
- Locate form fields using:
  - By.ID
  - By.XPATH

Use:

```python
.send_keys(value)
```

Click submit button.


---

# 🧹 Clear Form Function

```python
def clear_form(self):
```

Loop through all Entry widgets:

```python
field.delete(0, tk.END)
```

Updates status to Cleared.


---

# 🔒 Close Browser

```python
def close_browser(self):
    self.automate.exit()
```

Inside main.py:

```python
def exit(self):
    self.driver.quit()
```


---

# 🔁 Complete Execution Flow

1. Run `app.py`
2. Tkinter window opens
3. User enters login + form details
4. Click "Start Automation"
5. Thread starts
6. Selenium opens browser
7. Login performed
8. Form filled
9. Status updated


---

# ⚙️ Refactored OOP Structure

## WebAutomation Class Structure

```python
class WebAutomation:

    def __init__(self, URL):
        self.URL = URL
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.add_argument("--disable-search-engine-choice-screen")
        return webdriver.Chrome(options=options)

    def load_page(self):
        self.driver.get(self.URL)

    def login_form(self, username, password):
        pass

    def fill_form(self, fullname, email, current, permanent):
        pass

    def exit(self):
        self.driver.quit()
```


---

# 🎯 Concepts Used

- Object Oriented Programming (OOP)
- Threading
- Selenium Automation
- Tkinter GUI
- Exception Handling
- Form Validation
- Dynamic Status Update


---

# 📌 Future Improvements

- Add logging module
- Add Progress Bar using ttk.Progressbar
- Add Dark Mode UI
- Add Email validation (regex)
- Add config file for URL
- Add database support

---

# ✅ Conclusion

This project demonstrates how to integrate:

- Desktop GUI
- Background threading
- Browser automation
- OOP design

It is scalable and can be extended to production-level architecture.