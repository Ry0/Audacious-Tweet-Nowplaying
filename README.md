#Ubuntuの音楽プレイヤーAudaciousでTwitterに#nowplayingをツイートするためのPythonスクリプト
##Audaciousのインストール
```bash
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get install audacious
```

##このレポジトリをクローン

```bash
git clone https://github.com/Ry0/Audacious-Tweet-Nowplaying.git
```

##必要なPythonライブラリをインストール

```bash
cd Audacious-Tweet-Nowplaying
sudo pip install -r requirements.txt
```

##TwitterAPIとLast.fm APIの取得
TwitterからAPIを取得してください

>TwitterDevelopers  
>[https://dev.twitter.com/apps](https://dev.twitter.com/apps)


>Create API account   
>[http://www.last.fm/api/account/create](http://www.last.fm/api/account/create)

そしてこのレポジトリに`aud-nowplaying.conf`というファイル名で認証情報を作成

```bash
cd Audacious-Tweet-Nowplaying
gedit aud-nowplaying.conf
```

```html
[twitter_params]
consumer_key = abcdefghijklmnopqrstuvwxy
consumer_secret = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx
access_token_key = 123456789-ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNO
access_token_secret = abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrst

[lastfm_params]
api_key = abcdefghijklmnopqrstuvwxyzABCDEF
```

こんな感じで作成．

##ツイートしてみる
Audaciousで音楽再生中に実行する

```bash
python aud-nowplaying.py
```

![img](.img/screenshot_1.png)

![img](.img/screenshot_2.png)