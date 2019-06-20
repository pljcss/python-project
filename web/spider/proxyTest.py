import requests
import telnetlib

def test():
    """
    设置代理 IP

    测试代理IP是否生效
    :return:
    """

    # 设置shadowsocks代理ip成功
    # proxies = {'http': 'http://127.0.0.1:1087',
    #            'https': 'http://127.0.0.1:1087'}

    # proxies = {'http': 'http://106.12.39.147:8899',
    #            'https': 'http://106.12.39.147:8899'}

    proxies = {'http': 'http://115.217.46.53:8888',
               'https': 'http://115.217.46.53:8888'}

    # 设置请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
               'Connection': 'keep-alive'}

    # http://icanhazip.com
    r =requests.get("http://icanhazip.com", headers=headers, proxies=proxies)

    print(r.text)

if __name__ == '__main__':
    test()

    ##### 此种方法只能测试端口是否通 #####
    # try:
    #     telnetlib.Telnet('106.12.39.147',port='8899',timeout=5)
    # except:
    #     print('该代理IP  无效')
    # else:
    #     print('该代理IP  有效')