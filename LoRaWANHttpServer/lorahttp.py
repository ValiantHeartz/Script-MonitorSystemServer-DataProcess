
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import base64
import ssl
import time
import datetime

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
    def set_data(self, strdata):
        self.conn = self.conn_mysql()
        cur = self.conn.cursor()
        sqlhead = "Insert into air (time, id, humidity, temperature, pm25, illumination, pm10, atmosphere, wind_speed, wind_direction) Values (now(),"
        strdata = strdata.split(',')[13:len(strdata)]
        print(strdata)
        temp = 0
        sql = sqlhead
        for tdata in strdata:
            if (temp % 10 == 1):
                temp = temp + 1
                continue
            sql = sql + tdata + ','
            temp = temp + 1
            if(temp%10 == 0):
                sql = sql[0:len(sql) - 1] + ");"
                print(sql)
                cur.execute(sql)
                self.conn.commit()
                sql = sqlhead
        results = cur.fetchall()
        for i in results:
            print(str(i))
        cur.close()
        self.close_mysql()

# 全局的数据
data = {'result': 'hello, this is python http server!'}
dir = "LoRaWANData/"
host = ('localhost', 8080)
id_frame_dict = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}

# Resquest实现GET和POST
filedate = datetime.datetime.now().strftime('%m %d %H-%M ')
# mysql = TestMysql("root","localhost","103220","mytestbase")
# mysql.conn_mysql()

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        #print(self.headers)
        #print(self.command)
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        req_datas = self.rfile.read(int(self.headers['content-length']))
        print(time+'\n')
        data = req_datas.decode().split("\"")[3]
        print("raw_data: " + data+'\n')
        decodedata = base64.b64decode(data)
        print("decoded_data: ", end='')
        print(decodedata)
        print()
        lorawandata = decodedata.decode().split("[")[1].split("]")[0]
        print("MACframe: " + lorawandata + '\n')
        # mysql.set_data(lorawandata)
        macPayload = lorawandata.split(',')[13:]

        output = time + ' ' + lorawandata

        with open(dir + filedate + 'LoRaWANData.txt', mode='a') as f:
            # f = open("LoRaWANData.txt", 'a')
            f.write(output)
            f.write('\n')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

# 开启服务器
server = HTTPServer(host, Resquest)
print("Starting server, listen at: %s:%s" % host)
server.serve_forever()

# strdata = "3,13,46,34,26,2,20,0,1,0,55,0,0,1,13,40,23,65,11,92,98,0,3,2,13,40,23,65,11,92,98,0,3"


