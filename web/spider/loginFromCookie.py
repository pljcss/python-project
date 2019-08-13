import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie':'_zap=e6fb4168-5bd3-49e3-b0bd-0dc3cd2d6d44; d_c0="ACBpMcp4dQ-PTrQAlawrSGOrUJOlN57SQzA=|1558361439"; __gads=ID=56977c21eeb444ac:T=1558361442:S=ALNI_MZd2DWQqaddRtj8UhhZkV9BQmULSA; z_c0="2|1:0|10:1558750549|4:z_c0|92:Mi4xc0xYRkF3QUFBQUFBSUdreHluaDFEeVlBQUFCZ0FsVk5WZlBWWFFEQjVsT09jWUMwTG51NFFCZThTTDlDbjZkQTVB|21c878eef320f70b4ad9bdece873f3de582c220c50b17a613e3588bf59ea0820"; __utmv=51854390.100--|2=registration_date=20161205=1^3=entry_date=20161205=1; _xsrf=06a96db5-ae83-47b5-af29-f526bf6a5e69; q_c1=2ba81dd40b1f45d78d67d23b793ebd3e|1561389191000|1558361440000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; tst=r; __utma=51854390.1769722930.1558750765.1558750765.1561642052.2; __utmb=51854390.0.10.1561642052; __utmc=51854390; __utmz=51854390.1561642052.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/19942068/answer/677558035',
    'Connection':'keep-alive',
}

# proxies = {'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}

session = requests.Session()
response = session.get("https://www.zhihu.com/topic", headers=headers)

print(response.status_code)
print(response.text)


