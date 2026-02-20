# Instroduction with selenium browser automation

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