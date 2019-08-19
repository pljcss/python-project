import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq

def request_demo():
    url = 'http://quotes.toscrape.com/js/'
    response = requests.get(url)

    doc = pq(response.text)
    print('Quotes:', doc('.quote').length)
    # print(response.text)


async def pyppeteer_demo():
    url1 = 'http://quotes.toscrape.com/js/'
    url1 = 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/'
    browser = await launch(headless=False, autoClose=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto(url1)
    # await page.screenshot(path='example.png',fullPage=True)
    # await page.pdf(path='example.pdf')
    # await page.evaluate(
    #     '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    # print(await page.content())

    # await browser.close()


if __name__ == '__main__':
    # request_demo()
    asyncio.get_event_loop().run_until_complete(pyppeteer_demo())