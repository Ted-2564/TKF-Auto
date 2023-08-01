import win32api
import win32con
from time import sleep
import keyboard

def start():
      win32api.keybd_event(17, 0, 0, 0)#ctrl
      sleep(0.144)
      win32api.keybd_event(82, 0, 0, 0)#R
      sleep(0.08)
      win32api.keybd_event(82, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键R
      sleep(0.119)
      win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
      sleep(2)
      win32api.keybd_event(82, 0, 0, 0)#R
      sleep(0.08)
      win32api.keybd_event(82, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键R
      sleep(3.0)

conts=0
while True:
      start()
      if keyboard.is_pressed('P'):
            break
      conts+=1
      print(conts)


