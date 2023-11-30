import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")
time.sleep(1)

while True:
    try:
        print("entro al try")
        driver.find_element(by=By.XPATH, value='//*[@id="YVBoGaUiYWFZooe"]').click()
        # WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "aXiwntnBIHNQxmf")))
    except:
        break

links = driver.find_elements(by=By.CSS_SELECTOR, value="a.property-card-link")
prices = driver.find_elements(by=By.CSS_SELECTOR, value="span.PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
addresses = driver.find_elements(by=By.CSS_SELECTOR, value="address[data-test='property-card-addr']")

print(addresses)
for x in range(len(links)):
    if x%2 != 0:
        print(links[x].get_attribute("href"))

for price in prices:
    print(price.text)

for address in addresses:
    print(address.text)

while True:
    pass