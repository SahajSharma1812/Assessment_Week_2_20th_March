from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.prokabaddi.com")
driver.maximize_window()

sleep(3)

driver.find_element(By.XPATH, "//a[contains(@href,'standings')]").click()

sleep(3)

rows = driver.find_elements(By.CLASS_NAME, "table-row")

for row in rows:
    team_name = row.find_element(By.CLASS_NAME, "team").text

    if "Jaipur Pink Panthers" in team_name:
        print("Team:", team_name)

        print("Matches Played:", row.find_element(By.CLASS_NAME, "matches-play").text)
        print("Wins:", row.find_element(By.CLASS_NAME, "matches-won").text)
        print("Losses:", row.find_element(By.CLASS_NAME, "matches-lost").text)
        print("Score Difference:", row.find_element(By.CLASS_NAME, "score-diff").text)
        print("Points:", row.find_element(By.CLASS_NAME, "points").text)

        break
sleep(10)
driver.quit()