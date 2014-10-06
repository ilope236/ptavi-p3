#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.lista_dic = []
        self.tags = ['root-layout', 'region', 'img', 'audio', 'textstream']
        self.attrs = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
        }

    def startElement(self, name, attrs):
        dic_attrs = {}
        if name in self.tags:
            dic_attrs['name'] = name
            for atributo in self.attrs[name]:
                dic_attrs[atributo] = attrs.get(atributo, "")
            self.lista_dic.append(dic_attrs)

    def get_tags(self):
        return self.lista_dic

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
