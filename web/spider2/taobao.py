# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


"""此种登录方式会被识别"""
class TaoBaoSpider(object):
    def __init__(self, username, password):
        """初始化参数"""
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        # 初始化用户名密码
        self.username = username
        self.password = password

        options = webdriver.ChromeOptions()

        # 不加载图片,加快访问速度
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式,避免被识别
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])

        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)

    def run(self):
        """登陆接口"""
        self.browser.get(self.url)

        # 这里设置等待：等待输入框
        try:
            # 这里设置等待：等待输入框
            login_element = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
            login_element.click()

            # username
            red_username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1')))
            red_username.send_keys(self.username)

            # password
            red_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1')))
            red_password.send_keys(self.password)

            # 登录
            time.sleep(10)
            submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_SubmitStatic')))
            submit.click()


        except Exception as e:
            print('登录失败 - ', e)
            self.browser.close()

if __name__ == '__main__':
    spider = TaoBaoSpider('xxxxxx', 'xxxxxx')
    spider.run()