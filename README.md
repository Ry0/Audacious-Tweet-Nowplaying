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

##TwitterAPIの取得
TwitterからAPIを取得してください

>TwitterDevelopers  
>[https://dev.twitter.com/apps](https://dev.twitter.com/apps)

そしてこのレポジトリに`aud-nowplaying.conf`というファイル名で認証情報を作成

```bash
cd Audacious-Tweet-Nowplaying
gedit aud-nowplaying.conf
```

```html
[connect_params]
consumer_key = abcdefghijklmnopqrstuvwxy
consumer_secret = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx
access_token_key = 123456789-ABCDEFGHIJKLMNOPQRSTUVWXYABCDEFGHIJKLMNO
access_token_secret = abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrst
```

こんな感じで作成

##aud-nowplaying.pyの修正
`aud-nowplaying.conf`の場所を`aud-nowplaying.py`に記述してあるのでパスを自分の環境に修正

```python
config.read(['aud-nowplaying.conf'])
```

##ツイートしてみる
Audaciousで音楽再生中に実行する

```bash
python aud-nowplaying.py
```