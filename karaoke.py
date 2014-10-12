#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os

try:
    fichero = sys.argv[1]
except IndexError:
    print "Usage: python karaoke.py file.smil."
    raise SystemExit

parser = make_parser()
sHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(sHandler)
parser.parse(open(fichero))

lista_dic = sHandler.get_tags()

for diccionario in lista_dic:
    print diccionario['name'] + "\t",
    for key in diccionario:
        if key != 'name' and diccionario[key]:
            print key + "=" + diccionario[key] + "\t",
            if key == 'src' and diccionario[key][:7] == 'http://':
                os.system("wget -q " + diccionario[key])
                lista_barras = diccionario[key].split('/')
                diccionario[key] = lista_barras[-1]
    print
