import tkinter as tk
from tkinter import *

#  ========================= GUI ===================================================
#  general settings
root = Tk()
root.title('Instagram profile downloader!')
root.geometry('300x250')
root.resizable(width=False, height=False)

#  user name lable----------------------
usernamelable = tk.Label(root, text='User Name:')
usernamelable.place(x=25, y=40)

#  user name entry----------------------
username = Entry(root)
username.place(x=95, y=40)

#  profile download button--------------
pb = Button(root, text='Get Profile image') 
pb.place(x=95, y=150)

# main loop-----------------------------
root.mainloop()
