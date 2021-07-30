#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:47:57 2021

@author: hunglin
"""
import os
import re
import json
from tqdm import tqdm
# from pytube import YouTube, Playlist
import youtube_dl
from pathlib import Path
from validate import compute_md5, check_file_by_md5
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet':True
}
ydl = youtube_dl.YoutubeDL(ydl_opts)

# url = "https://www.youtube.com/playlist?list=PLDBEBMxJMdKQR4hxCr0b2sybEOgp_f3T1"
# os.chdir("/home/hunglin/Music")


def get_playlist_info(url:str):
    pl_info = ydl.extract_info(url, download=False)
    return pl_info

def extract_vedio_url(pl_info):
    url_ids = []
    for v_info in pl_info.get("entries"):
        url_ids.append(v_info["id"])
    return url_ids

def download_music(url_id:str, out_dir:Path) -> Path:
    os.chdir(out_dir)
    if not ydl.download([f"https://www.youtube.com/watch?v={url_id}"]):
        for file in out_dir.iterdir():
            if file.stem.endswith(url_id):
                file = file.rename(file.parent/re.sub(rf'-{url_id}', '', file.name))
                return file

def main():
    url = "https://www.youtube.com/playlist?list=PLDBEBMxJMdKQj_ZmISBdeJq0UyB1dZ5X2"
    out_dir = Path("/home/hunglin/Music")
    
    pl_info = get_playlist_info(url)
    pl_title = pl_info.get('title')
    pl_dir = out_dir / pl_title
    pl_dir.mkdir(exist_ok=True)
    os.chdir(pl_dir)

    info_f = pl_dir / f".{pl_title}.json"
    if not info_f.is_file():
        info_f.write_text(json.dumps({}))
        
    check_file_by_md5(dir_path=pl_dir)
    info_d = json.loads(info_f.read_bytes())
    
    url_ids = extract_vedio_url(pl_info)
    pbar = tqdm(total=len(url_ids), desc=f"Download music in {pl_title} playlist")
    for url_id in url_ids:
        if url_id not in info_d:
            file = download_music(url_id, pl_dir)
            if file:
                md5_v = compute_md5(file)
                info_d[url_id] = md5_v
        pbar.update(1)
    pbar.close()
                
    info_f.write_text(json.dumps(info_d))
                
        
    

# out_dir = Path("/home/hunglin/Music")

# url = "https://www.youtube.com/playlist?list=PLDBEBMxJMdKQR4hxCr0b2sybEOgp_f3T1"

# playlist = Playlist(url)
# playlist_title = playlist.title
# videos = [x for x in playlist.video_urls]

# for video in videos:
#     yt = YouTube(video)
#     # yt.streams.filter(type="audio").first().download(output_path=out_dir/)
#     break