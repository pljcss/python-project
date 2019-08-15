from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
在   main   方法中才会延迟输出
"""
def auto_search():
    """
    自动搜索
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

    # driver.close()

if __name__ == '__main__':
    # auto_search()

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

    # driver.close()