from selenium import webdriver
import time


usr_username ="root_ebby" #input("Username : ")
usr_password = "nippY0366_"#input("Password : ")

url = "https://www.instagram.com/"

browser = webdriver.Firefox()
browser.get(url)
time.sleep(2)

username = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')


username.send_keys(usr_username)
time.sleep(1)
password.send_keys(usr_password)
time.sleep(1)
giris.click()
time.sleep(3)


bilgi_kayıt = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
bilgi_kayıt.click()
time.sleep(1)

simdi_degil = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
simdi_degil.click()
time.sleep(1)

profile_button = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
profile_button.click()
time.sleep(1)
profile = browser.find_element_by_xpath("//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     ']")
profile.click()
time.sleep(1)

followerS = browser.find_element_by_xpath('//a[@class="-nal3 "]')                                          
followerS.click()
time.sleep(1)



jscommand = """
followers = document.querySelector("._gs38e");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
followersList = []

followers = browser.find_elements_by_tag_name("a")



for follower in followers:
    
    followersList.append(follower.text)
    
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
        


