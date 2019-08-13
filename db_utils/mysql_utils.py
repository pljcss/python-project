import pymysql

def get_connect_db():
    db = pymysql.connect(host="106.12.39.147",
                         user="root",
                         password="Cs477616*",
                         db="test_db",
                         port=3306,
                         charset="utf8")
    return db



if __name__ == '__main__':
    connection = get_connect_db()

    # 获取游标
    cursor = connection.cursor()

    # 执行查询 SQL
    cursor.execute('SELECT * FROM `EMPLOYEE` WHERE FIRST_NAME = "heheh" ')

    # 获取所有数据
    data = cursor.fetchall()

    # print(data)



    for i in data :
        print(i)
        print(i)
