import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq
import time
import random


width, height = 1280, 800
class TxCaptcha(object):
    def __init__(self):
        url = 'https://open.captcha.qq.com/online.html'
        self.url = url

    async def run(self):
        # 开启浏览器
        browser = await launch(headless=False, autoClose=False, args=['--disable-infobars', f'--window-size={width},{height}'])
        # 新建页面
        page = await browser.newPage()
        # 设置浏览器尺寸
        await page.setViewport({'width': width, 'height': height})
        # 打开URL
        await page.goto(self.url)

        await asyncio.sleep(1)
        # 点击有滑动验证码的页面
        await page.click('#app > section.wp-on-online > div > div > div > div.wp-on-box.col-md-5.col-md-offset-1 > div.wp-onb-tit > a:nth-child(2)')
        await asyncio.sleep(1)
        # 点击体验验证码
        await page.click('#code')
        await asyncio.sleep(2)

        # 验证码页面是在frame中, 需要找到指定frame
        frame_list =  page.frames

        # 找到指定frame
        frame_str = None
        for frame in frame_list:
            # print(frame.name)

            if frame.name == 'tcaptcha_iframe':
                frame_str = frame

        await asyncio.sleep(2)
        # 模拟点击操作
        await frame_str.hover('#tcaptcha_drag_thumb')
        await page.mouse.down()
        await page.mouse.move(1000, 0, {'steps': 30})
        await page.mouse.up()


if __name__ == '__main__':
    txCaptcha = TxCaptcha()
    asyncio.get_event_loop().run_until_complete(txCaptcha.run())
