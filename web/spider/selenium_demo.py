from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
if __name__ == '__main__':
    # 调用 chrome 驱动
    # driver = webdriver.Chrome()
    # driver.set_page_load_timeout(5)
    # driver.set_script_timeout(5)  # 这两种设置都进行才有效
    #
    # driver.set_window_size(1200, 900)
    #
    # # driver.get("https://www.zhihu.com/signup?next=%2F")
    # # driver.get("https://cuiqingcai.com/1076.html")

    # try:
    #     driver.get("http://www.dianping.com/shop/98394949")
    # except:
    #     driver.execute_script('window.stop()')

    # try:
    #     driver.get("http://www.dianping.com/shop/98394949")
    #     # driver.get("http://www.dianping.com")
    #     # print(driver.page_source)
    #     cookies = driver.get_cookies()
    #     print(cookies)
    # except TimeoutException:
    #     driver.execute_script('window.stop()')
    #     print(driver.page_source)



    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3)  #后面可以使用wait对特定元素进行等待

    driver.get('http://www.dianping.com/shop/98394949')
    # some code to work.

    time.sleep(2)
    print(driver.get_cookies())
    print("Reach end.")

    # driver.close()


        # driver.execute_script('window.stop()')
    # driver.get("http://www.dianping.com")
    # driver.get("https://www.baidu.com/")
    #
    # print(driver.page_source)

    # cookies = driver.get_cookies()
    #
    # print(cookies)
    #
    # driver.close()

    # elem = driver.find_element_by_id('J-search-input')
    #
    # elem.clear()
    # elem.send_keys("火锅")
    # elem.send_keys(Keys.RETURN)



    # driver.close()



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