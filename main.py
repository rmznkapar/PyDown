import io
import youtube_dl
from tkinter import *
from PIL import ImageTk,Image
from urllib.request import urlopen
import urllib.request
from time import gmtime
from time import strftime
import subprocess
import moviepy.editor as mpe

class Downloader:
    video = ''
    tags = {}
    urls = []

    def __init__(self, user_link):
        self.user_link = user_link

    def list(self):
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        result = ydl.extract_info(
            self.user_link,
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
        return self.tags
        pass

    def urler(self):
        for url in self.video['formats'] :
            if url['filesize'] != 'none':
                self.urls.append({
                    'format': url['format_note'],
                    'ext': url['ext'],
                    'filesize': str( round( url['filesize']*(10**-6), 2 ) ),
                    'url': url['url']
                })
                pass
            pass
        return self.urls
        pass


window = Tk()

window.title("PyDown")

window.geometry('400x300')

lbl = Label(window, text="YouTube Link")
lbl.grid(column=0, row=0, padx=5, pady=5)
txt = Entry(window,width=50)
txt.grid(column=0, row=1, padx=5, pady=5)

def clicked():
    urlink = Downloader( txt.get() )
    #cagrilmasi zorunlu
    urlink.list()
    listbox = Listbox(window, width=50)

    for n, xec in enumerate( urlink.urler() ):
        if xec['format'] == 'tiny':
            list_text = 'audio ' + xec['ext'] + ' (' + xec['filesize'] + 'mb)'
        else:
            list_text =  xec['format'] + ' ' + xec['ext'] + ' (' + xec['filesize'] + 'mb)'
        listbox.insert( n+1, list_text )
        pass

    listbox.grid(column=0, row=2, pady=5, padx=5)

    raw_data = urlopen(urlink.tagger()['thumbnail']).read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((95, 55), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    imgframe = Label(window, image=image)
    imgframe.image = image
    imgframe.grid(column=0,row=3, sticky=W,padx=5)

    inf = Label(window, text=urlink.tagger()['title'][:45]+'\n ('+strftime("%H:%M:%S", gmtime(urlink.tagger()['duration']))+')' )
    inf.grid(column=0,columnspan=2, row=3, padx=(60,0), pady=5)

    audio_link = urlink.urler()[1]['url'] if urlink.urler()[1]['format'] == 'tiny' else urlink.urler()[0]['url']
    dwn_btn = Button(window, text="Download", command=lambda: download( urlink.urler()[listbox.curselection()[0]]['url'], urlink.urler()[listbox.curselection()[0]]['format'], urlink.tagger()['title'], audio_link ))
    dwn_btn.grid(column=1, row=2, pady=5)

def merge(link, type, title):
    my_clip = mpe.VideoFileClip('resd.mp4')
    my_clip.write_videofile("resd.mp4", audio="resd.mp3", codec='mpeg4')
    pass

def download(link, type, title, audio):
    print(audio)
    if type != 'tiny':
        print('video indiriliyor')
        urllib.request.urlretrieve(link, 'resd.mp4')
        print('indirme islemi tamamlandi')
        print('indiriliyor')
        urllib.request.urlretrieve(audio, 'resd.mp3')
        print('indirme islemi tamamlandi')
        merge(link, type, title)
    else:
        print('indiriliyor')
        urllib.request.urlretrieve(link, title + '.mp3')
        print('indirme islemi tamamlandi')

src_btn = Button(window, text="Search", command=clicked)
src_btn.grid(column=1, row=1, pady=5)
























window.mainloop()
