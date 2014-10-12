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
        for diccionario in self.lista_dic:
            print diccionario['name'] + "\t",
            for key in diccionario:
                if key != 'name' and diccionario[key]:
                    print key + "=" + diccionario[key] + "\t",
            print

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
    karaoke.__str__()
    karaoke.do_local()
    karaoke.__str__()
