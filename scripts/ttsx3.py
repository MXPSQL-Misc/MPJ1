#!/usr/bin/env python3
import pyttsx3, sys


print("TTSX3: Python Text synthesis script powered by pyttsx3")
print(f"Script is located on {__file__}")

print("Starting speech synthesis")
engine = pyttsx3.init()
engine.save_to_file(input("What do you want to say for pyttsx3? "), input("Where to save that file? "))
print("Generating speech with pyttsx3")
engine.runAndWait()
print("Done synthesizing and generating speech")

sys.exit(0)

