from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PRODUCT = "Blackberry"
options = webdriver.ChromeOptions()
options.add_argument("maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
Item_List = driver.find_elements(By.TAG_NAME, "app-card")
for item in Item_List:
    item_name = item.find_element(By.CSS_SELECTOR, "h4[class='card-title']").text
    if item_name == PRODUCT:
        item.find_element(By.CSS_SELECTOR, "button[class*='btn']") .click()
        break
driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='suggestions']")))
country_list = driver.find_elements(By.CSS_SELECTOR, "div[class*='suggestions'] ul")
for country in country_list:
    country_text = country.find_element(By.CSS_SELECTOR, "li a").text
    if country_text == "India":
        country.find_element(By.CSS_SELECTOR, "li a").click()
        break
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
success_message = driver.find_element(By.CSS_SELECTOR, ".alert").text
assert "Success!" in success_message

