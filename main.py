import youtube_dl
from tkinter import *


class Downloader:
    video = ''
    tags = {}
    urls = []

    def __init__(self, user_link):
        self.user_link = user_link

    def list(self):
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        result = ydl.extract_info(
            user_link,
            download=False
        )
        self.video = result
    def tagger(self):
        self.tags.update({
            'id': self.video['id'],
            'uploader': self.video['uploader'],
            'title': self.video['title'],
            'duration': self.video['duration'],
            'thumbnail': self.video['thumbnail']
        })
        pass
    def urler(self):
        for url in self.video['formats'] :
            if url['filesize'] != 'none':
                self.urls.append({
                    'format': url['format_note'],
                    'ext': url['ext'],
                    'filesize': str( url['filesize']*(10**-6) ),
                    'url': url['url']
                })
                pass
            pass
        pass






window = Tk()

window.title("PyDown")

window.geometry('400x200')

lbl = Label(window, text="YouTube Link")
lbl.grid(column=0, row=0, padx=5, pady=5)
txt = Entry(window,width=50)
txt.grid(column=0, row=1, padx=5, pady=5)

def clicked():
    urlink = Downloader( txt.get() )
    urlink.ydler()

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=1, pady=5)
window.mainloop()
