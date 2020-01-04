import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

result = ydl.extract_info(
    'https://www.youtube.com/watch?v=4p_aQwIedN4',
    download=False
)

if 'entries' in result:
    video = result['entries'][0]
else:
    video = result


def download():
    for format in video['formats']:
        if format['acodec'] != 'none':
            print(format['format_note'])
            print(format['url'])
            print(format)
            print('\n******************************************************\n')
        pass
    pass

def tag():
    print(video['id'])
    print(video['uploader'])
    print(video['title'])
    print(video['duration'])
    print(video['thumbnail'])
    pass

tag()
download()
