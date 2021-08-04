#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 07:17:55 2021

@author: hunglin
"""
import os
import sys
import subprocess
from pathlib import Path
import wget
import zipfile
root_dir = Path(__file__).parent
# install python packages
subprocess.call(["pip", "install", "-r", root_dir/"requirements.txt"])

# install ffmpeg
lib_dir = root_dir / "lib"
os_dir = lib_dir / sys.platform
os_dir.mkdir(exist_ok=True, parents=True)
os.chdir(os_dir)

if sys.platform == "linux":
    link = "https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz"
    if not (os_dir/"ffmpeg/ffmpeg").is_file():
        os.system(f"wget -qcO- {os_dir/Path(link).name} {link} | tar -Jxf -")

elif sys.platform == "win32":
    link = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    if not (os_dir/"ffmpeg/bin/ffmpeg").is_file():
        zip_file = wget.download(url=link, out=str(os_dir/Path(link).name))
        
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(os_dir)
        os.remove(zip_file)
                   
for file in os_dir.iterdir():
    if file.is_dir() and file.name.startswith("ffmpeg"):
        file.rename(os_dir/"ffmpeg")
print("Setup finished.")
