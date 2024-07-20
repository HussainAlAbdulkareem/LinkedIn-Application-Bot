from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3971779738&f_AL=true&geoId=100459316&keywords=python%20developer&location=Saudi%20Arabia&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&spellCorrectionEnabled=true")

time.sleep(3)

#Clicks the Sign in button
driver.find_element(By.CLASS_NAME, value="nav__button-secondary").click()

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(os.getenv("EMAIL"))

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(os.getenv("PASSWORD"))

#Clicks the Sign in button
driver.find_element(By.CLASS_NAME, value="btn__primary--large").click()
