from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "ben_yanes"
USERNAME = "just_eugene@hotmail.com"
PASSWORD = "eugenio10"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Edge()

    def login(self):

        #Logging in
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value="username").send_keys(USERNAME)
        self.driver.find_element(by=By.NAME, value="password").send_keys(PASSWORD)
        time.sleep(0.3)
        self.driver.find_element(by=By.CSS_SELECTOR, value="#loginForm > div > div:nth-child(3) > button > div").click()
        time.sleep(4)

        #Searching target
        self.driver.find_element(by=By.CSS_SELECTOR, value='svg[aria-label="Buscar"]').click()
        time.sleep(0.5)
        self.driver.find_element(by=By.CSS_SELECTOR, value='input[aria-label="Buscar entrada"]').send_keys("ben_yanes")
        time.sleep(1)
        self.driver.find_element(by=By.CSS_SELECTOR, value='a[href="/ben_yanes/"]').click()

        #Clicking the followers button
        time.sleep(3)
        self.driver.find_element(by=By.CSS_SELECTOR, value='a[href="/ben_yanes/followers/"]').click()

        #Following accounts
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_aZ"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button').click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Seguir')])[1]"))).click()

    def find_followers(self):
        pass

    def follow(self):
        pass


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

while True:
    pass