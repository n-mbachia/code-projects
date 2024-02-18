#!/usr/bin/python3

"""This code was adopeted from python coding YouTube page day 73..."""

from moviepy.editor import VideoFileclip

video_clip = VideoFileClip("Binod.mp4")

video_clip.write_gif("Binod.gif")
