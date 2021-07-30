#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:01:37 2021

@author: hunglin
"""

import hashlib
import json
from pathlib import Path

def compute_md5(file):
    with open(file, "rb") as f:
        buf = f.read()
    m = hashlib.md5(buf)
    return m.hexdigest()

def md5_to_file(dir_path:Path):
    md5_to_file_d = {}
    for file in dir_path.iterdir():
        if file.name.endswith(".mp3"):
            md5_to_file_d[compute_md5(file)] = file
    return md5_to_file_d
    
def check_file_by_md5(dir_path):
    dir_path = Path(dir_path)
    val_f = dir_path / f".{dir_path.name}.json"
    if val_f.is_file():
        val_d = json.loads(val_f.read_bytes())
    else:
        val_d = {}
    val_d_reverse = dict([ (v, k) for k, v in val_d.items()])
    md5_to_file_d = md5_to_file(dir_path)
    # local_md5_ls = [compute_md5(file) for file in dir_path.iterdir() if file.name.endswith(".mp3")]

    for md5_v, file in md5_to_file_d.items():
        if md5_v not in val_d.values():
            # print(f"remove {file}")
            file.unlink(missing_ok=True)
            
    lack_ls = set(val_d.values()) - set(md5_to_file_d)
    for md5_v in lack_ls:
        del val_d[val_d_reverse[md5_v]]
    val_f.write_text(json.dumps(val_d))
    return 0


        