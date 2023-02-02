import tkinter as tk
from threading import Thread
from time import perf_counter, sleep
from tkinter import ttk
from ttkwidgets import TimeLine, TickScale

import imageio.v3 as iio
import youtube_dl
from PIL import Image, ImageTk
from tkinterdnd2 import DND_TEXT, TkinterDnD

from videoplayer import VideoPlayer

root = TkinterDnD.Tk()

## MAIN WINDOW SETUP
root.title('AnimRef')

window_w = 700
window_h = 350

center_x = int(root.winfo_screenwidth() / 2  - window_w / 2)
center_y = int(root.winfo_screenheight() / 2 - window_h / 2)

root.geometry(f"{window_w}x{window_h}+{center_x}+{center_y}")

max_height = 300

##setup ui
f1=ttk.Frame()
l1 = ttk.Label(f1)
l1.pack()
f1.pack(fill='x')


player = VideoPlayer(l1)
player.load_video("https://upload.wikimedia.org/wikipedia/commons/d/d3/Newtons_cradle_animation_book_2.gif")

playbtn = ttk.Button(text='play', command=player.start)
stopbtn = ttk.Button(text='stop', command=player.stop)


tl = TickScale(orient='horizontal')

playbtn.pack(side= 'left')
stopbtn.pack(side= 'left')



tl.pack(fill='x')

f1.drop_target_register(DND_TEXT)
f1.dnd_bind('<<Drop>>', lambda e: player.load_video(e.data))


##input
root.bind_all(",", lambda e: player.back(2))
root.bind_all('.', lambda e: player.forward(2))

root.mainloop()

