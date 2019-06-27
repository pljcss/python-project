import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NjE2MTg3ODMsImV4cCI6MTU2MTYyMjM4MywibmJmIjoxNTYxNjE4NzgzLCJqdGkiOiJsM3VpOTRsZ1VKNEFtSzhQIiwic3ViIjo3NDA3NTgsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.vI-KVFlgErXhHl8Ynv6cGJz4-87YWe-CamROFCS7Fs4',
}

proxies = {'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}

session = requests.Session()
response = session.get("http://radar.itjuzi.com/investevent", proxies=proxies, headers=headers)

print(response.status_code)
print(response.text)


