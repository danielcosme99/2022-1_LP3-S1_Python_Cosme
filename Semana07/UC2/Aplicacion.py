# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:42:21 2022

@author: Carlos Cosme
"""

import Gestion_archivos

def menu():
    print("***MENU PRINCIPAL***")
    print("1. Crear Archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivos")
    print("5. Salir")

def crear():
    print("**CREAR ARCHIVO**")
    archivo = input("Crear archivo: ")
    contenido = input("Contenido del archivo: ")
    Gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("** ELIMINAR ARCHIVO**")
    archivo=input("Quiero eliminar el archivo: ")
    Gestion_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("** AGREGAR CONTENIDO A UN ARCHIVO**")
    archivo=input("Quiero agregar contenido al archivo: ")
    contenido = input("El contenido adicional del archivo sera: ")
    Gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("**MOSTRAR CONTENIDO DE UN ARCHIVO**")
    archivo = input("Quiero mostrar el contenido del archivo")
    print(Gestion_archivos.leer_archivo(archivo))
    
def salir():
    print("Gracias... Vuelva pronto")
    
def error():
    print("Opcion incorrecta")
    
#la logica para el menu de opciones
opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Selecciones una opcion [1-5]: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()