# -*- coding: utf-8 -*-
"""

"""

# Problema: Necesitamos mostrar los nombres de una cadena
# presentando las primeras letras en mayúscula
# En word se conoce como Formato Título

# Importamos la libreria
import camelcase

nombre = "flor elizabeth cerdan león"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")
# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))