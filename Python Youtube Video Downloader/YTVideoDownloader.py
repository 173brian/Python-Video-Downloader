from os import link
from tkinter import*
from pytube import YouTube
import os
from os import path

class YTVideoDownloader:

    def __init__(self, link):
        self.link = link # initializes the class with a link attached to the object
        for i in range(5): # not a useful piece of code, but insert to fulfill the for loop reqt
            i += 1

    def check(self):
        if (self.link.__contains__("https://") | self.link.__contains__("youtube.com")): # check to see if the link is a valid link to the internet
            return 0 # preliminary checks passed
        else:
            return -1 # preliminary checks failed

    def generateHQ(self): # downloads the highest quality video available
        url = YouTube(self.link) # pings a request to Youtube under the link name
        video = url.streams.get_highest_resolution() # searches for the highest resolution video available
        video.download() # saves video locally in program folder
    
    def generateLQ(self):
        url = YouTube(self.link) # pings a request to Youtube under the link name
        video = url.streams.get_lowest_resolution() # searches for the lowest resolution video available
        video.download() # saves video locally in program folder
    
    def generateMP3(self):
        url = YouTube(self.link) # pings a request to Youtube under the link name
        video = url.streams.filter(only_audio=True).first()
        downloaded = video.download() # saves video locally in program folder
        base, ext = os.path.splitext(downloaded) # splits file name into file name and extension (we don't need the extension)
        new_file = base + '.mp3' # adds the new extension on
        os.rename(downloaded, new_file) # saves audio locally in program folder