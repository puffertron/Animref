from tkinter import *
import imageio.v3 as imageio
from PIL import Image, ImageTk
from time import perf_counter, sleep
import youtube_dl

def stream(index):
    try:
        before = perf_counter()
        image = video[0]
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        after = perf_counter()
        delta = int((after - before)*1000)   #rough!!
        print(delta)
        l1.after(delay-delta, lambda: stream())
    except Exception as e:
        print(e)
        video.close()
        return   
########### Main Program ############
root = Tk()
root.title('Video in a Frame')
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
#get url
tweeturl = "https://twitter.com/IIuvatar_/status/1620554094300520448"
vidurl = ""
ydl_opts = {
    #'forceurl': 'true'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([tweeturl])


video_name = "R:\Art\Animation Sketches\supercube10000-0239.mp4"   #Image-path
video = imageio.imread(video_name, plugin="pyav")
delay = int(33)
print (delay)
stream()
root.mainloop()