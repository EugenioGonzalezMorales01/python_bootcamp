import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "https://tinder.com/"
password = "eugenio10!"

driver = webdriver.Edge()
driver.get(link)

time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR, value="a.c1p6lbu0").click()

time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="u-1238065328"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()

time.sleep(1)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
log_in = driver.find_element(by=By.NAME, value="email")
log_in.send_keys("just_eugene@hotmail.com")
log_in.send_keys(Keys.TAB)
log_in = driver.find_element(by=By.NAME, value="pass")
log_in.send_keys(password)
log_in.send_keys(Keys.ENTER)

time.sleep(4)
tinder_window = driver.window_handles[0]
driver.switch_to.window(tinder_window)
def accept_all():
    driver.find_element(by=By.CSS_SELECTOR, value='button.c1p6lbu0').click()

    time.sleep(1)
    driver.find_element(by=By.CSS_SELECTOR, value='button.c1p6lbu0').click()

    time.sleep(1)
    driver.find_element(by=By.CSS_SELECTOR, value='button.c1p6lbu0').click()

x = True

while x:
    try:
        accept_all()
        x = False
    except:
        time.sleep(2)

time.sleep(5)
while True:
    time.sleep(1)
    try:
        driver.find_element(by=By.CSS_SELECTOR, value='#u490315748 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button').click()
    except:
        driver.find_element(by=By.CSS_SELECTOR, value='#u-1238065328 > main > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\)--ml.Px\(24px\) > button.c1p6lbu0.D\(b\).Mx\(a\)').click()
