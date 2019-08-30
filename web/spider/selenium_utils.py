from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time




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

def no_delay_cookies(url):
    """
    非延迟获取cookies
    :return:
    """
    # 修改页面加载策略
    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟, 即等待页面加载完成再输出
    desired_capabilities["pageLoadStrategy"] = "none"

    # 静默模式
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 启动浏览器
    driver = webdriver.Chrome(options=option)
    # driver = webdriver.Chrome()
    driver.delete_all_cookies()
    # 后面可以使用wait对特定元素进行等待
    wait = WebDriverWait(driver, 1)

    # driver.get('http://www.dianping.com/shop/98394949')
    driver.get(url)

    time.sleep(1)
    cookies_list = driver.get_cookies()

    cookie_dict = dict()
    for res in cookies_list:
        key = res.get("name")
        value = res.get("value")
        cookie_dict[key] = value

    print("9991111", cookie_dict)

    if cookie_dict is not None:
        lxsdk_s = cookie_dict.get("_lxsdk_s")
        if lxsdk_s is not None:
            increase_int = lxsdk_s[(int(lxsdk_s.rindex('C')) + 1):]

            with open('incre_cookid_detail', 'w') as f:
                f.write(str(increase_int))
    else:
        with open('incre_cookid_detail', 'w') as f:
            f.write(5)

    # driver.close()
    return cookie_dict

def test(url):
    driver1 = webdriver.Chrome()
    # driver.delete_all_cookies()

    driver1.get(url)

    # cookies_list = driver1.get_cookies()
    #
    # print(cookies_list)

    # driver1.close()


if __name__ == '__main__':
    # ss = no_delay_cookies("http://www.dianping.com/shop/98394949")
    # print(ss)

    # auto_search()

    # test("http://www.dianping.com/shop/2767525")
    # test("http://www.baidu.com")

    pass
