#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Convert all WMA files from given folder to MP3."""

import os
import sys

LOG_LEVEL = 'fatal'

if len(sys.argv) != 2:
    sys.exit('Missing input path!')

path = sys.argv[1]

if not os.path.isdir(path):
    sys.exit('Incorrect input path!')

items = os.listdir(path)

for i in items:
    if i.endswith('.wma'):
        print(i)
        file_base_name = i[:-4]
        file_wma = os.path.join(path, '%s.wma' % file_base_name)
        file_mp3 = os.path.join(path, '%s.mp3' % file_base_name)
        os.system('ffmpeg -loglevel %s -i \"%s\" -acodec mp3 \"%s\"' % (LOG_LEVEL, file_wma, file_mp3))
