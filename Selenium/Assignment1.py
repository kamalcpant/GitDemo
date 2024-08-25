import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
TEXT = driver.find_element(By.XPATH, "//div/p[2]").text
EMAIL = TEXT.split()[4]
driver.switch_to.window(window_handles[0])

driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys("Test@123")
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
print(driver.find_element(By.CSS_SELECTOR, ".alert").text)
