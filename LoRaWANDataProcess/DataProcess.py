f = open("../LoRaWANHttpServer/LoRaWANData428.txt", 'r')
for row in f.readlines():
    data = row[20:len(row)].split(',')
    print(len(data))