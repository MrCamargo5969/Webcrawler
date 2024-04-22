from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('window-size=1366,768')

chrome_driver = Service(ChromeDriverManager().install())

web = webdriver.Chrome(service = chrome_driver, options = chrome_options)

url = 'https://twitter.com'

web.get(url)

web.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
time.sleep(2)

web.find_element('xpath', '///*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').click()
time.sleep(2)

web.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys('pescdata@gmail.com')
time.sleep(2)

web.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
time.sleep(2)

web.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('')
time.sleep(2)

itens = web.find_elements(By.CLASS_NAME, 'ui-search-item__title')

for i in itens:
    print(i.text)

#web.close()
