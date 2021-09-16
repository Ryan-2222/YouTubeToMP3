import youtube_dl
import webbrowser
from YT2MP3 import *
import json

index = 0

with open("config.json", "r") as f:
    link = json.load(f)
    # print(link["link"][0])
    len_array = len(link["link"])
    # print(len_array)

while True:
    try:
        url_full = link["link"][index]
        url = url_full[url_full.find("=") + 1 : url_full.find("=") + 12]

        print(url_full)

        cover_get(url)
        YT2MP3(url)
        Info_edit()

        del link["link"][index]
        link["album_num"] += 1

        with open("config.json", "w") as f:
            json.dump(link, f)

    except IndexError:
        print("Finished! PLease check!")
        break

    except:
        print("Oops! It seems the URL went wrong!")
        print("Please go config.json and check the Wrong URL")
        print()

        index += 1
        continue

#(ValueError, urllib.error.HTTPError, youtube_dl.utils.DownloadError)
