from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from typing import List
import pandas
import time

# from config import CHROME_PROFILE_PATH

options = webdriver.ChromeOptions()
# options.add_argument(CHROME_PROFILE_PATH)
driver = webdriver.Chrome("C:/Users/Admin/chromedriver.exe", options=options)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

count = 0

# Read data from excel
excel_data = pandas.read_excel(
    'My WHATSAPP_EXCEL_2021.xls', sheet_name='Comunicazioni_PYTHON')
msg = 0
# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():

    # Assign customized message
    # message = excel_data['Message'][0]
    message = excel_data['Message'][msg]

    # Locate search box through x_path
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(
        ec.presence_of_element_located((By.XPATH, search_box)))

    # Clear search box if any contact number is written in it
    person_title.clear()

    # Send contact number in search box
    person_title.send_keys(str(excel_data['Contact'][count]))
    count += 1
    msg += 1

    # Wait for 2 seconds to search contact number
    time.sleep(2)

    try:
        # Load error message in case unavailability of contact number
        element = driver.find_element_by_xpath(
            '//*[@id="pane-side"]/div[1]/div/span')
    except NoSuchElementException:
        actions = ActionChains(driver)
        msg1: List[str] = []
        with open('message.txt', "r") as file:
            for line in file:
                msg1.append(line.rstrip())
        person_title.send_keys(Keys.ENTER)
        for msg_line in msg1:  # iterate over the list of lines of a message
            actions.send_keys(msg_line + Keys.SHIFT + Keys.ENTER)
            print((msg_line).encode())
            actions.perform()
        # Format the message from excel sheet
        #message = message.replace('{customer_name}', column)
        # person_title.send_keys(Keys.ENTER)
        #actions = ActionChains(driver)
        # print((message).encode("unicode_escape"))
        # message=message.replace("\\n",(Keys.SHIFT+Keys.ENTER))
        # actions.send_keys(message)
        # actions.send_keys(Keys.ENTER)
        # actions.perform()

# Close chrome browser
# driver.quit()
