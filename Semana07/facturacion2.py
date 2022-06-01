# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:52:11 2022

@author: User
"""

# Dado el total, calcular el IGV y el Subtotal

import financieros
total = 1000.49

print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")
