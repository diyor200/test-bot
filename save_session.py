import asyncio
import time
import pickle
from concurrent.futures.thread import ThreadPoolExecutor

import selenium_async
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

executor = ThreadPoolExecutor(10)

options = webdriver.ChromeOptions()
options.add_argument('--headless')

service = "https://my.gov.uz/oz/car/create"
    # l = ["40E820OA", "AAC", "6603157"]


def get_data(data: dict, loop):
    loop.run_in_executor(executor,start_action(data))

def start_action(data: dict):
    print(data)
    url = "https://my.gov.uz/oz"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/a[1]").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[1]/div/div/div[2]/div/div[1]/button').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="login"]').send_keys("Diyorbek01")
    # driver.find_element(By.ID, 'password').send_keys('Tatu65019$')
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div/div/form/div[2]/div[2]/button').click()
    # time.sleep(5)
    # pickle.dump(driver.get_cookies(), open("diyorbek.session", "wb"))
    for cookie in pickle.load(open("diyorbek.session", "rb")):
        driver.add_cookie(cookie)
        print(cookie)


    driver.refresh()
    time.sleep(0.3)
    driver.get(service)
    driver.find_element(By.XPATH, '//*[@id="car-registration_number"]').send_keys(data["car_number"])
    driver.find_element(By.XPATH, '//*[@id="car-texp_sery"]').send_keys(data["license_code"])
    n = driver.find_element(By.XPATH, '//*[@id="car-texp_number"]')
    n.send_keys(data["license_number"])
    n.send_keys(Keys.ENTER)
    time.sleep(10)

if __name__ == "__main__":
    data = {
        "car_number": "40E820OA",
        "license_code": "AAC",
        "license_number": "6603157",
    }
    loop = asyncio.get_event_loop()
    for _ in range(5):
        get_data(data, loop)
    # coros = [get_data(data, loop) for _ in range(3)]
    # print(coros)
    loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
