from selenium import webdriver


if __name__ == '__main__':
    # 调用 chrome 驱动
    driver = webdriver.Chrome()

    driver.set_window_size(1200, 900)

    # driver.get("https://www.zhihu.com/signup?next=%2F")
    driver.get("https://cuiqingcai.com/1076.html")

    print(driver.page_source)
    # driver.close()

    # 截图
    driver.save_screenshot("codingpy.png")
    driver.close()