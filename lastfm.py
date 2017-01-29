# -*- coding: utf-8 -*-
# http://d.hatena.ne.jp/ninoseki/20091018/1255866133
import urllib2
import re
import os
from BeautifulSoup import BeautifulStoneSoup
import Image
import ImageFileIO

class AlbumArt:
    def __init__(self, artist, album, api_key):
        self.api_key = api_key
        self.artist = artist
        self.album = album
        pass

    def openUrl(self):
        artist = re.sub(" ", "%20", self.artist)
        album = re.sub(" ", "%20", self.album)
        url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=%s&artist=%s&album=%s" % (self.api_key, artist, album)
        try:
            xml = urllib2.urlopen(url).read()
            pass
        except Exception:
            # print "can't open url"
            return 0
        return xml

    def getImageUrl(self, xml):
        image_url = ""
        soup = BeautifulStoneSoup(xml)
        e = soup.find("lfm")

        if e.has_key("status") and e["status"] == "ok":
            images =  e.findAll("image")
            if images[1].contents:
                #images[ここの数字を大きくすると画像サイズも大きくなる]
                image_url = images[3].contents[0]
                pass
            pass
        if image_url:
            return image_url
        else:
            return 0
        pass

    def saveImage(self, image_url):
        stream = urllib2.urlopen(image_url)
        if stream.info().gettype()[:5] == "image":
            python_script_path = os.path.abspath(os.path.dirname(__file__))
            file_name = python_script_path + "/.img/tmp.jpg"
            image = Image.open(ImageFileIO.ImageFileIO(stream))
            image.save(file_name, quality = 100)
            pass
        else:
            return 0
        # print "success! AlbumArt saved as %s" % file_name
        stream.close()