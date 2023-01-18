#!/usr/bin/env python3
import tempfile, sys
from pydub import AudioSegment

print("MP3toOGG, a script to convert MP3 to OGG powered by PyDub")

mp3file = input("Where to get the mp3 file from?")
oggfile = input("Where to output the ogg file?")
print("Converting file")
AudioSegment.from_mp3(mp3file).export(oggfile, format='ogg')

print("Done!")
sys.exit(0)
