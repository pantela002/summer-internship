from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

options.add_experimental_option('prefs', {  
    "download.default_directory": "/home/oopsie/Documents/Lukowa/pdf_scraper/svi_cv",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
url= "https://app.teamtailor.com/"
driver.get(url)

driver.maximize_window()
cookies = driver.find_element(By.XPATH, "//*[@id='ember-teamtailor-modal']/div/div[2]/div")

if cookies.is_displayed():
    driver.find_element(By.XPATH, "//*[@id='ember-teamtailor-modal']/div/div[2]/div/div/footer/div[2]/button[2]").click()

time.sleep(5)
username_field = driver.find_element(By.XPATH , "//*[@id='email']")


password_field = driver.find_element(By.XPATH ,"//*[@id='password']")


username = "your-username"
password = "your-password"



username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

#url1="https://app.teamtailor.com/companies/w2uyscMTojM/candidates/segment/all/candidate/56558559"
#driver.get(url1)
#time.sleep(1)
#time.sleep(3)
#driver.switch_to.frame(0)
#element = driver.find_element(By.XPATH, "//button[@id='secondaryToolbarToggle']")
#element.click()
#time.sleep(3)
#time.sleep(1)
#down = driver.find_element(By.XPATH, "//*[@id='secondaryDownload']").click()
#time.sleep(3)

with open ("cand.csv", "r") as f:
    l=f.readlines()
    for line in l:
        url1="https://app.teamtailor.com/companies/w2uyscMTojM/candidates/segment/all/candidate/"+line[:8]
        print(url1)
        driver.get(url1)
        driver.switch_to.frame(0)
        time.sleep(5)

        element = driver.find_element(By.XPATH, "//button[@id='secondaryToolbarToggle']").click()
        time.sleep(5)
        down = driver.find_element(By.XPATH, "//*[@id='secondaryDownload']").click()

