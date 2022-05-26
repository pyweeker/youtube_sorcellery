#! /usr/bin/env python3
# coding: utf-8
 
import shlex
import subprocess
import os
import threading
 

QUALITY_FORMAT = "18"

print(f" \n \n       ___    QUALITY_FORMAT  is  {QUALITY_FORMAT}    ___    \n \n ")

url_list = []

print("\n     press Enter key if no more videos to DL")


i = 1
x = None

while x != '':
    x=input("\n  please give video URL  n° " + str(i) + "  to DL :  ")
    print("\n")
    url_list.append(x)
    i += 1




for url in url_list:
    proc = subprocess.Popen(shlex.split(f"youtube-dl -f {QUALITY_FORMAT} {url}"))
    print(f"Downloading {repr(url)} start. (PID={proc.pid})")


