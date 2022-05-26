#! /usr/bin/env python3
# coding: utf-8
 
import shlex
import subprocess
import os
import threading


BASE_URL_vYT = "https://www.youtube.com/watch?v="

files = [file for file in os.listdir('.') if os.path.isfile(file)]

url_list = []



for file in files:
    

    if file[-5:] == ".part":
        
        target = file[-20:-9]
        fulltarget = BASE_URL_vYT + target
        print(f" ... cutted filed found  => {file}")
        print(f"    ->    {fulltarget}   \n\n")
        url_list.append(fulltarget)


for url in url_list:
    proc = subprocess.Popen(shlex.split(f"youtube-dl -f 18 {url}"))
    print(f"Downloading {repr(url)} start. (PID={proc.pid})")



