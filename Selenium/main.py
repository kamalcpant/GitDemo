import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='radio1']").click()
time.sleep(1)
driver.find_element(By.ID, "autocomplete").send_keys("Learn Automation")
time.sleep(1)
dropdown_driver = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example"))
dropdown_driver.select_by_visible_text("Option1")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.click(driver.find_element(By.LINK_TEXT, "Reload")).perform()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, 1200)")
driver.switch_to.frame("courses-iframe")
driver.get_screenshot_as_file("photo.png")
# driver.find_element(By.LINK_TEXT, "All Access plan")



# driver1 = webdriver.Firefox()
# driver1.maximize_window()
# driver1.implicitly_wait(1)
# driver1.get("https://the-internet.herokuapp.com/windows")
# driver1.find_element(By.LINK_TEXT, "Click Here").click()
#
# WINDOWHANDLES = driver1.window_handles
# driver1.switch_to.window(WINDOWHANDLES[1])
# print(driver1.find_element(By.TAG_NAME, "h3").text)
# driver1.switch_to.window(WINDOWHANDLES[0])
# print(driver1.find_element(By.TAG_NAME, "h3").text)

time.sleep(3)