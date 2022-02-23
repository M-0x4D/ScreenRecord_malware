import socket 
import cv2
import numpy as np
from win32api import GetSystemMetrics 
import struct ## new
#import scipy.misc
from io import BytesIO
import pickle
import sys
from PIL import Image
import datetime


print('''
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |  _________   | || |     ______   | || |              | |
| | |_   __ \    | || | |_   ___  |  | || |   .' ___  |  | || |      _       | |
| |   | |__) |   | || |   | |_  \_|  | || |  / .'   \_|  | || |     (_)      | |
| |   |  __ /    | || |   |  _|  _   | || |  | |         | || |      _       | |
| |  _| |  \ \_  | || |  _| |___/ |  | || |  \ `.___.'\  | || |     (_)      | |
| | |____| |___| | || | |_________|  | || |   `._____.'  | || |              | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' ''')
    
s= socket.socket()
host = '0.0.0.0'
port = 8888
s.bind((host,port))
s.listen()
print(f"listening on port {port} ..." )
c,addr=s.accept()
print("connected ....",addr)

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))


# Specify video codec
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

  
# Specify name of Output file
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filename = f'{time_stamp}.mp4'
  
# Specify frames rate. We can choose any 
# value and experiment with it
fps = 1.0
  

width_bytes = c.recv(4096)
width = int.from_bytes(width_bytes, "big")

height_bytes = c.recv(4096)
height = int.from_bytes(height_bytes, "big")


#width = 1366
#height = 768


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, fourcc, fps, (width,height))
    
    

while True:

    
    
    while len(data) < payload_size:
        data += c.recv(4096)
        #print(sys.getsizeof(data))
       
    packed_msg_size = data[:payload_size]  #from fisrt to 5
    data = data[payload_size:]  # from 5 to end
    msg_size = struct.unpack(">L", packed_msg_size)[0]   
    #print(data)
    #np_bytes = BytesIO(data)
    #ret = pickle.load(np_bytes)
    #print(np_bytes)
    while len(data) < msg_size:
        data += c.recv(4096)
    frame_size = data[:msg_size]
    data = data[msg_size:]
    frame=pickle.loads(frame_size, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    #########frame_data = cv2.imdecode(res, cv2.IMREAD_COLOR)
    
    
    #print(res.getbuffer())
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(rgb)
    #cv2.imshow('data',rgb)
    # receive image row data form client socket
    #packed_msg_size = data[:payload_size]  #from fisrt to 5
    ####data = data[payload_size:]  # from 5 to end
    #msg_size = struct.unpack(">L", packed_msg_size)[0]
    ####while len(data) < payload_size:
        ####data += c.recv(4096)
    #frame_data = data[:msg_size]
    ####data = data[msg_size:]
    
    
    # unpack image using pickle 
    ####frame=pickle.loads(data, fix_imports=True, encoding="bytes")
    ####frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    ####rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ####captured_video.write(rgb)


# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()



