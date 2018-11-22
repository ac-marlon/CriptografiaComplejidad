# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:14:34 2018

@author: FamiliaHogar
"""

from math import floor
import numpy as np

#Sistema de ecuaciones diferenciales
def atractorLorenz(x, y, z, s=10, r=28, b=(8 / 3)):
    xPunto = s * (y - x)
    yPunto = r * x - y - x * z
    zPunto = x * y - b * z
    return xPunto, yPunto, zPunto

#Parametros realcionados con el diferencial de tiempo y la cantidad de pasos
dt = 0.01
pasoValores = 9999

xs = np.empty((pasoValores + 1,))
ys = np.empty((pasoValores + 1,))
zs = np.empty((pasoValores + 1,))

#Clave (condiciones inciales para generar la secuencia cifrante)
#Puede ser d elongitud variable
clave = (0.003882, 0.488801, 1.020202)
print("La clave es:", clave)
xs[0], ys[0], zs[0] = clave

#Comportamiento del atractor a traves de pasoValores
for i in range(pasoValores):
    #Derivadas de x, y, z en el paso actual
    xPrima, yPrima, zPrima = atractorLorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (xPrima * dt)
    ys[i + 1] = ys[i] + (yPrima * dt)
    zs[i + 1] = zs[i] + (zPrima * dt)

#Contenedores de las secuencias aleatorias (pseudo-aleatorias)
secuenciaCifranteDecimal = []
secuenciaAux = []
secuenciaCifranteBinaria = []

#Se eligen las variaciones positivas de xs para conformar la secuencia cifrante
#Y ademas se aproximan al menor entero con al funcion floor
for i in range(pasoValores):
    if xs[i] > 0:
        secuenciaCifranteDecimal.append(floor(xs[i] * 100))

#De la secuencia anterior se convierten en 1 los pares y en 0 los impares
for j in secuenciaCifranteDecimal:
    if j % 2 == 0:
        secuenciaAux.append(1)
    else:
        secuenciaAux.append(0)

#Texto de prueba y su representacion en binario
textoClaro = "Sin desviarse de la norma el progreso no es posible"
print("El mensaje original es:", textoClaro)
textoAux = ''.join(format(ord(x), 'b').zfill(8) for x in textoClaro)
textoClaroBin = []

for j in textoAux:
    textoClaroBin.append(int(j))

#Se consigue la secuencia cifrante definitiva segun la longitud del texto claro
#Se recorre desde el ultimo digito de la secuencia binaria hasta la longitud -m
#Ademas se tienen en cuenta los espacios en el mensaje
for m in range(len(textoClaro) * 8):
    secuenciaCifranteBinaria.append(secuenciaAux[-m])

textoCifrado = []

#Se realiza la operacion logica XOR entre textoClaro y secuenciaCifranteBinaria
#De este modo se tiene el texto cifrado
for p, q in zip(textoClaroBin, secuenciaCifranteBinaria):
    textoCifrado.append((p & ~ q) | (~ p & q))

#Bloque para comprobar que el texto cifrado es ininteligible
#------------------------------------------------------------------------------
prueba = []

for j in textoCifrado:
    prueba.append(str(j))

pruebaASCII = ''.join(format(ord(x), 'c') for x in prueba)
mensajeCifrado = ""

while pruebaASCII != "":
    i = chr(int(pruebaASCII[:8], 2))
    mensajeCifrado = mensajeCifrado + i
    pruebaASCII = pruebaASCII[8:]

print("El mensaje cifrado es:", mensajeCifrado)
#------------------------------------------------------------------------------

#Para descifrar el mensaje se realiza el mismo procedimiento de forma inversa
#De esta manera al aplicar la operacion XOR se recupera el mensjae original
mensajeDescifrado = []

for p, q in zip(textoCifrado, secuenciaCifranteBinaria):
    mensajeDescifrado.append((p & ~ q) | (~ p & q))

#Bloque para comprobar que el mensaje descifrado es identico al original
#En cuyo caso la recuperacion de la informacion es satisfactoria
#------------------------------------------------------------------------------
prueba2 = []

for j in mensajeDescifrado:
    prueba2.append(str(j))

pruebaASCII2 = ''.join(format(ord(x), 'c') for x in prueba2)
textoDescifradoRecuperado = ""

while pruebaASCII2 != "":
    i = chr(int(pruebaASCII2[:8], 2))
    textoDescifradoRecuperado = textoDescifradoRecuperado + i
    pruebaASCII2 = pruebaASCII2[8:]

print("El mensaje descifrado (recuperado) es:", textoDescifradoRecuperado)
#------------------------------------------------------------------------------
