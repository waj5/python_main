import pymysql


class DatabaseBackup:
    def __init__(self, local_db_config, remote_db_config):
        self.local_db_config = local_db_config
        self.remote_db_config = remote_db_config
        self.local_connection = None
        self.remote_connection = None

    def connect_databases(self):
        try:
            self.local_connection = pymysql.connect(**self.local_db_config)
            self.remote_connection = pymysql.connect(**self.remote_db_config)
            print("连接至本地和远程数据库成功！")
        except pymysql.MySQLError as e:
            print(f"数据库连接失败: {e}")
            raise

    def close_connections(self):
        if self.local_connection:
            self.local_connection.close()
        if self.remote_connection:
            self.remote_connection.close()

    def check_and_create_table(self):
        try:
            with self.remote_connection.cursor() as cursor:
                # 验证连接和权限
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                if result["1"] != 1:
                    raise pymysql.MySQLError("连接验证失败")

                # 检查表是否存在
                check_table_sql = """
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_name = %s
                AND table_schema = %s
                """
                cursor.execute(
                    check_table_sql, ("bilibili", self.remote_db_config["db"])
                )
                result = cursor.fetchone()

                if result["COUNT(*)"] == 0:
                    # 如果表不存在，则创建表
                    create_table_sql = """
                    CREATE TABLE bilibili (
                        id INT NOT NULL AUTO_INCREMENT,
                        title VARCHAR(255) NOT NULL,
                        views INT DEFAULT 0,
                        danmaku_count INT DEFAULT 0,
                        publish_date VARCHAR(255) DEFAULT NULL,
                        likes INT DEFAULT 0,
                        coins INT DEFAULT 0,
                        favorites INT DEFAULT 0,
                        shares INT DEFAULT 0,
                        description TEXT,
                        comments INT DEFAULT 0,
                        PRIMARY KEY (id)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                    """
                    cursor.execute(create_table_sql)
                    print("bilibili 表已创建")
                else:
                    print("bilibili 表已存在，跳过创建步骤")
        except pymysql.MySQLError as e:
            print(f"检查或创建表失败: {e}")
            raise

    def backup_data(self):
        try:
            with self.local_connection.cursor() as local_cursor, self.remote_connection.cursor() as remote_cursor:
                # 从本地数据库读取数据
                local_cursor.execute("SELECT * FROM data")
                data = local_cursor.fetchall()

                # 将数据插入到远程数据库
                for row in data:
                    columns = ", ".join(row.keys())
                    placeholders = ", ".join(["%s"] * len(row))
                    sql = f"INSERT INTO bilibili ({columns}) VALUES ({placeholders})"
                    remote_cursor.execute(sql, tuple(row.values()))

                # 提交事务
                self.remote_connection.commit()
                print("数据备份成功!")

        except pymysql.MySQLError as e:
            self.remote_connection.rollback()
            print(f"备份数据失败: {e}")
            raise


# 配置数据库连接参数
local_db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "db": "bilibili",
    "port": 3306,
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

remote_db_config = {
    "host": "192.168.86.129",
    "user": "root",
    "password": "Password123@mysql",
    "db": "dataease",
    "port": 3306,
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

if __name__ == "__main__":
    db_backup = DatabaseBackup(local_db_config, remote_db_config)
    try:
        db_backup.connect_databases()
        db_backup.check_and_create_table()
        db_backup.backup_data()
    finally:
        db_backup.close_connections()
