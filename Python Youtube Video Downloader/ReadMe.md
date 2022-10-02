# Youtube Video Downloader
This is a python script that creates a GUI window to allow the user to download Youtube videos. Downloads are stored in the program folder.

## Program.py
This is where the program should be run from, doesn't require any arguments, creates a default window size of 500x500 pixels.

## GUI.py
This is the user interface for the program, once called by Program.py it will create a window that presents the user with a place to insert a link for a Youtube video to turn into a HQ video, LQ video, or a MP3. The window is resizeable.

## YTVideoDownloader.py
This is the backend for the GUI that makes the download process functional. This uses pytube and some os functions to provide the ability to download videos from the internet (requires internet access), manipulate filetypes, and download relevant information for the desired outcome. Provides functionality for the Highest Quality video available (HQMP4), the Lowest Quality video available (LQMP4), and mp3 downloads from the link that the GUI is provided with.