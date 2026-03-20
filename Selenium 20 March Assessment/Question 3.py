from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://www.shine.com/registration/")
sleep(2)

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("/Users/sahajsharma/Downloads/Resume.pdf")
sleep(10)
driver.quit()