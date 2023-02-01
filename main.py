import tkinter as tk
from tkinter import ttk
import imageio.v3 as iio
from PIL import Image, ImageTk
import youtube_dl
from time import perf_counter, sleep
from threading import Thread


root = tk.Tk()

root.title('AnimRef')

# window_w = 700
# window_h = 200

# center_x = int(root.winfo_screenwidth() / 2  - window_w / 2)
# center_y = int(root.winfo_screenheight() / 2 - window_h / 2)

# root.geometry(f"{window_w}x{window_h}+{center_x}+{center_y}")


def stream(frames, target, fps, loop=True):
    duration = float(1/fps)
    try:
        
        before = perf_counter()
        for frame in frames:   
            frame_image = Image.fromarray(frame)
            frame_image=ImageTk.PhotoImage(frame_image)
            l1.config(image=frame_image)
            l1.image = frame_image

            delta = duration + before
            after = perf_counter()
            delta = delta - after
            print(delta)

            if delta > 0:
                sleep(delta)

            before = perf_counter()
        return

    except Exception as e:
        print(e)
        return   

rawurl = "https://twitter.com/IIuvatar_/status/1620554094300520448"
id = rawurl.split('/')[-1]

##get the video
ydl_opts = {
    #'forceurl': 'true'
    'outtmpl': '%(id)s.%(ext)s'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([rawurl])

##setup ui
f1=ttk.Frame()
l1 = ttk.Label(f1)
l1.pack()
f1.pack()

textbox = ttk.Entry()

video_name = f"{id}.mp4"
print("loading vid")
video = iio.imread(video_name)
print('stream time')
fps = int(iio.immeta(video_name)['fps'])
print(fps)
#stream(video, l1, fps)
thread = Thread(target=stream, args=(video, l1, fps))
thread.daemon = True
thread.start()

root.mainloop()

