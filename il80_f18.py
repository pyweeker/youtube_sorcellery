#! /usr/bin/env python3
# coding: utf-8
 
import shlex
import subprocess
import os
import threading

import time


QUALITY_FORMAT = "18"

print(f" \n \n       ___    QUALITY_FORMAT  is  {QUALITY_FORMAT}    ___    \n \n ")


playlist_URL = input(" \n\n\n ==>>>  playlist_URL ")


cmd = f"youtube-dl -F {playlist_URL}"



with open('report.txt', 'w') as output_file:
    subprocess.check_call(shlex.split(cmd), stdout=output_file)
time.sleep( 5 )


import re

filename = "report.txt"

accepted_heads = {"[youtube:tab]","[download]","[youtube]","[info]"}




target_start = "[info] Available formats for "
len_target_start = len(target_start)

print(f"  len(target_start)   {len(target_start)} ")
print("=========================================")



#counterpattern = "[download] Downloading video" one void space
counterpattern = "[download] Downloading video "

targetpattern_end = ": Downloading webpage"
crophead = "[youtube] "

maxvideo_startpattern  = "[youtube:tab] playlist "


alllines =[]

targets = []

counterlines = []

curatedlines = []

biglist = []

#with open(filename, 'rb') as reportfile:
with open(filename, 'r') as reportfile:
        for line in reportfile:

            

            line = line.rstrip()
            line = line[:-1]

            alllines.append(line)

            for accepted_head in accepted_heads:
                if line.startswith(accepted_head):
                    curatedlines.append(line)


            if line.startswith(maxvideo_startpattern):
                counterlines.append(line)

            



print(counterlines)

print("\n\n\n")

for curline in curatedlines:
    print(curline)
    if curline.startswith(target_start):
        print(f" \n   >>>>>>>>>>>>>>>>> {curline}             type(curline)  {type(curline)}          len(curline)   {len(curline)}         {curline[len_target_start:]}   \n")

        target_url_string = curline[len_target_start:]

        targets.append(target_url_string)


time.sleep( 2 )


print(f"targets {targets}    type  {type(targets)}")


for target_url in targets:


    print(f"...target_url {target_url}    type  {type(target_url)}")

    target_url.rstrip()

    print(f"___target_url {target_url}    type  {type(target_url)}")



    proc = subprocess.Popen(shlex.split(f"youtube-dl -f {QUALITY_FORMAT} {target_url}"))
    print(f"Downloading {repr(target_url)} start. (PID={proc.pid})")

print(f"targets {targets}    type  {type(targets)}")


