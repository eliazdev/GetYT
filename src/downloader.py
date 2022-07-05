#Downloader Class
from __future__ import unicode_literals
import yt_dlp
import requests
import PyQt5.QtWidgets
import PyQt5.QtCore
import threading
import messagebox
class Downloader:
    def __init__(self, urls : list, dest : str, ui):
        self.urls = tuple(urls)
        self.dest = dest
        self.ui = ui
    def download_all(self):
        th = threading.Thread(target=self.run)
        th.start()
    def run(self):
        opts = {'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'}
        opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'outtmpl': self.dest + '/%(title)s.%(ext)s', 'quiet' : True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(self.urls)
        messagebox.info("Success", "Downloads Finished!").exec_()

class getInfo:
    def __init__(self, url):
        self.url = url
    def checkURL(self):
        r = requests.get(self.url)
        if "Video unavailable" in r.text:
            return False
        else:
            return True