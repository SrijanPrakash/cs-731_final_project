from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

browser = webdriver.Chrome(
    executable_path='C:\chromedriver\chromedriver')

browser.get('http://127.0.0.1:3000/login')

dataframe = pd.read_excel('login_data.xlsx')

for i in dataframe.index:
    entry = dataframe.iloc[i]

    email_input = browser.find_element('name','email')
    email_input.send_keys(entry['Email'])

    pass_input = browser.find_element('name','password')
    pass_input.send_keys(entry['Password'])

    print('Sleeping for 5 seconds before submitting...')
    time.sleep(3)

    # email_input.submit()

    browser.find_element('name','login').click()
    time.sleep(3)
    expected_url = "http://127.0.0.1:3000/profile"
    current_url = browser.current_url
    print(current_url)

    if expected_url == current_url:
        time.sleep(3)
        browser.find_element('name','logout').click()
        print("User testcase valid")
        browser.find_element('name','login_link').click()
         
    else :
        print("Invalid testcase")
       

    time.sleep(5)



