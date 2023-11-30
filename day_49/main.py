from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link = "https://www.linkedin.com/jobs/search/?currentJobId=3640855289&f_AL=true&geoId=104201579&keywords=Python" \
       "%20developer&location=Monterrey%2C%20Nuevo%20Le%C3%B3n%2C%20Mexico&refresh=true"

drive = webdriver.Edge()

drive.get(link)

time.sleep(1)
drive.find_element(by=By.LINK_TEXT, value="Inicia sesión").click()

time.sleep(1)
drive.find_element(by=By.NAME, value="session_key").send_keys("wallet.pencil@hotmail.com")
drive.find_element(by=By.NAME, value="session_password").send_keys("eugenio10")
drive.find_element(by=By.CSS_SELECTOR, value="div.login__form_action_container button").click()

time.sleep(1)
drive.find_element(by=By.CSS_SELECTOR, value="div.jobs-apply-button--top-card button").click()





time.sleep(1)
phone_code = drive.find_element(by=By.CSS_SELECTOR, value="div.pb4 div:nth-child(4) select")

phone_code.send_keys(Keys.DOWN)
phone_code.send_keys(Keys.ENTER)

drive.find_element(by=By.CSS_SELECTOR, value="div.artdeco-text-input--container input.artdeco-text-input--input").send_keys("2211250450")
drive.find_element(by=By.CSS_SELECTOR, value="div.display-flex button.artdeco-button").click()

time.sleep(1)
drive.find_element(by=By.CSS_SELECTOR, value="div.display-flex button.artdeco-button").click()
while True:
       pass
