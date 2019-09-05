import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq
import time
import random
from bs4 import BeautifulSoup


width, height = 1280, 800
async def get_cookie(url1):

    # --disable-infobars, 禁止提示
    # window-size, 设置页面显示
    browser = await launch(headless=False, autoClose=False, args=['--disable-infobars', f'--window-size={width},{height}'])

    page = await browser.newPage()

    await page.setViewport({'width': width, 'height': height})
    await page.goto(url1, {'waitUntil':'domcontentloaded'}) # 不加这个参数会, 点评页面会加载很久

    print(await page.cookies())
    print(page.url)

    #
    await page.click('#nav > div > ul > li:nth-child(5) > div.primary-container > span > a:nth-child(3)')

    # print(await page.content())

    await asyncio.sleep(2)
    pages = await browser.pages()

    print(pages[-1].url)
    # print(await pages[-1].content())
    #J_nav_tabs > a.cur > span

    #J_nav_tabs > a:nth-child(3)
    #J_nav_tabs > a.cur
    # await pages[-1].click('#J_nav_tabs > a:nth-child(2)')
    #
    # element = await pages[-1].querySelector('#region-nav')  # 只抓取一个
    # print(element)
    # # 获取所有文本内容  执行 js
    # content = await pages[-1].evaluate('(element) => element.textContent', element)
    # print(content)
    #classfy > a:nth-child(1)
    await pages[-1].click('#classfy > a:nth-child(2)')

    # 如果不加这行, 不会加载到这个页面的内容
    await pages[-1].waitForNavigation()

    print(pages[-1].url)
    content = await pages[-1].content()

    soup = BeautifulSoup(content, features="lxml")
    # print(content)

    all_regions = soup.find('div', attrs={'id':'region-nav'}).find_all('a')

    print(all_regions)

    for item in all_regions:
        await asyncio.sleep(2)

        url = item.get('href')
        region = item.get_text()
        print(url, region)

        page = await browser.newPage()
        await page.goto(url, {'waitUntil':'domcontentloaded'})

        content1 = await page.content()

        soup1 = BeautifulSoup(content1, features="lxml")
        max_size = soup1.find('div', attrs={'class':'page'}).find_all('a')[-2].get('title')
        print('最大页码', max_size)
        # for page in all_pages:
        #     print(page.get('title'))


        # all_pages = soup1.find('div', attrs={'class':'page'}).find_all('a')
        # for page in all_pages:
        #     print(page.get('title'))
        # print(all_pages)


if __name__ == '__main__':

    # asyncio.get_event_loop().run_until_complete(get_cookie('http://www.dianping.com/shop/65751792'))
    asyncio.get_event_loop().run_until_complete(get_cookie('http://www.dianping.com/nanjing'))

