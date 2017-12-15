# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'nowornever'

import requests
import re
import json
# 模拟浏览器去下载MP3
# print(response.content) # content 二进制数据
def getSong_byId(song_id):
    api_song = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery172045817479606786593_1513350397613&songid=%s&_=1513350399836' % song_id
    response = requests.get(api_song)
    # byte -> string
    data = response.content.decode(encoding='utf-8')
    data = re.findall(r'\((.*)\)', data, re.S) # re.S 可用来匹配换行符
    datadict = json.loads(data[0])
    song_title = ' '
    song_author = ''
    song_url = ''
    song_extension = ''
    try:
        song_title = datadict['songinfo']['title']
        song_author = datadict['songinfo']['author']
        song_url = datadict['bitrate']['show_link']
        song_extension = datadict['bitrate']['file_extension']
    except KeyError as e:
        print(e)
        return 0
    print(datadict)
    if song_url == '':
        song_url = datadict['bitrate']['file_link']
    # 持久化
    with open('%s-%s.%s' % (song_author, song_title, song_extension),'wb') as f:
        f.write(requests.get(song_url).content)

def getSongId_byAuthor(author):
    getSongId_url = 'http://music.baidu.com/search'
    param = {
        'key' : author
    }
    receivedData = requests.get(getSongId_url, params=param)
    data = receivedData.content.decode(encoding='utf-8')
    songids = re.findall(r'sid&quot;:(\d+)', data, re.S) # 正则提取，获取括号里的内容
    return songids

m_author = input('想要谁的歌:')
song_Ids = getSongId_byAuthor(m_author)
for song_id in song_Ids:
    getSong_byId(song_id)
