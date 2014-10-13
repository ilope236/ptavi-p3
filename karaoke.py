#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista_dic = sHandler.get_tags()

    def __str__(self):
        str_total = ""
        for dicc in self.lista_dic:
            etiqueta = dicc['name']
            attr = ""
            for key in dicc:
                if key != 'name' and dicc[key]:
                    attr = attr + '\t' + key + "=" + '"' + dicc[key] + '"'
            str_total = str_total + etiqueta + attr + '\n'
        return str_total

    def do_local(self):
        for diccionario in self.lista_dic:
            for key in diccionario:
                if key == 'src' and diccionario[key][:7] == 'http://':
                    os.system("wget -q " + diccionario[key])
                    lista_barras = diccionario[key].split('/')
                    diccionario[key] = lista_barras[-1]

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        print "Usage: python karaoke.py file.smil."
        raise SystemExit

    karaoke = KaraokeLocal(fichero)
    print karaoke
    karaoke.do_local()
    print karaoke
