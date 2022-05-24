from kiteconnect import KiteConnect
from selenium import webdriver
import time
import os

os.path

cwd = os.chdir("/Users/sonukumar/Desktop/Trading App")

api_key = "4mskpbib2ifglgv7"
api_secret = "t4j3z6wt3ahlh6x0tlgl02jh4xdm97e9"
user_name ='JH1931'
user_password = 'Market2021'
user_pin = '932021'

def autologin(api_key, api_secret, user_name, user_password, user_pin):
    kite = KiteConnect(api_key=api_key)
    service = webdriver.chrome.service.Service('./chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)
    driver.get(kite.login_url())
    driver.implicitly_wait(10)
    username = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    username.send_keys(user_name)
    password.send_keys(user_password)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    pin = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input')
    pin.send_keys(user_pin)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button').click()
    time.sleep(10)
    request_token = driver.current_url.split('=')[1].split('&action')[0]
   
    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(request_token, api_secret=api_secret)
    driver.quit()
    return data["access_token"]

#generating and storing access token - valid till 6 am the next day
access_token  = autologin(api_key, api_secret, user_name, user_password, user_pin)

print("access_token : ", access_token)
