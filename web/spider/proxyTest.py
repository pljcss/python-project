import requests

def test():
    # 设置shadowsocks代理ip成功
    proxies = {'http': 'http://127.0.0.1:1087',
               'https': 'http://127.0.0.1:1087'}

    # 设置请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
               'Connection': 'keep-alive'}

    # http://icanhazip.com
    r =requests.get("http://icanhazip.com", headers=headers, proxies=proxies)

    print(r.text)

if __name__ == '__main__':
    test()