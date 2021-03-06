import time

import pafy
from moviepy.editor import *
import os
import shutil
import eyed3
import random
import json
import urllib.request
import re

video_name = ""

def YT2MP3(url):
    video = pafy.new("https://www.youtube.com/watch?v=" + url)
    bestvid = video.getbest(preftype="mp4")
    bestvid.download(quiet = False)

    global video_name
    video_name = video.title

    video_name = re.sub(r'[\\/*?:"<>|]', "_", video_name)
    video1 = VideoFileClip(video_name + '.mp4')
    video1.audio.write_audiofile(video_name + '.mp3')
    video1.close() #No use for mac

    time.sleep(1)

    try:
        shutil.move(video_name + ".mp4", "Music")
        shutil.move(video_name + ".mp3", "Music")
        os.remove("Music/" + video_name + ".mp4")
    except (shutil.Error, FileNotFoundError):
        try:
            os.remove(video_name + ".mp4")
        except:
            pass
        try:
            os.remove(video_name + ".mp3")
        except:
            pass
        try:
            os.remove("Music/" + video_name + ".mp4")
        except:
            pass



def Info_edit():
    global video_name
    audiofile = eyed3.load("Music/" + video_name + '.mp3')
    if (audiofile.tag == None):
        audiofile.initTag()

    with open("config.json", "r") as f:
        album = json.load(f)
        album_num = str(album["album_num"])

        # audiofile.tag.album = str(random.randint(522, 99999999999))
        audiofile.tag.album = album_num
        audiofile.tag.images.set(3, open('cover.jpg', 'rb').read(), 'image/jpeg')

        audiofile.tag.save()

def cover_get(url):
    while True:
        try:
            urllib.request.urlretrieve("https://img.youtube.com/vi/" + url + "/maxresdefault.jpg", "cover.jpg")
            break
        except urllib.error.HTTPError:
            pass

            try:
                urllib.request.urlretrieve("https://img.youtube.com/vi/" + url + "/sddefault.jpgt.jpg", "cover.jpg")
                break
            except urllib.error.HTTPError:
                pass

                try:
                    urllib.request.urlretrieve("https://i3.ytimg.com/vi/" + url + "/hqdefault.jpg", "cover.jpg")
                    break
                except urllib.error.HTTPError:
                    pass

                    try:
                        urllib.request.urlretrieve("https://img.youtube.com/vi/" + url + "/mqdefault.jpg", "cover.jpg")
                        break
                    except urllib.error.HTTPError:
                        pass

                        try:
                            urllib.request.urlretrieve("https://img.youtube.com/vi/" + url + "/default.jpg", "cover.jpg")
                            break
                        except:
                            break

                            
