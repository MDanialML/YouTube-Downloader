#this block of code is used to download youtube playlist
#code from 
'''from pytube import Playlist
url = 'https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x'
pl = Playlist(url)
print(pl.title)'''
# this block of code is used to download a single youtube video 
'''from pytube import YouTube
link='https://www.youtube.com/shorts/xCzEoQlspqk'
youtube_1 = YouTube(link)
#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
#videos = youtube_1.streams.all()
videos = youtube_1.streams.filter(only_video=True)
vid = list(enumerate(videos))
for i in vid:
    print(i) 
print()
strm = int(input("Enter index number : "))
videos[strm].download()
print("Successful")'''


'''
print("========* Python Youtube downloader *========")
print("Kindly go to YouTube and copy the link of The video you want to download...!")

import moviepy.editor as mpe
import os
from pytube import YouTube
from threading import *

vname = "clip.mp4"
aname = "audio.mp3"
url = input("Enter Target URL : ")

# Download video and rename
def download_video():
    get_link = YouTube(url)
    print(get_link.title)
    video_stream = get_link.streams.filter(only_video=True)
    l_vid = list(video_stream)
    for i in range(len(l_vid)):
        print(i,l_vid[i])
    str_no = int(input('Enter stream Num  : '))
    print('Downloading the target stream',l_vid[str_no])
    video=l_vid[str_no].download()
    print('Download Successful...!')
    print('Now renaming the downloaded video..')
    os.rename(video, vname)
    #video_stream.first().download()

# Download audio and rename
def download_audio():
    audio = YouTube(url)
    audio_str = audio.streams.filter(only_audio=True)
    str_l = list(audio_str)
    for x in range(len(str_l)):
        print(x,str_l[x])
    str_n = int(input('Enter stream No : '))
    print('Now downloading :',str_l[str_n])
    str_l[str_n].download()
    os.rename(audio, aname)

#function call
vd_thread = Thread(target=download_video)
ad_thread = Thread(target=download_audio)
vd_thread.start()
ad_thread.start()
vd_thread.join()
ad_thread.join()


# Setting the audio to the video
print('Now rendering audio and video')
video = mpe.VideoFileClip(vname)
audio = mpe.AudioFileClip(aname)
final = video.set_audio(audio)

# Output result
final.write_videofile("video.mp4")

# Delete video and audio to keep the result
os.remove(vname)
os.remove(aname)'''

#clean code for downlaoding audio and video separatly then merge them to get a video with audio

#Importing requaired libs
from pytube import YouTube #for downloadin audio and video
import moviepy.editor as medit #for merging
import os #for renaming the downloaded file
print("========* Python Youtube downloader *========")
print("Copy Target URL and paste it down below!")

#Declaring the global variable to get url and setting the video and audio file name
url = input('Enter Target URL : ')
v_name = 'Clip.mp4'
a_name = 'Clip.mp3'

#Downloading the target video
load_video_url = YouTube(url)
#print the Title of loaded Video
print(load_video_url.title)
get_vstream = load_video_url.streams.filter(only_video = True)
stream_itr = list(enumerate(get_vstream))
for vs in stream_itr:
    print(vs)
stream_n = int(input('Enter target stream number : '))
video =get_vstream[stream_n].download() #downloading and storing video to video variable
print('Video download complete')
os.rename(video,v_name)


#Downloading the target audio
load_audio_url = YouTube(url)
get_astream = load_audio_url.streams.filter(only_audio=True)
audio_str_itr = list(enumerate(get_astream))
for a in audio_str_itr:
    print(a)
audio_str_n = int(input('Enter audio Stream No : '))
audio= get_astream[audio_str_n].download()
print('Audio download complete')
#os.name(audio,a_name)

#now setting audio to video
final_video = medit.VideoFileClip(v_name)
final_audio = medit.AudioFileClip(audio)
final = final_video.set_audio(final_audio)

#output the final video
final.write_videofile('finalVideo.mp4')

# Delete video and audio to keep the result
os.remove(v_name)
#os.remove(a_name)