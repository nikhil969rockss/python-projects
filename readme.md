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
  

    