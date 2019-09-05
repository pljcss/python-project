import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq
import time
import random



width, height = 1280, 800
async def pyppeteer_demo(username, pwd):

    url1 = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&rsv_pq=9df02d7900093dbd&rsv_t=bac9wjaM2dzphhn9t5saAoN5AzYB5taXpfFJReSLzecje6Yy%2FGL7UAXUywY&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=499&rsv_sug4=1119'

    url1 = 'http://www.dianping.com/shop/110281977'

    url1 = 'http://106.12.39.147/'
    # --disable-infobars, 禁止提示
    # window-size, 设置页面显示
    # browser = await launch(headless=False, autoClose=False, args=['--disable-infobars',
    #                                                               f'--window-size={width},{height}',
    #                                                               '--proxy-server=127.0.0.1:1087',
    #                                                               '--proxy-server=127.0.0.1:1087'])



    browser = await launch(headless=False, autoClose=False, args=['--disable-infobars',
                                                                  f'--window-size={width},{height}',
                                                                  '--proxy-server=117.83.137.7:32982',
                                                                  '--proxy-server=117.83.137.7:32982'])



    print(await browser.userAgent())
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto(url1, {'waitUntil':'domcontentloaded'})
    await asyncio.sleep(2)

    print(await page.content())
    # await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(pyppeteer_demo('xxxx', 'xxxx'))
