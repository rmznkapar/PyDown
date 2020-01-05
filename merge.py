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

my_clip = mpe.VideoFileClip('resd.mp4')
my_clip.write_videofile("resd.mp4", audio=True)
