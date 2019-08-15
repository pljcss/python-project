from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time


def auto_search():
    """
    自动进行搜索
    :return:
    """
    driver = webdriver.Chrome()

    url = "http://www.dianping.com"
    # url = "https://www.baidu.com/"
    driver.get(url)

    # 获取页面元素
    print(driver.page_source)

    # 获取 cookies
    cookies = driver.get_cookies()
    print(cookies)

    # 搜索
    elem = driver.find_element_by_id('J-search-input')
    elem.clear()
    elem.send_keys("火锅")
    elem.send_keys(Keys.RETURN)

    driver.close()

def no_delay_output():
    """
    非延迟输出,正常会等页面加载完毕后才进行输出,
    此种方式在加载界面的时候, 会输出
    :return:
    """
    # 修改页面加载策略
    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟, 即等待页面加载完成再输出
    desired_capabilities["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome()

    # 后面可以使用wait对特定元素进行等待
    wait = WebDriverWait(driver, 3)

    driver.get('http://www.dianping.com/shop/98394949')

    time.sleep(2)
    print(driver.get_cookies())
    print("end")

    driver.close()

if __name__ == '__main__':
    no_delay_output()
