#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 07:40:03 2021

@author: hunglin
"""
import os
import sys
from pathlib import Path
import subprocess
from pydub import AudioSegment
myos = sys.platform
ffmpeg_path = Path(__file__).parent.parent/ "lib"
if myos == "linux":
    ffmpeg_path = ffmpeg_path / f"{myos}/ffmpeg"
elif myos == "win32":
    ffmpeg_path = ffmpeg_path / f"{myos}/ffmpeg/bin"
os.environ["PATH"] += os.pathsep + str(ffmpeg_path)

def convert_webm2mp3(webm_file:Path) -> Path:
    mp3_file = webm_file.parent / f'{webm_file.stem}.mp3'
    if sys.platform == "linux":
        AudioSegment.from_file(webm_file).export(mp3_file, format="mp3")
    else:
        cmd = [ffmpeg_path/"ffmpeg.exe", "-i", webm_file, "-vn", mp3_file]
        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
    
    if Path(mp3_file).is_file():
        Path(webm_file).unlink()
        return mp3_file