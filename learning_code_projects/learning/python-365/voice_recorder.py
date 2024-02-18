#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 44..."""

import sounddevice #pip3 install sounddevice
from scipy.io.wavfile import write #pip3 install scipy

fs=440 # sample_rate

# Prompt user to specify recording time
second = int(input("Enter recording time in seconds: ")) 
print("Recording .....\n")
record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)
sounddevice.wait()
write("MyRecording.wav",fs,record_voice)
print("Recording is done please check your folder to listen recording")
