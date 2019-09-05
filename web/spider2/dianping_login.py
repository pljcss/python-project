import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq
import time
import random


width, height = 1280, 800
async def get_cookie(url1):

    # --disable-infobars, 禁止提示
    # window-size, 设置页面显示
    browser = await launch(headless=False, autoClose=False, args=['--disable-infobars', f'--window-size={width},{height}'])

    print(await browser.userAgent())
    page = await browser.newPage()

    await page.setViewport({'width': width, 'height': height})
    # await page.goto(url1)
    await page.goto(url1, {'waitUntil':'domcontentloaded'}) # 不加这个参数会, 点评页面会加载很久


    await page.click('#top-nav > div > div.group.quick-menu > span.login-container.J-login-container > a:nth-child(1)')

    await asyncio.sleep(2)

    frame_list =  page.frames

    print(frame_list)
    # 找到指定frame
    frame_str = None
    for frame in frame_list:
        # print(frame.url)
        # print(type(frame.url))
        if 'iframeLogin' in frame.url:
            print(frame.url)
            frame_str = frame


    await frame_str.click('body > div > div.qrcode-page > div.bottom-area > span')
    await frame_str.click('#tab-account')

    await frame_str.type('#account-textbox', '13263820575', {'delay': input_time_random() - 50})
    await frame_str.type('#password-textbox', 'cc515524', {'delay': input_time_random()})



    await frame_str.click('#login-button-account')


    await asyncio.sleep(2)


    #yodaBox
    await frame_str.hover('#yodaBox')
    await page.mouse.down()
    await page.mouse.move(10000, 0, {'steps': 30})
    await page.mouse.up()


def input_time_random():
    return random.randint(100, 151)

async def move_utils(page):
    for i in range(10):
        await page.mouse.move(i * 100, 0)
        await page.waitFor(1)

if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(get_cookie('http://www.dianping.com'))

