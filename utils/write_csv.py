import csv

def write_csv():
    # 文件头
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

    # 待写入文件
    rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
             'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
            {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
             'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
            {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
             'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
            ]

    with open('/Users/caosai/Desktop/test2.csv','a') as f:
        # f_csv = csv.DictWriter(f, headers)
        # f_csv.writeheader()

        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    write_csv()