# driver.quit() เพื่อปิด browser
# driver.close() เพื่อปิด tab
# print(driver.title) แสดง title

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import pandas
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://store.steampowered.com/app/1237950/STAR_WARS_Battlefront_II/")
time.sleep(1)
value = True

while (value):
    try:
        #If Age Restrict
        year = driver.find_element(By.NAME,"ageYear")
        Select(year).select_by_visible_text("2001")

        view_page_btn = driver.find_element(By.ID, "view_product_page_btn").click()
        time.sleep(2)
    except:
        pass

    #name
    #name = driver.find_element(By.CLASS_NAME, "apphub_AppName")
    #print(name.text)

    #tag
    #tag = driver.find_elements(By.XPATH, "//*[@id='glanceCtnResponsiveRight']/div[2]/div[2]/a")
    #for i in tag:
        #print(i.text)
    
    print(driver.current_url)

    next_click = driver.find_element(By.XPATH, "//*[@id='recommended_block_content']/a[12]").click()
    time.sleep(2)





# # Store Data
# data_list = []

# for i in range(len(name)):
#     data = {
#         'Name': name.text,
#         'tag': tag.text
#     }
#     data_list.append(data)

# df = pandas.DataFrame(data_list)
# df

# #main = driver.find_element(By.XPATH, "//*[@id='appHubAppName_responsive']" )
# #print(main.text)
