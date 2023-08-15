import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

item_search = "Table Tennis Racket"

driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get(url="https://www.flipkart.com/")
time.sleep(5)
close_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
close_btn.click()
time.sleep(3)
search_input = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search_input.click()
search_input.send_keys(item_search)

time.sleep(2)
search_svg = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_svg.click()
time.sleep(3)

item_list = driver.find_elements(By.CLASS_NAME, 's1Q9rs')
time.sleep(2)
price_list = driver.find_elements(By.CLASS_NAME, '_30jeq3')
time.sleep(2)
image_list = driver.find_elements(By.CLASS_NAME, '_396cs4')
time.sleep(2)

name = []
link = []
images = []
prices = []

for item in item_list:
    name.append(item.get_attribute('title'))
    link.append(item.get_attribute('href'))

time.sleep(2)
for item in image_list:
    images.append(item.get_attribute('src'))

time.sleep(2)
for item in price_list:
    prices.append(item.text)

main_price = [item.split('₹')[1] for item in prices]
total_items = len(name)
data = []

for item in range(total_items):
    row = {
        'name': name[item],
        'price': prices[item],
        'image': images[item],
        'product': link[item]
    }
    data.append(row)

df = pd.DataFrame(data=data)
df.to_csv('products.csv')
print(df)
