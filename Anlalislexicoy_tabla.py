import sys
import re
import subprocess

print("Analizador Léxico")

##Declaramos file para abrir y leer archivo
file = open(r"/home/gmichel/Documentos/codigo3.txt")

##Diccionarios de datos
operadores = {'=':'Asignacion','+':'Adicion','-':'Sustraccion','/':'Division','*':'Multiplicacion','<':'Menor que','>':'Mayor que','++':'incremento','!=':'desigualdad','==':'igualdad'}
operadores_key = operadores.keys()

tipo_dato = {'int':'tipo integer','float':'punto flotante','char':'tipo char','long':'long int','void':'tipo vacio'}
tipo_dato_key = tipo_dato.keys()

simbolo_puntuacion = {':':'dos puntos',';':'punto y coma','.':'punto',',':'coma','(':'parentesis apertura',')':'parentesis cierre','{':'llave apertura','}':'llave cierre','[':'corchete apertura',']':'corchete cierre'}
simbolo_puntuacion_key = simbolo_puntuacion.keys()

identificador = {'a':'id','b':'id','c':'id','d':'id','e':'id','f':'id','g':'id','h':'id','i':'id','j':'id','k':'id','l':'id','m':'id','n':'id','o':'id','p':'id','q':'id','r':'id','s':'id','t':'id','u':'id','v':'id','w':'id','x':'id','y':'id','z':'id','A':'id','B':'id','C':'id','D':'id','E':'id','F':'id','G':'id','H':'id','I':'id','J':'id','K':'id','L':'id','M':'id','O':'id','P':'id','Q':'id','R':'id','S':'id','T':'id','U':'id','V':'id','W':'id','X':'id','Y':'id','Z':'id','flag':'id'}
identificador_key = identificador.keys()

numero_entero = {'0':'cero','1':'uno','2':'dos','3':'tres','4':'cuatro','5':'cinco','6':'seis','7':'siete','8':'ocho','9':'nueve','13':'trece'}
numero_entero_key = numero_entero.keys()

estructura_selectiva = {'else':'ELSE','if':'IF','switch':'SWITCH','case':'CASE'}
estructura_selectiva_key = estructura_selectiva.keys()

estructura_repetitiva = {'for':'FOR','while':'WHILE','do':'DO'}
estructura_repetitiva_key = estructura_repetitiva.keys()

ins_preprocesador = {'#include':'INCLUDE','define':'DEFINE','<stdio.h>':'libreria'}
ins_preprocesador_keys = ins_preprocesador.keys()

palabra_reservada = {'return':'RETURN','main':'MAIN','printf':'IMPRIMIR'}
palabra_reservada_keys = palabra_reservada.keys()

##Leer el archivo
a = file.read()

count = 0

with open('tabla.txt', 'w') as file:
    file.write('{:^50}{:^30}{:^40}'.format('Componente Lexico', 'Lexema', 'Valor\n\n'))

program = a.split("\n")
for line in program:
    count = count + 1
    print("line #",count,"\n",line)
    
    ##Para leer separamos los tokens con el line split
    tokens = line.split(' ')
    print("Los tokens son ",tokens)
    
    print("Line #",count,"Propiedades \n")
    for token in tokens:
        if token in operadores_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('operador', token, operadores[token] ,'\n'))

        if token in tipo_dato_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Tipo de dato', token, tipo_dato[token],'\n'))

        if token in simbolo_puntuacion_key:
            with open('tabla.txt''', "a") as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Simbolo de puntuacion', token, simbolo_puntuacion[token],'\n'))

        if token in identificador_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Identificador', token, identificador[token],'\n'))

        if token in numero_entero_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Numero entero', token, numero_entero[token],'\n'))

        if token in estructura_selectiva_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Estructura selectiva', token, estructura_selectiva[token],'\n'))

        if token in estructura_repetitiva_key:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('tructura repetitivaEs', token, estructura_repetitiva[token],'\n'))

        if token in ins_preprocesador_keys:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Pre-procesador', token, ins_preprocesador[token],'\n'))

        if token in palabra_reservada_keys:
            with open('tabla.txt', 'a') as file:
                file.write('{:^50}{:^30}{:^30}{:^1}'.format('Palabra reservada', token, palabra_reservada[token],'\n'))

        #if token not in palabra_reservada_keys or ins_preprocesador_keys or estructura_repetitiva_key or estructura_selectiva_key or numero_entero_key or identificador_key or simbolo_puntuacion_key or tipo_dato_key or operadores_key:
          #  print(" Error en line #",count,token,"\n")
    print("- - - - - - - - - - - - - - - - - - - -")

        