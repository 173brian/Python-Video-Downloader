from tkinter import*
from pytube import YouTube
import tkinter as tk
from YTVideoDownloader import*

class GUI:
    # This method handles the initialization of the GUI window
    def __init__(self, geoX, geoY):
        windowGeoX = geoX   # Local variables for the window size
        windowGeoY = geoY
        self.windowFontLarge = 'san-serif 18 bold' #local fonts to be used by the program
        self.windowFont = 'san-serif 14 bold'
        self.windowFontSmall = 'san-serif 8'
        self.mainWindow = Tk() # initialization of the window
        self.wGEOTkValX = tk.StringVar() # the variables that will show the size of the window when created, StringVar enables the program to be dynamically updated
        self.wGEOTkValY = tk.StringVar()
        self.mainWindow.resizable(True,True) # functionality to resize the window
        self.mainWindow.geometry(f'{windowGeoX}x{windowGeoY}') # shows what the window size is
        self.mainWindow.update_idletasks() # forces the window to refresh and check it's attributes
        print(self.mainWindow.winfo_width()) # debut information that shows that the window was created according to the input size
        print(self.mainWindow.winfo_height())
        self.mainWindow.title('Youtube to MP4/MP3 Converter') # Window title
        self.windowGeoX = self.mainWindow.winfo_width() # Double check to make sure that the local variables and attributes line up
        self.windowGeoY = self.mainWindow.winfo_height()
        self.wGEOTkValX.set(windowGeoX) # sets global values to the double checked variables
        self.wGEOTkValY.set(windowGeoY)
        self.link = tk.StringVar() # creates an instance of a stringvar that can be used for our video link

    def createWidgets(self):
        Label(self.mainWindow, text="Youtube Video Downloader", font=self.windowFontLarge).pack(side=TOP) # main title widget
        self.wSize = Label(self.mainWindow, text=f'windowSize=({self.windowGeoX}x{self.windowGeoY})', font=self.windowFontSmall).pack(side=BOTTOM) # widget detailing window size
        Label(self.mainWindow, text="Paste your link here", font=self.windowFont).pack(side=TOP) # paste link title widget
        Label(self.mainWindow, text="", font=self.windowFont).pack(side=TOP) # empty line for spacing
        Label(self.mainWindow, text="\n\n\n\n\n", font=self.windowFont).pack(side=TOP) # another way to do empty lines I was playing around with, 5 empty lines added

        Entry(self.mainWindow, width=70, textvariable=self.link).pack(side=TOP) # The link entry widget for the user

        Button(self.mainWindow, text='MP4HQ', font=self.windowFont, bg='red', command=self.tempHelpHQ).pack(ipadx=4, ipady = 10, fill=tk.X, expand=True, side=LEFT) # HQ widget
        Button(self.mainWindow, text='MP4LQ', font=self.windowFont, bg='red', command=self.tempHelpLQ).pack(ipadx=4, ipady = 10, fill=tk.X, expand=True, side=LEFT) # LQ widget
        Button(self.mainWindow, text='MP3', font=self.windowFont, bg='blue', command=self.downloadMP3).pack(ipadx=4, ipady = 10, fill=tk.X, expand=True, side=RIGHT) # MP3 Widget

    def mp4HelperMethod(self, link): # A helper method for downloading MP4s (Debug info)
        download = YTVideoDownloader(link) # Creates YT object with url link
        if (download.check() == 0): # Preliminary link check
            message = YTVideoDownloader(link).generate() # Feedback from downloading video
            Label(self.mainWindow, text=message, font=self.windowFont).pack(side=BOTTOM) # Updates with link

    def updater(self, window, textInContainer): # A method to help with the window updates I referenced in my video, enables resizing info to keep button placements even
        sizeX = window.winfo_width() # Size variables
        sizeY = window.winfo_height()
        print(f"size:({sizeX}, {sizeY}), link:{textInContainer}") # Debug info for size variables
        self.wGEOTkValX.set(sizeX) # Updates global variables
        self.wGEOTkValY.set(sizeY)

    def tempHelpHQ(self): # Download method for the HQ video
        textInContainer = self.link.get() # gets the url for the new class
        self.updater(self.mainWindow, textInContainer) # calls helper method
        video = YTVideoDownloader(textInContainer) # new video class
        if (video.check() == 0): # preliminary checks 
            video.generateHQ() # calls HQ video download method

    def tempHelpLQ(self): # Download method for the LQ video
        textInContainer = self.link.get() # Checks url
        self.updater(self.mainWindow, textInContainer) # calls helper method
        video = YTVideoDownloader(textInContainer) # new video class
        if (video.check() == 0): # preliminary checks
            video.generateLQ() # calls LQ video download method

    def loadWindow(self): # Main loop
        self.mainWindow.mainloop()

    def downloadMP3(self): # Download method for MP3s
        textInContainer = self.link.get() # checks url
        self.updater(self.mainWindow, textInContainer) # calls helper method
        video = YTVideoDownloader(textInContainer) # new video class
        if (video.check() == 0): # preliminary checks
            video.generateMP3() # calls MP3 Download method