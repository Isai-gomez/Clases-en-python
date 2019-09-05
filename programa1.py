import os, sys, time, re, string 
#import urllib
#import sqlite3 as dbapi
#print (dbapi.apilevel)
#print(sys.path)
#print (time.asctime())
#if(len(sys.argv)>1):
#	print ("Abriendo " + sys.argv[1])
#else:
#	print("Debes indicar el nombre del archivo")
#archivo = open("datos.txt", "a")
#print("archivo abierto con exito")
#lista = ["edad","peso","altura",21,23.4,74.5]
#close(archivo)
#print("Archivo cerrado")

cadena = input("escribe una palabra")
print(cadena)
#buscar = string.formatter_parser(cadena)
#if buscar == "tab":
#	print("encontramos", buscar)
mayuscula = cadena.upper() # La combierte a mayuscula
minuscula = cadena.lower() # La combierte a minusccula
print(minuscula , mayuscula)

s = "I intend to live forever, or die trying."
s.replace("to", "three")#remplasa to por three en la cadena #
