from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time

if __name__ == '__main__':
    # 调用 chrome 驱动
    driver = webdriver.Chrome()

    # driver.set_window_size(1200, 900)

    driver.get("https://www.baidu.com/")
    # print(driver.page_source)

    # cookies = driver.get_cookies()
    # print(cookies)

    # driver.close()

    # elem = driver.find_element_by_id('J-search-input')
    #
    # elem.clear()
    # elem.send_keys("火锅")
    # elem.send_keys(Keys.RETURN)


    # 截图
    driver.save_screenshot("codingpy.png")
    driver.close()
