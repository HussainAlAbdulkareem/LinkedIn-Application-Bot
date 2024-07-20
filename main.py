from selenium import webdriver
from selenium.webdriver import Keys
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

#Clicks the easy apply button
driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()

time.sleep(1)
phone_num_field = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
phone_num_field.send_keys("12345678")

time.sleep(1)

#Clicks on the Next button
next_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
driver.execute_script("arguments[0].click();", next_button)

time.sleep(1)
driver.execute_script("arguments[0].click();", next_button)

#Answers selection questions
question1 = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3971779738-3580441093-multipleChoice")
question1.click()
question1.send_keys("y")
question1.send_keys(Keys.ENTER)

question2 = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3971779738-3580441085-multipleChoice")
question2.click()
question2.send_keys("y")
question2.send_keys(Keys.ENTER)

review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
driver.execute_script("arguments[0].click();", review_button)

submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
driver.execute_script("arguments[0].click();", submit_button)
