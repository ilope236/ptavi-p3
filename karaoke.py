#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


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
        if key != 'name' and diccionario[key] != "":
            print key+"="+diccionario[key]+ "\t",
    print
