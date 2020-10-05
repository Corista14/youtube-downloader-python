from pytube import YouTube

userURL = input('Insert here the YouTube video link: ')

yt = YouTube(userURL)
userFileName = input('Name your file: ')
userFileLocation = input('Paste the location that you want to save it: ')
askForOnlyAudio = input('Do you want just the audio? (Y/N)').upper()

def download(audio):
    yt.streams.filter(only_audio=audio).first().download(output_path=userFileLocation, filename=userFileName)
    input()

def downloadAudio():
    download(audio=True)

def downloadVideo():
    download(audio=False)
    

if askForOnlyAudio == 'Y':
    downloadAudio()
else:
    downloadVideo()




