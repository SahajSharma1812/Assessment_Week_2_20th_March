from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get("https://www.saucedemo.com")
wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("secret_sauce")
sleep(3)
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
print("Page Title:", title.text)
sleep(3)
names = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
for i in range(len(names)):
    print(names[i].text, "-", prices[i].text)
    sleep(1)
add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
add_buttons[3].click()
sleep(10)
driver.quit()