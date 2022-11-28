from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


browser = webdriver.Chrome(
    executable_path='C:\chromedriver\chromedriver')

browser.get('http://127.0.0.1:3000')

dataframe = pd.read_excel('data.xlsx')
# print(dataframe.iloc[0])
for i in dataframe.index:
    entry = dataframe.iloc[i]

    email_input = browser.find_element('name','email')
    email_input.send_keys(entry['Email'])

    name_input = browser.find_element('name','username')
    name_input.send_keys(entry['Username'])

    pass_input = browser.find_element('name','password')
    pass_input.send_keys(entry['password'])

    cnfpass_input = browser.find_element('name','passwordConf')
    cnfpass_input.send_keys(entry['cnf_password'])

    print('Sleeping for 5 seconds before submitting...')
    time.sleep(3)

    # email_input.submit()

    submit_btn = browser.find_element('name','submit')
    browser.execute_script("return arguments[0].click()", submit_btn)

    time.sleep(2)