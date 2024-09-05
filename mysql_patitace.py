import pymysql

# 连接到MySQL数据库
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='pypatitace',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 使用cursor()方法获取操作游标
try:
    with connection.cursor() as cursor:
        # 创建一个表
        sql = """CREATE TABLE IF NOT EXISTS customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    address VARCHAR(255))"""
        cursor.execute(sql)

        # 插入数据
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        cursor.execute(sql, ('John', 'Highway 21'))

    # 提交更改
    connection.commit()

    with connection.cursor() as cursor:
        # 查询数据
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # 关闭连接
    connection.close()




