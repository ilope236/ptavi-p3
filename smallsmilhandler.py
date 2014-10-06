#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista_tags = []

        self.rootlayout = ""
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""

        self.region = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""

        self.img = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""

        self.audio = ""
        self.src = ""
        self.begin = ""
        self.dur = ""

        self.textstream = ""
        self.src = ""
        self.region = ""
     

    def startElement(self, name, attrs):
        dic_attrs = {}
        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('background-color',"")

            dic_attrs['name'] = name
            dic_attrs['width'] = self.width
            dic_attrs['height'] = self.height
            dic_attrs['backgroundcolor'] = self.backgroundcolor

            self.lista_tags.append(dic_attrs)

        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")

            dic_attrs['name'] = name
            dic_attrs['id'] = self.id
            dic_attrs['top'] = self.top
            dic_attrs['bottom'] = self.bottom
            dic_attrs['left'] = self.left
            dic_attrs['right'] = self.right

            self.lista_tags.append(dic_attrs)

        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")

            dic_attrs['name'] = name
            dic_attrs['region'] = self.region
            dic_attrs['begin'] = self.begin
            dic_attrs['dur'] = self.dur

            self.lista_tags.append(dic_attrs)

        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")

            dic_attrs['name'] = name
            dic_attrs['src'] = self.src
            dic_attrs['begin'] = self.begin
            dic_attrs['dur'] = self.dur

            self.lista_tags.append(dic_attrs)

        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")

            dic_attrs['name'] = name
            dic_attrs['src'] = self.src
            dic_attrs['dur'] = self.dur

            self.lista_tags.append(dic_attrs)         

    def get_tags(self):
        return self.lista_tags


if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
