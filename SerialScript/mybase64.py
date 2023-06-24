import json,base64

if __name__ == '__main__':
    # # 要编码的数据
    # data = {"uname":"Tanch","uid":3}
    # # 先转化为bytes类型数据
    # data_bytes = json.dumps(data).encode()
    # print(type(data_bytes))
    # # 编码
    # base_data = base64.b64encode(data_bytes)
    # print(base_data)
    #
    # # 解码
    # string_bytes = b"eyJ1bmFtZSI6ICJUYW5jaCIsICJ1aWQiOiAzfQ=="
    # ori_data = base64.b64decode(string_bytes).decode()
    # # 字符串
    # print(ori_data)
    # # 变回原来的字典
    # data = json.loads(ori_data)
    # print(type(data))
    str = "eyJtZXRob2QiOiJyZXBvcnQiLCJjbGllbnRUb2tlbiI6IjIwMjItMDQtMTlUMDg6MDY6MzUuOTQ4WiIsInBhcmFtcyI6eyJWT0wiOjE4Nn0sIm1ldGFMb1JhIjoie1wiZnJhbWVUeXBlXCI6NCxcImZQb3J0XCI6MSxcImZDbnRcIjoxOTYsXCJmcmVxdWVuY3lcIjo0NzA1MDAwMDAsXCJkclwiOjUsXCJyc3NpXCI6LTM1LFwic25yXCI6MTMsXCJwYXlsb2FkU2l6ZVwiOjR9In0="
    #str = "gQECAw=="
    de = base64.b64decode(str)
    print(de.decode().split())
    # for i in range(len(de)):
    #     print(de[i], end = ',')