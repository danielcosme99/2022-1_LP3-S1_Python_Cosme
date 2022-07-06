# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:23:47 2022

@author: Cosme
"""

import sqlite3

# con el comando connect buscara la base de datos
# que tenga ese nombre, de lo contrario lo creara

conexion=sqlite3.connect("bdbiblioteca.db")
conexion.close()