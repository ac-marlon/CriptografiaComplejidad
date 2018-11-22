# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:13:20 2018

@author: FamiliaHogar
"""
#Se define la forma recursiva del GCL
def generadorCongruencial(Xn, a, c, m):
    return (a * Xn + c) % m

#Generador de la primera secuencia de numeros pseudo-aleatorios
def primerGCL(X, a, c, m):
    secuenciaPrimerGen = []
    for _i in range(m[0]):
        X[0] = generadorCongruencial(X[0], a[0], c[0], m[0])
        secuenciaPrimerGen.append(X[0])
    return secuenciaPrimerGen

#Generador de la segunda secuencia de numeros pseudo-aleatorios
def segundoGCL(X, a, c, m):
    secuenciaSegundoGen = []
    for _j in range(m[1]):
        X[1] = generadorCongruencial(X[1], a[1], c[1], m[1])
        secuenciaSegundoGen.append(X[1])
    return secuenciaSegundoGen

#Generador de la tercera secuencia de numeros pseudo-aleatorios
def tercerGCL(X, a, c, m):
    secuenciaTercerGen = []
    for _k in range(m[2]):
        X[2] = generadorCongruencial(X[2], a[2], c[2], m[2])
        secuenciaTercerGen.append(X[2])
    return secuenciaTercerGen

#Se efectua la suma de las tres secuencias generadas por los GCL
#Ademas hay que tener en cuenta que las cifras escogidas se basan en la 
#secuencia mas corta para que haya coherencia y se suman las primeras del
#primer y tercer GCL y las ultimas del segundo GCL
def unionGCL(m, secuenciaPrimerGen, secuenciaSegundoGen, secuenciaTercerGen):
    sFinal = []
    for p in range(min(m)):
        sFinal.append((secuenciaPrimerGen[-p] + secuenciaSegundoGen[p]
                       + secuenciaTercerGen[-p]) / 100)
    return sFinal

#Se suman los elementos de clave que se pasa como argumento
def claveCriptosistema(listaNumeros):
    if len(listaNumeros) == 1:
        return listaNumeros[0]
    return listaNumeros[0] + claveCriptosistema(listaNumeros[1:])

def main():
    
    #Se definene los parametros de trabajo de los tres GCL respectivamente
    #Se debe tener en cuenta que la semilla X es la clave de los generadores
    X = [3, 8, 2]
    a = (21, 25, 13)
    c = (7, 11, 5)
    m = (64, 48, 72)

    claveUno = []
    claveDos = []
    claveTres = []
    
    #Se invoca el metodo que calcula la secuencia final de numeros
    sF = unionGCL(m, primerGCL(X, a, c, m), segundoGCL(X, a, c, m), tercerGCL(X, a, c, m))
    
    #Se divide la secuencia final en tres partes iguales (claves), se suman los
    #elementos de cada una y se dividen entre un factor elegido para aumentar
    #la aleatoriedad y la longitud de cada una para diez digitos decimales
    claveUno = "{0:.10f}".format(claveCriptosistema(sF[:int(min(m)/3)])/1000.987)
    claveDos = "{0:.10f}".format(claveCriptosistema(sF[int(min(m)/3):int(2*min(m)/3)])/1000.123)
    claveTres = "{0:.10f}".format(claveCriptosistema(sF[int(2*min(m)/3):])/1000.564)
    
    #Las tres claves se guardan en una tupla para que funcionen como llave
    #en el criptosistema basado en la dinamica del atractor de Lorenz
    claveFinal = (float(claveUno), float(claveDos), float(claveTres))
    print("Clave:", claveFinal)

if __name__ == "__main__":
    main()
