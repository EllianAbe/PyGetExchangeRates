from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
import pandas as pd
import os

os.environ["TMPDIR"] = "temp"

options = FirefoxOptions()
options.binary_location = "/snap/bin/firefox"

df = pd.read_csv('input.csv')

driver = webdriver.Firefox(options=options)

try:

    for index, row in df.iterrows():
        driver.get(f"https://www.google.com/search?q={row['command']}")
        element = driver.find_elements(
            by=By.XPATH, value='//input[@aria-label="Campo do montante da moeda"]')[1]

        text = element.get_attribute('value')
        df.at[index, 'rate'] = float(text)

        driver.implicitly_wait(3)
except Exception as e:
    raise e
finally:
    driver.quit()


df.to_csv('output.csv', index=False)
