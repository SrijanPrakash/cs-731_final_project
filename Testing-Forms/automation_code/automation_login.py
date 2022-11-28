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

    login_btn = browser.find_element('name','login')
    browser.execute_script("return arguments[0].click()", login_btn)

    time.sleep(5)



