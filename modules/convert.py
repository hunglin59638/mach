#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 07:40:03 2021

@author: hunglin
"""
from pathlib import Path
from pydub import AudioSegment

def convert_webm2mp3(webm_file:Path) -> Path:
    mp3_file = webm_file.parent / f'{webm_file.stem}.mp3'
    AudioSegment.from_file(webm_file).export(mp3_file, format="mp3")
    if Path(mp3_file).is_file():
        Path(webm_file).unlink()
        return mp3_file