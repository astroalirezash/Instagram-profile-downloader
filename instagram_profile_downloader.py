import tkinter as tk
from tkinter import *
import instaloader

#  ======================== Instaloader func ======================================

def prof_downloader():
    loader = instaloader.Instaloader()
    loader.download_profile(username.get(), profile_pic_only=True)


#  ========================= GUI ===================================================
#  general settings
root = Tk()
root.title('Instagram profile downloader!')
root.geometry('300x250')
root.resizable(width=False, height=False)

# some customize-------------------------
frame = LabelFrame(root, text='Instagram', bg='#f0f0f0', font=(20))
frame.pack(expand=True, fill=BOTH)

#  user name lable----------------------
usernamelable = tk.Label(root, text='User Name:')
usernamelable.place(x=25, y=40)

#  user name entry----------------------
username = Entry(root)
username.place(x=95, y=40)

#  profile download button--------------
pb = Button(root, text='Get Profile image', command=lambda: prof_downloader()) 
pb.place(x=95, y=150)

# main loop-----------------------------
root.mainloop()
