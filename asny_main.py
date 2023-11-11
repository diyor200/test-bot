import selenium_async
import asyncio


def get_title(driver: selenium_async.WebDriver):
    driver.get("https://www.python.org/")
    print(driver.title)


if __name__ == "__main__":
   asyncio.run(selenium_async.run_sync(get_title))