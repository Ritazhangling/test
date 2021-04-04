from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

#initailize browser and open the test website
driver = webdriver.Chrome()
driver.get('http://zero.webappsecurity.com/')
#print(driver.title)

# login as existed user by using username/password
username='username'
password='password'
driver.find_element_by_id('signin_button').click()
driver.find_element_by_id('user_login').send_keys(username)
driver.find_element_by_id('user_password').send_keys(password)
driver.find_element_by_name('submit').click()
sleep(1)

# transfer funds between different account
driver.find_element_by_id('details-button').click()
driver.find_element_by_id('proceed-link').click()
driver.back()

driver.find_element_by_id('transfer_funds_link').click()
sel1=driver.find_element_by_id('tf_fromAccountId')
Select(sel1).select_by_value('1')

sel2=driver.find_element_by_id('tf_toAccountId')
Select(sel2).select_by_value('2')
driver.find_element_by_id('tf_amount').send_keys('10')
driver.find_element_by_id('tf_description').send_keys('test for transfer')
driver.find_element_by_id('btn_submit').click()
driver.find_element_by_id('btn_submit').click()

#check the result on UI
element_text=driver.find_element_by_xpath('//*[@id="transfer_funds_content"]/div/div/div[1]').text
expected_text='You successfully submitted your transaction.'

if str(element_text).find(str(expected_text)) > -1:
    print('transaction is successful')
else:
    print('transaction is failed')

#logout
driver.find_element_by_link_text(username).click()
driver.find_element_by_xpath('//*[@id="logout_link"]').click()
driver.quit()