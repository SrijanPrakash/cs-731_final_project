from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

browser = webdriver.Chrome(
    executable_path='C:\chromedriver\chromedriver')

browser.get('http://127.0.0.1:4000/login')

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

    req_status = entry['req_status']
    desc = entry['Test_description']

    result_expected = ""
    actual_result = ""

    if req_status:
        result_expected = "Login Successful"
    else:
        result_expected = "Login Failed"
       
    url = browser.current_url
    # msg = browser.find_element('id','check')

    status = 1
    if(url == "http://127.0.0.1:4000/profile"):
        err = "None"
        actual_result = "Login Successful"
        time.sleep(3)
        browser.find_element('name','logout').click()
        time.sleep(2)
        browser.get('http://127.0.0.1:4000/login')
    else:
        status = 0
        msg = browser.find_element('id','check')
        actual_result = "Login Failed"
        err = msg

    if status == req_status:
        status = "Pass"
    else:
        status = "Fail" 

    entry = {'Test description':desc,'Testcase status':status,'Result Expected':result_expected,'Actual_Result':actual_result,'Error':err}
    print(entry)
    # time.sleep(3)
    # browser.find_element('name','logout').click()
    # time.sleep(2)
    # browser.get('http://127.0.0.1:3000/login')
    # email_input.clear()
    # name_input.clear()
    # pass_input.clear()
    # cnfpass_input.clear()
    
    time.sleep(5)       
    # time.sleep(5)



