# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:38:01 2020

@author: JAIRI IDRISS
"""

import youtube_dl


def download_video(video): 
    video = video.strip() 
    ydl = youtube_dl.YoutubeDL() 
    try:
        ydl.download([video])
    except:
        print("Invalid URL!")
        



link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") 
video = link_of_the_video.strip() 
  
download_video(video) 