from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,random


if __name__ == '__main__':
    # 打开页面至屏幕最大尺寸
    driver = webdriver.Chrome()
    driver.get('https://account.ch.com/NonRegistrations-Regist')
    driver.maximize_window()
    #获取输入手机号码的表单
    input1 = driver.find_element_by_name('phoneNumberInput')
    # 输入注册号码
    input1.send_keys('13196986244')
    time.sleep(0.2)
    # 获取打开滑块验证码页面的元素
    getcheck=driver.find_element_by_id('getDynamicPwd')
    # 点击进入滑块验证码页面
    getcheck.click()