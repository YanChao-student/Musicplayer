import cloudmusic
from tkinter import *
from tkinter.messagebox import *
import time
import re
import urllib.request


class homePage(Frame):
    def searchSingle(self,musciname):
        ly = musciname
        results = cloudmusic.search(ly,10)
        if results == []:
            print("kong")
        else:
            print("已搜索到歌曲")
        f1 = open('Lyrics.csv','w',encoding='utf-8')
        # print(results[0].getLyrics())
        for lyrics in results[0].getLyrics():
            f1.write(lyrics)
        f2 = open('Names.csv','w',encoding='utf-8')
        for name in results:
            f2.write(name.name+'\n')
        f1.close()
        f2.close()
    # def Names(self):
    #     f = open('Lyrics.csv', 'r', encoding='utf-8')
    #     name = f.readlines()
    #     creatPage()
    #     f.close()
    #     print("歌词显示区")
    #     return name


    # def Name(self,name):
    #     self.w1.insert(1.0, name+'\n') # 在第１行第０列插入,把text插入到列表之中

    # def Lyrics(self,lyrics,order):
    #     if order == 'single':
    #         for i in lyrics:
    #             self.w3.insert(1.0, i + '\n')
    #     else:
    #         for i in lyrics:
    #             self.w2.insert(1.0,i+'\n')
