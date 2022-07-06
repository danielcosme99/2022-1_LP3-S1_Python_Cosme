# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:52:52 2022

@author: Cosme
"""

import sqlite3
conexion=sqlite3.connect("bdbiblioteca.db")

cursor=conexion.cursor()

consulta="""DELETE FROM EDITORIAL
            WHERE
                IDEDITORIAL=5
            """
            
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()

