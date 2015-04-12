#!/usr/bin/env python
#coding utf-8
import os, subprocess, ConfigParser, sys
from requests_oauthlib import OAuth1Session

# 自分で取得したTwitterの各種トークン
CK = 'abcdefghijklmnopqrstuvwxy'                                  # Consumer Key
CS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx'         # Consumer Secret
AT = '123456789-ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNO'         # Access Token
AS = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrst'              # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# Audaciousからいま再生している楽曲データを取得
curr_song = subprocess.Popen(['audtool', 'current-song'], stdout=subprocess.PIPE)
status = "#nowplaying" + ' ' + curr_song.stdout.read().rstrip()

params = {"status": status}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)