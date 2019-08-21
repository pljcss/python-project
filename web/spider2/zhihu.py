# -*- coding:utf-8 -*-
import asyncio
from pyppeteer import launch
import random


width, height = 1280, 960
class ZhiHuLogin(object):
    # 初始化参数
    def __init__(self, username, password):
            self.url = 'https://www.zhihu.com/'
            self.username = username
            self.password = password

    # 运行 pyppeteer
    async def run(self):
        browser = await launch(headless=False, autoClose=False,
                               args=['--disable-infobars', f'--window-size={width},{height}'])

        page = await browser.newPage()
        await page.setViewport({'width': width, 'height': height})
        await page.goto(self.url)

        # 点击到账号密码登录页面
        await page.click('#root > div > main > div > div > div.Card.SignContainer-content > div > form > div.SignFlow-tabs > div:nth-child(2)')

        # 输入用户名和密码
        await page.type('#root > div > main > div > div > div.Card.SignContainer-content > div > form > div.SignFlow-account > div.SignFlowInput.SignFlow-accountInputContainer > div.SignFlow-accountInput.Input-wrapper > input', self.username, {'delay': input_time_random() - 50})
        await page.type('#root > div > main > div > div > div.Card.SignContainer-content > div > form > div.SignFlow-password > div > div.Input-wrapper > input', self.password, {'delay': input_time_random()})

        # 点击登录按钮
        # await page.click('#root > div > main > div > div > div.Card.SignContainer-content > div > form > button')

def input_time_random():
    return random.randint(200, 351)

if __name__ == '__main__':
    login = ZhiHuLogin('xxxxxx', 'xxxxxx')
    asyncio.get_event_loop().run_until_complete(login.run())