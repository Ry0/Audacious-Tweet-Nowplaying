#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, subprocess, ConfigParser, sys, codecs
from requests_oauthlib import OAuth1Session

config = ConfigParser.ConfigParser()
config.read(['./aud-nowplaying.conf'])

# 自分で取得したTwitterの各種トークン
CONSUMER_KEY = config.get('connect_params', 'CONSUMER_KEY', 1)               # Consumer Key
# print CONSUMER_KEY
CONSUMER_SECRET = config.get('connect_params', 'CONSUMER_SECRET', 1)         # Consumer Secret
# print CONSUMER_SECRET
ACCESS_TOKEN_KEY = config.get('connect_params', 'ACCESS_TOKEN_KEY', 1)       # Access Token
# print ACCESS_TOKEN_KEY
ACCESS_TOKEN_SECRET = config.get('connect_params', 'ACCESS_TOKEN_SECRET', 1) # Accesss Token Secert
# print ACCESS_TOKEN_SECRET

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# Audaciousからいま再生している楽曲データを取得
curr_song = subprocess.Popen(['audtool', 'current-song'], stdout=subprocess.PIPE)

print "コメントを入力"
comment = raw_input('>>>  ')

status = "#nowplaying" + ' ' + curr_song.stdout.read().rstrip() + ' ' + comment
params = {"status": status}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)