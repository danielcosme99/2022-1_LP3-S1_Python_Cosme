# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:17:25 2022

@author: Cosme
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")

consulta ="""INSERT INTO 
                PAIS(NOMBRE, ESTADO)
                VALUES('Brasil', 'A')
          """

cursor=conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()
