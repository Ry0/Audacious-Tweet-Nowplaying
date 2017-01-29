#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import ConfigParser
import os
from requests_oauthlib import OAuth1Session
import lastfm

config = ConfigParser.ConfigParser()
python_script_path = os.path.abspath(os.path.dirname(__file__))
config.read([python_script_path + '/aud-nowplaying.conf'])

# 自分で取得したTwitterの各種トークン
# Consumer Key
TW_CK = config.get('twitter_params', 'consumer_key', 1)
# Consumer Secret
TW_CS = config.get('twitter_params', 'consumer_secret', 1)
# Access Token
TW_AT = config.get('twitter_params', 'access_token_key', 1)
# Accesss Token Secert
TW_AS = config.get('twitter_params', 'access_token_secret', 1)
# 自分で取得したLast.fmのAPI
# API Key
LF_AK = config.get('lastfm_params', 'api_key', 1)

# ツイート投稿用のURL
text_url = "https://api.twitter.com/1.1/statuses/update.json"
with_media_url = "https://api.twitter.com/1.1/statuses/update_with_media.json"

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

# OAuth認証で POST method で投稿
twitter = OAuth1Session(TW_CK, TW_CS, TW_AT, TW_AS)

# Last.fmでAlbumアート取得
cover = lastfm.AlbumArt(artist_name, album_title, LF_AK)
xml = cover.openUrl()
if xml:
  url = cover.getImageUrl(xml)
  if url:
    cover.saveImage(url)
    files = {"status":status, "media[]":open(python_script_path + "/.img/tmp.jpg", "rb")}
    print "[画像付き] " + status
    # req = twitter.post(with_media_url, files = files)
  else:
    params = {"status": status}
    print status
    # req = twitter.post(text_url, params = params)
else:
  params = {"status": status}
  print status
#   req = twitter.post(text_url, params = params)

# # レスポンスを確認
# if req.status_code == 200:
#   print ("OK")
# else:
#   print ("Error: %d" % req.status_code)