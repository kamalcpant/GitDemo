import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

SEARCH_KEYWORD = "ber"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

EXPECTED_ITEM_LIST = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
ACTUAL_ITEM_LIST = []
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys(SEARCH_KEYWORD)
time.sleep(2)
VEG_ITEMS = driver.find_elements(By.XPATH, "//div/div[@class='products']/div")
print(len(VEG_ITEMS))

for item in VEG_ITEMS:
    item.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
    item_name = item.find_element(By.CSS_SELECTOR, ".product-name").text
    # print(item_name)
    ACTUAL_ITEM_LIST.append(item_name)

# print(f"Expected Item List: {EXPECTED_ITEM_LIST}")
# print(f"Actual Item List: {ACTUAL_ITEM_LIST}")
assert EXPECTED_ITEM_LIST == ACTUAL_ITEM_LIST

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
message = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert message == "Code applied ..!"

cart_element = driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr")
SUM_CALC = 0
for element in cart_element:
    amount = element.find_element(By.XPATH, "td[5]//p[@class='amount']").text
    print(amount)
    SUM_CALC += float(amount)

SUM = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(SUM)
assert SUM == SUM_CALC

DISCOUNTED_AMOUNT = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert DISCOUNTED_AMOUNT < SUM



time.sleep(2)