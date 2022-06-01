# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:48:07 2022

@author: User
"""

archivo=open("archivo_de_prueba.txt",'wt')
contenido="Linea1 hola amigos ¿Como estan?\nLinea2 Bienvenidos a la UNTELS"
archivo.write(contenido)
archivo.close()