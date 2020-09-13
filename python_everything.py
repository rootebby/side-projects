# import pyautogui as pt
# import os
import time
from selenium import webdriver
TC     = "10237424036"  #input("TC : ")
PASSWD = "nippY0366"    #input("Password")
# Start :-)
url = "https://www.btkakademi.gov.tr/portal/sign-in#!/play"
browser = webdriver.Firefox()

browser.get(url)
time.sleep(1)

milyon_giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/button')
milyon_giris.click()
time.sleep(1)

area_tc     = browser.find_element_by_xpath('//*[@id="identification"]')
area_passwd = browser.find_element_by_xpath('//*[@id="password"]')
area_giris = browser.find_element_by_xpath('//*[@id="loginform"]/button')

area_tc.clear()
area_passwd.clear()

area_tc.send_keys(TC)
area_passwd.send_keys(PASSWD)
area_giris.click()

time.sleep(7)


# __MAIN____MAIN____MAIN____MAIN____MAIN____MAIN____MAIN____MAIN____MAIN____MAIN__
"""

url_2 = "https://www.btkakademi.gov.tr/portal/course/deliver/c--7008#!/play"

browser.get(url_2)
print("Lütfen sayfa açılınca videoyu oynatmaya başlayınız !!!!!")

time.sleep(10)
try:

    total_time   = browser.find_element_by_name('total-time')
    current_time = browser.find_element_by_name('current-time')
    print("Elementleri Buldu !!!")

except :
    print("Elementleri Bulamadı !!!")
"""

    



