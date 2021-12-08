from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.nytimes.com/search?dropmab=false&endDate=20161231&query=&sections=Arts%7Cnyt%3A%2F%2Fsection%2F6e6ee292-b4bd-5006-a619-9ceab03524f2%2CSports%7Cnyt%3A%2F%2Fsection%2F4381411b-670f-5459-8277-b181485a19ec%2COpinion%7Cnyt%3A%2F%2Fsection%2Fd7a71185-aa60-5635-bce0-5fab76c7c297%2CWorld%7Cnyt%3A%2F%2Fsection%2F70e865b6-cc70-5181-84c9-8368b3a5c34b&sort=oldest&startDate=20161217&types=article")
print(driver.title)
i = 0
while i < 160:
    try:
        time.sleep(1)
        #show_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"][contains(.,"Show More")]')))
        #show_more.click()
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-show-more-button']"))))
        print(i)
        i = i+1
    except Exception as e:
        print(e)
        break
print("THIS IS I Final", i)
headlines = ["Headlines"]
for headline in driver.find_elements(By.XPATH, "//h4[@class='css-2fgx4k']"):
    headlines.append(headline.text)
glances = ["Glances"]
for glance in driver.find_elements(By.XPATH, "//p[@class = 'css-16nhkrn']"):
    #print(glance.text)
    glances.append(glance.text)
np.savetxt('output.csv', [p for p in zip(headlines, glances)], delimiter='/t', encoding="utf-8", fmt='%s')
print("done")
#print(headlines)
#print(glances)
df = pd.read_csv ('output.csv', delimiter='/t')
print(df)
df["both"] = df["Headlines"]+df["Glances"]
print(df["both"])
print(df["both"][0])
#try:
 #   while True:
  #      button.click()
   #     time.sleep(.5)
#except:
 #   print("QUITTING!")
  #  driver.quit()

#time.sleep(10)
#driver.quit()
