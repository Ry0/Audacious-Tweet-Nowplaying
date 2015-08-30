#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import ConfigParser
import sys
import os
import codecs
from requests_oauthlib import OAuth1Session

config = ConfigParser.ConfigParser()
config.read(['/home/ry0/Workspace/Python/Audacious-Tweet-Nowplaying/aud-nowplaying.conf'])

# 自分で取得したTwitterの各種トークン
# Consumer Key
CONSUMER_KEY = config.get('connect_params', 'CONSUMER_KEY', 1)
# print CONSUMER_KEY

# Consumer Secret
CONSUMER_SECRET = config.get('connect_params', 'CONSUMER_SECRET', 1)
# print CONSUMER_SECRET

# Access Token
ACCESS_TOKEN_KEY = config.get('connect_params', 'ACCESS_TOKEN_KEY', 1)
# print ACCESS_TOKEN_KEY

# Accesss Token Secert
ACCESS_TOKEN_SECRET = config.get('connect_params', 'ACCESS_TOKEN_SECRET', 1)
# print ACCESS_TOKEN_SECRET

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# Audaciousからいま再生している楽曲データを取得
curr_song = subprocess.Popen(['audtool', 'current-song'], stdout=subprocess.PIPE)
curr_song = curr_song.stdout.read().rstrip()
print curr_song

# ハイフンで区切られているデータをばらばらに
strip_song = curr_song.split(" - ")

#アーティスト名
artist_name = strip_song[0]
# アルバム名にハイフンが入っているときがあるので対策
list_size = len(strip_song)
# アルバム名 ハイフンが入っていたと仮定して最後の要素を除いて再び合体
album_title = strip_song[1]
for i in range(list_size-3):
  album_title += " " + strip_song[i+2]
# 楽曲名
song_title = strip_song[list_size-1]

print "コメントを入力"
comment = raw_input('>>>  ')

# ツイートするフォーマットはここを編集
# 使える変数
# artist_name
# album_title
# song_title
status = "#nowplaying" + ' ' + song_title + ' - ' + artist_name

if len(comment) != 0:
  status = status + '\n' + comment

print status
params = {"status": status}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
  print ("OK")
else:
  print ("Error: %d" % req.status_code)
