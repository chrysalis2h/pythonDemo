# This is a sample Python script.
import pymysql


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def connectMysql():
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 关闭数据库连接
    db.close()
    # print(f'resultLists ==== {resultLists}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connectMysql()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
