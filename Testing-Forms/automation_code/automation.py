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

    req_status = entry['req_status']
    desc = entry['Test_description']
    result_expected = ""
    actual_result = ""

    if req_status:
        result_expected = "Registration Successful"
    else:
        result_expected = "Registration Failed"

    msg = browser.find_element("id","check")

    status = 1
    if(msg.text == "You are regestered,You can login now."):
        err = "None"
        actual_result = "Registration Successful"
    else:
        status = 0
        actual_result = "Registration Failed"
        err = msg

    if status == req_status:
        status = "Pass"
    else:
        status = "Fail"

    entry = {'Test description':desc,'Testcase status':status,'Result Expected':result_expected,'Actual_Result':actual_result,'Error':err}
    print(entry)
    time.sleep(3)
    email_input.clear()
    name_input.clear()
    pass_input.clear()
    cnfpass_input.clear()
    
    time.sleep(5)
    # browser.close()