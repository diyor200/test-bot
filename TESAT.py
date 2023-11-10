import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from fake_useragent import FakeUserAgent


def fake_user_agent():
    return FakeUserAgent.random


options = Options()
options.add_argument(f"user-agent={fake_user_agent()}")


def start_action(initiate="a8bb7b5b-9568-4d6f-a8dc-6b114299f7fc"):
    driver = webdriver.Chrome(options=options)
    driver.start_client()
    driver.implicitly_wait(time_to_wait=1000)
    driver.get('https://whoer.net/')
    time.sleep(10)
    url = f"https://openbudget.uz/boards/initiatives/initiative/31/{initiate}"
    driver.get(url, )
    for i in range(5):
        time.sleep(2)
        element = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[4]/p/button[2]")
        element.click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        print(driver.application_cache)
    driver.close()
    return "success"


if __name__ == "__main__":
    start_action()
