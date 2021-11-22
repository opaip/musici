import requests
import youtube_dl
import os
def spotify():
    os.system('cls')
    while True:
        inputt = input('Enter you song name :>> ')
        if inputt=='/exit':
            break
        link = requests.get(f'https://api.otherapi.tk/music?platform=spotify&type=search&query='+inputt).json()
        try:
            print(link['music'][0]['download'])
        except:
            print('song name is unavailable in database')
                                    
        print('for exit enter /exit')
        inn = input('>>')
        if inn=='/exit':
            break
def youtube():
    os.system('cls')
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
}
    name = input('music name :>> ')
    result = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?q={name}&maxResults=1&key=AIzaSyAOw0wToDhyqx693bhLEkIk2TY4g8ec4n8').json()
    data = result
    data = data['items'][0]['id']['videoId']
    url = f'https://youtube.com/watch?v={data}'
    print(f'link : {url}')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print('successfully downloaded')
        except:
            print('downloadind faild try vpn')
        input('Enter for bcak to menu >>' )
    
while True:
    os.system('cls')
    plat = input('select your platform : [1]spotify  [2]youtube >> ')
    if plat == '1':
        spotify()
    else:
        youtube()
    

    
