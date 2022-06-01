# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:10 2022

@author: User
"""
# Importamos la libreria camelcase

import camelcase

# Tenemos un cadena llamada nombre y se desea que se muestre 
# en formato titulo
nombre = "carlos daniel Cosme hernandez"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# Imprimimos el nombre en formato titulo
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto incluimos los argumentos
# 'carlos' y 'hernandez'

cam2=camelcase.CamelCase('carlos','hernandez')
print(cam2.hump(nombre))