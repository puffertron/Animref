import tkinter as tk
from itertools import cycle
from threading import Thread
from time import perf_counter, sleep
from tkinter import ttk

import imageio.v3 as iio
import youtube_dl
from PIL import Image, ImageTk


class VideoPlayer():
    def __init__(self, tkframe):
        self.tkframe = tkframe
        self.fps = 0
        self.currentframe = 0
        self.video = None
        self.playing = False
        self.loop = True
        self.videolength = 0
        self.max_height = 300

        self.debug = True # swap for self.debug = false later



    def load_video(self, url):
        rawurl = url
        #video ID, may be unstable and weird depoending on platform?
        id = rawurl.split('/')[-1]

        data = ''

        ##get the video
        ydl_opts = {
            #'forceurl': 'true'
            #'outtmpl': '%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #ydl.download([rawurl])
            # data = ydl.extract_info(rawurl)
            # realurl = data['formats'][-1]['url']
            # print(realurl)
            pass
            
        print("loading vid")
        self.video = iio.imread(url)
        print('done!')
        try:
            self.fps = int(iio.immeta(url)['fps'])
        except:
            print('could not grab fps')
            self.fps = 24
        self.videolength = len(self.video)

        self.showframe(self.video[0])
        
    def showframe(self, frame):
        #resisze and convert
        frame_image = Image.fromarray(frame)
        aspect = frame_image.width / frame_image.height
        frame_image = frame_image.resize(
            (int(self.max_height*aspect), self.max_height))
        frame_image=ImageTk.PhotoImage(frame_image)

        #update tk image frame
        self.tkframe.configure(image=frame_image)
        self.tkframe.image = frame_image
    
    def update(self):
        before = perf_counter()
        duration = float(1/self.fps)
        while self.playing:
            self.currentframe += 1
            if self.loop:
                self.currentframe = self.currentframe % self.videolength
            elif self.currentframe > self.videolength:
                self.playing = False
                self.currentframe = self.videolength #might need a -1?

            #display a frame
            self.showframe(self.video[self.currentframe])

            #timing
            delta = duration + before
            after = perf_counter()
            delta = delta - after
            print(delta)

            if delta > 0:
                sleep(delta)

            before = perf_counter()

    def stop(self):
        self.playing = False
    
    def start(self):
        if not self.playing:
            self.playing = True
            thread = Thread(target=self.update)
            thread.daemon = True
            thread.start()

    def rewind(self):
        pass
    
    def forward(self, count):
        self.currentframe += count
        self.currentframe = self.currentframe % self.videolength
        self.showframe(self.video[self.currentframe])

    def back(self, count):
        self.currentframe -= count
        self.currentframe = (self.currentframe % self.videolength +    self.videolength) %  self.videolength
        self.showframe(self.video[self.currentframe])
    
    # def play(self):
    #     for frame in self.video:
    #         frame_image = Image.fromarray(frame)
    #         aspect = frame_image.width / frame_image.height
    #         frame_image = frame_image.resize((int(max_height*aspect), max_height))
    #         frame_image=ImageTk.PhotoImage(frame_image)
    #         l1.config(image=frame_image)
    #         l1.image = frame_image

    #         delta = duration + before
    #         after = perf_counter()
    #         delta = delta - after
            
    #         if self.debug:
    #             print(delta)

    #         if delta > 0:
    #             sleep(delta)

    #         before = perf_counter()
    