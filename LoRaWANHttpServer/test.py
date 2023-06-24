import datetime
datanum = 36
id_frame_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0};
lorawandata="3,14,42,35,27,1,22,0,1,0,59,0,0,3,10,35,20,66,10,84,103,0,2,255"
macPayload = lorawandata.split(',')[13:]


for i in range(10):
    if(i*10 < len(macPayload) and macPayload[i*10] != "255"):
        id_frame_dict[macPayload[i*10]]-=1
        if()

recievenum = 0
for i in len(id_frame_dict):
    if(len('0'+(i+1)) <= -datanum):
        recievenum += 1
print("receicve rate:" + recievenum/datanum)
print(id_frame_dict)
print(len(macPayload))
