import asyncio
from pyppeteer import launch
import requests
from pyquery import PyQuery as pq
import time
import random


def request_demo():
    url = 'http://quotes.toscrape.com/js/'
    response = requests.get(url)

    doc = pq(response.text)
    print('Quotes:', doc('.quote').length)
    # print(response.text)

width, height = 1280, 800
async def pyppeteer_demo(username, pwd):
    url1 = 'http://quotes.toscrape.com/js/'
    url1 = 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/'

    url1 = 'https://login.taobao.com/member/login.jhtml'

    # --disable-infobars, 禁止提示
    # window-size, 设置页面显示
    browser = await launch(headless=False, autoClose=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    print(await browser.userAgent())
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto(url1)
    await asyncio.sleep(2)

    await page.click('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')

    # await page.click('#J_Form > div.login-links > a.forget-pwd')
    await page.type('#TPL_username_1', username, {'delay': input_time_random() - 50})
    await page.type('#TPL_password_1', pwd, {'delay': input_time_random()})

    await page.waitFor(2)

    # 检测是否有滑块, 通过检测是否有相关的元素
    slider = await page.Jeval('#nocaptcha', 'node => node.style')

    print(slider)

    if slider:
        print('出现滑块')
        await asyncio.sleep(2)
        # 不同场景的验证码模块能名字不同
        await page.hover('#nc_1_n1z')

        start_x = page.mouse._x
        print('-----', start_x)

        await page.mouse.down()
        # await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        # await page.mouse.move(2000, 0, {'delay': input_time_random() - 50})

        # 带有步长的方式可能会被识别出,如设置为30
        await page.mouse.move(2000, 0, {'steps': 3})
        # await page.mouse.move(2000, 0)

        # await move_utils(page)
        await page.mouse.up()

        await asyncio.sleep(2)
        # await page.keyboard.press('Enter')

        # await page.click('#J_SubmitStatic')
    else:
        # await page.click('#J_SubmitStatic')
        pass
    #
    # time.sleep(2)
    #
    # await page.keyboard.press('Enter')
    # # await page.waitFor(20)
    # await page.waitForNavigation()

    # 截屏
    # await page.screenshot(path='example.png',fullPage=True)
    # 保存为PDF
    # await page.pdf(path='example.pdf')
    # await page.evaluate(
    #     '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    # print(await page.content())

    # await browser.close()

def input_time_random():
    return random.randint(100, 151)

async def move_utils(page):
    for i in range(10):
        await page.mouse.move(i * 100, 0)
        await page.waitFor(1)

if __name__ == '__main__':
    # request_demo()
    asyncio.get_event_loop().run_until_complete(pyppeteer_demo('13196986255', 'cs1002'))