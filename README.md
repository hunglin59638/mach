# Mach: Donwload music from Youtube playlist automatically
## Introduction
Inupt youtube playlist url and download all of music in the playlist.

## Requirements
Mach is nornally is normally distributed as a dependency-free binary for Linux and Win10.
### Software requirements
- [ffmpeg](https://www.ffmpeg.org/)
### Python packages
- youtube-dl
- pydub
- tqdm

## Installation

+ git 
```
git clone https://github.com/hunglin59638/mach.git
cd mach
./setup.py
./mach -h
```

## Usage
```
./mach --playlist_url https://www.youtube.com/playlist?list=PLDBEBMxJMdKQj_ZmISBdeJq0UyB1dZ5X2 --out_dir $HOME/Music
```