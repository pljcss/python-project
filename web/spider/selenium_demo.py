from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    # 调用 chrome 驱动
    driver = webdriver.Chrome()
    #
    # driver.set_window_size(1200, 900)
    #
    # # driver.get("https://www.zhihu.com/signup?next=%2F")
    # # driver.get("https://cuiqingcai.com/1076.html")
    driver.get("http://dianping.com")
    # driver.get("https://www.baidu.com/")
    #
    # print(driver.page_source)
    print(driver.get_cookies())
    # # driver.close()
    #
    # # 截图
    # # driver.save_screenshot("codingpy.png")
    # # driver.close()
    #
    #

    # driver = webdriver.Chrome()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # print(driver.title)
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # print(driver.page_source)