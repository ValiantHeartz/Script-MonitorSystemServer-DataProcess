#导入pymsql模块
import pymysql

#创建连接MYSQL的类
class TestMysql:

    #初始化变量
    def __init__(self,username,host,passwd,database):
        self.username = username
        self.host = host
        self.passwd = passwd
        self.database = database
    #创建数据库连接
    def conn_mysql(self):
        conn = pymysql.connect(user=self.username,host=self.host,password=self.passwd,db=self.database)
        return conn
    #关闭数据库的提示信息
    def close_mysql(self):
        print("MySQL is Closed")
    #查询数据
    def get_data(self):
        self.conn = self.conn_mysql()
        cur = self.conn.cursor()
        #
        while True:
            sql = input('输入SQL语句:')
            cur.execute(sql)
            # sql = "select *;"
            results = cur.fetchall()
            for i in results:
                print(str(i))
            yn = input('按N断开连接，任意键继续：').strip()
            if yn == 'N':
                break
        #
        cur.close()
        self.close_mysql()

if __name__ == "__main__":
    #定义变量
    # username = input('用户名:').strip()
    # host = input('主机名:').strip()
    # passwd = input('密码:').strip()
    # database = input('库名:').strip()
    #使用try--except
    try:
        #创建TestMysql的实例
        mysql = TestMysql("root","localhost","103220","mytestbase")
        mysql.conn_mysql()
        mysql.get_data()
    except pymysql.err.ProgrammingError as e:
        print("Exception Error is %s"%(e))
    except pymysql.err.OperationalError as e:
        print("Exception Error is %s"%(e))
