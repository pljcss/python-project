from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get("https://www.zhihu.com/signup?next=%2F")
    print(driver.page_source)
    # driver.close()



