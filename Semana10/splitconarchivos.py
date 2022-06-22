# -*- coding: utf-8 -*-
noticia = open("noticia.txt","rt",encoding='utf-8-sig')

datos_noticia = noticia.read()

lista = datos_noticia.split()

print(datos_noticia)

print(lista)