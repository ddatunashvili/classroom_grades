from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from pprint import pprint as pp

# Provide the full path to the 'chromedriver.exe' executable
chromedriver_path = 'chromedriver.exe'  # Replace with the actual path

# Create a service object for the ChromeDriver with the specified executable path
service = Service(executable_path=chromedriver_path)

# Create the options object using the Options class
options = Options()
options.add_argument(r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
options.add_argument("--disable-webgl")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=NetworkService")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)

# Create the WebDriver instance with the specified service and options
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=service, options=options)


url = input("write url  ")
# driver.minimize_window()
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
input("start...")
# time.sleep(2)
# driver.find_element(
#     By.CSS_SELECTOR, 'input[type="email"]').send_keys(gmail_username)
# driver.find_element(
#     By.CSS_SELECTOR, 'input[type="email"]').send_keys(Keys.RETURN)
# time.sleep(3)
# driver.find_element(
#     By.CSS_SELECTOR, 'input[type="password"]').send_keys(gmail_password)
# driver.find_element(
#     By.CSS_SELECTOR, 'input[type="password"]').send_keys(Keys.RETURN)
# time.sleep(10)

while True:
    try:
        input("choose group and people tab...")
        input("next...")
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
                        if "ab" in name:
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
            #tr
            en = "abcdefghijklmnopqrstuvwxyz"
            ge = "აბცდეფგჰიჯკლმნოპქრსტუვწხყზ"
            alph = dict(zip(en, ge))
            alph["ცჰ"] = "ჩ"
            alph["კრ"] = "ქრ"
            alph["სჰ"] = "შ"
            alph["კჰ"] = "ხ"
            alph["დზ"] = "ძ"
            alph["პხ"] = "ფხ"
            alph["ტს"] = "ც"
            for en, ge in alph.items():
                student_name = [i.replace(ge, en) for i in student_name]
                student_name = "".join(student_name)
            #tr
            scores[student_name] = f"{data[0]}-{data[1]}-{data[2]}-{data[3]}-{data[4]}"   
            driver.back() 
        print(scores)
        scors = []
        for student_name, score in scores.items():
            scors.append(f"{student_name}: {score}\n")

        with open("scores.txt", "w", encoding="utf-8") as f:
            f.writelines(scors)
    except Exception as e:
        print("e")
        print("\n\nerror happend ! .. :(")