# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:44:33 2022

@author: Cosme
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()

consulta = """ SELECT * 
                FROM LIBRO
                WHERE
                    precio >= 55
                ORDER BY titulo
            """
            
cursor=conexion.cursor()
cursor.execute(consulta)
libros=cursor.fetchall()

for libro in libros:
    print(libro)
    
conexion.close()
