#YouTube to MP3 Convector

##Features
- Support batch download
- Auto add cover image for MP3
- I know those features are bullshit bruh

##Download

- `git clone https://github.com/Ryan-2222/YouTubeToMP3.git` to install **or**
-    Download directly from the web

##RUN
- Download all libraries mentioned in `requirement.txt` e.g `pip install`
- Copy and paste the YouTube link into `config.json`, e.g.`"link":["here", "here2"]`. 
- terminal / cmd: `py main.py`

##Be Careful
- Please make sure that you have created a folder named "Music".
- Please make sure that you have downloaded all libraries.
- Don't make any changes in `config.json` `album_num` part.

##Something you might need to pay attention to 
- The library `pafy` that I used has a bug, you may need to change lines 53 and 54 of file `backend_youtube_dl.py`
- line 53: `self._likes = self._ydl_info.get('like_count',0)`
- line 54: `self._dislikes = self._ydl_info.get('dislike_count',0)`
- Reference: https://github.com/mps-youtube/pafy/pull/288

##Others
- Don't worry if you type the wrong link. Terminal will remind you :)
- All MP3 files will be saved into the `Music` folder
- If the converter can't handle converting to MP3, it will automatically send you to that MP3 download link.