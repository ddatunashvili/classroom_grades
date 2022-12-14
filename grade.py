# -*- coding: utf-8 -*-
from logging import exception
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
# for selections
from selenium.webdriver.common.by import By

import undetected_chromedriver as UC

gmail_username = 'davitidatunashvili12'
gmail_password = 'h1287h21g8ygf8192hd87h12kjnc$%^^&T&%$%^&'
url = "https://classroom.google.com/u/1/r/NTQ4MjA2OTgzNTU0/sort-last-name"

driver = UC.Chrome(use_subprocess=True)
driver.set_window_size(400, 500)

# driver.minimize_window()
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

time.sleep(2)
driver.find_element(
    By.CSS_SELECTOR, 'input[type="email"]').send_keys(gmail_username)
driver.find_element(
    By.CSS_SELECTOR, 'input[type="email"]').send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element(
    By.CSS_SELECTOR, 'input[type="password"]').send_keys(gmail_password)
driver.find_element(
    By.CSS_SELECTOR, 'input[type="password"]').send_keys(Keys.RETURN)
time.sleep(10)

# functions


def calculate_score():
    rows = driver.find_elements(By.CSS_SELECTOR,  'main div[role="button"]')
    quiz_score = 0
    lab_score = 0
    mid_1 = 0
    mid_2 = 0
    final = 0
    for r in rows:
        r = r.find_element(By.XPATH, "..")
        if "Expand " in r.get_attribute("innerHTML"):
            try:
                name = r.find_element(By.CSS_SELECTOR,  'div:first-child').get_attribute("aria-label").split("Expand ")[1]
                value = r.find_element(By.CSS_SELECTOR,  'span:first-child span:nth-child(2) span').text
                if "Lab" in name:
                    try:
                        lab_score += int(value)
                    except:
                        pass
                elif "შუალედური 1" in name:
                    try:
                        mid_1 += int(value)
                    except:
                        pass
                elif "ფინალური" in name:
                    try:
                        final += int(value)
                    except:
                        pass
                elif "შუალედური 2" in name:
                    try:
                        mid_2 += int(value)
                    except:
                        pass
                elif "ქვიზი" in name:
                    try:
                        quiz_score += int(value)
                    except:
                        pass
            except:
                continue
    return [lab_score,quiz_score,mid_1,mid_2,final]



table = driver.find_elements(By.CSS_SELECTOR, 'tbody')[1]
students = table.find_elements(By.CSS_SELECTOR, 'tr')
scores = {}
for student in students:
    student_name = student.find_element(By.CSS_SELECTOR, 'span:nth-child(3)').text
    student.click()
    time.sleep(5)
    data = calculate_score()
    scores[student_name] = f"{data[0]}-{data[1]}-{data[2]}-{data[3]}-{data[4]}"   
    driver.back() 
print(scores)
scors = []
for student_name, score in scores.items():
    scors.append(student_name +": "+ score+"\n")

with open("scores.txt", "w") as f:
    f.writelines(scors[:-1])
