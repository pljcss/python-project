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

    await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
    # await page.setExtraHTTPHeaders({
    #     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    # })

    await page.setViewport({'width': width, 'height': height})
    await page.goto(url1)
    # await asyncio.sleep(2)

    # print(page.cookies())
    # doc = pq(await page.content())
    # print('Quotes:', doc('.quote').length)


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(get_cookie('http://www.dianping.com/shop/65751792'))