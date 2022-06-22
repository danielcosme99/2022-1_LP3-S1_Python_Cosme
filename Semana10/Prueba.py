# -*- coding: utf-8 -*-
"""

"""

# Problema: Necesitamos mostrar los nombres de una cadena
# presentando las primeras letras en mayúscula
# En word se conoce como Formato Título

import camelcase

nombre = "flor elizabeth cerdan león"

print(nombre.upper())
print(nombre.title())

# Que pasaría si deseo que el nombre de flor y león 
# no tenga formato tiutlo
# Ahora utilizamos camelcase

cam = camelcase.CamelCase()
print("Con camelcase....")
print(cam.hump(nombre))

cam2 = camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))