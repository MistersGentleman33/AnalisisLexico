#  ANALIZADOR EN PYTHON
![](https://2.bp.blogspot.com/-tzQyWIBjg1E/Vva72o0VT1I/AAAAAAAABfs/-l8476gfcxk4Licz7Z_Pbm0UozxcY6M6Q/s1600/Compiladores%2Bde%2Bcodigo%2Bonline.png)

------------

# Integrantes:
## Sanchez Palafox Manuel
## Caballero Perdomo Axel Lennyn
## Acosta Cortes Gerardo Michel
## Castillo Salgado Edgar Sebastian
## 

------------


## Introduccion
El análisis léxico-sintáctico tiene por objeto reconocer la forma de las sentencias de un lenguaje.
Reconocer la forma de una sentencia implica reconocer sus lexemas y estructuras sintácticas. El
resultado del análisis léxico-sintáctico puede ser un error de reconocimiento o una versión de la
sentencia reconocida en forma de árbol de sintaxis abstracta (asa).

![](https://sites.google.com/site/compiladoresesilval/_/rsrc/1468848842177/home/compiladores/analisis-lexico/AnalizadorLexico.jpg)

Para reconocer los lexemas de un lenguaje usaremos expresiones regulares y para reconocer
estructuras sintácticas usaremos gramáticas independientes de contexto (gramática en
adelante).
Una gramática es un conjunto de reglas. Cada regla es de la forma genérica:

*cabeza : cuerpo1 | cuerpo2 | ... | cuerpoN siendo N>=1*

La cabeza de la regla es un símbolo llamado no terminal que representa una estructura
sintáctica. El cuerpo de la regla está compuesto por símbolos terminales (lexemas) y no
terminales. La composición de estos símbolos se consigue haciendo uso de alternativas,
iteraciones y yuxtaposiciones.

## Desarrollo
#### Explicacion del codigo
Primero se imprime en pantalla el titulo "Analizador Lexico"
```python
print("Analizador Léxico")
```
Seguido de esto tenemos la linea que abre el archivo que querramos leer
```python
file = open(r"/home/gmichel/Documentos/codigo3.txt")
```

###### Diccionario de datos
Se crea un diccionario de datos el cual asigna valores a todos los tokens que se pueden encontrar dentro del archivo que querramos leer como:
 - Operadores.
```python
operadores = {'=':'Asignacion','+':'Adicion','-':'Sustraccion','/':'Division','*':'Multiplicacion','<':'Menor que','>':'Mayor que','++':'incremento','!=':'desigualdad','==':'igualdad'}
operadores_key = operadores.keys()
```
 - Tipos de datos
```python
tipo_dato = {'int':'tipo integer','float':'punto flotante','char':'tipo char','long':'long int','void':'tipo vacio'}
tipo_dato_key = tipo_dato.keys()
```
 - Simbolos
 ```python
simbolo_puntuacion = {':':'dos puntos',';':'punto y coma','.':'punto',',':'coma','(':'parentesis apertura',')':'parentesis cierre','{':'llave apertura','}':'llave cierre','[':'corchete apertura',']':'corchete cierre'}
simbolo_puntuacion_key = simbolo_puntuacion.keys()
```
 - Identificadores
```python
identificador = {'a':'id','b':'id','c':'id','d':'id','e':'id','f':'id','g':'id','h':'id','i':'id','j':'id','k':'id','l':'id','m':'id','n':'id','o':'id','p':'id','q':'id','r':'id','s':'id','t':'id','u':'id','v':'id','w':'id','x':'id','y':'id','z':'id','A':'id','B':'id','C':'id','D':'id','E':'id','F':'id','G':'id','H':'id','I':'id','J':'id','K':'id','L':'id','M':'id','O':'id','P':'id','Q':'id','R':'id','S':'id','T':'id','U':'id','V':'id','W':'id','X':'id','Y':'id','Z':'id','flag':'id'}
identificador_key = identificador.keys()
```
 - Numeros enteros
```python
numero_entero = {'0':'cero','1':'uno','2':'dos','3':'tres','4':'cuatro','5':'cinco','6':'seis','7':'siete','8':'ocho','9':'nueve','13':'trece'}
numero_entero_key = numero_entero.keys()
```

 - Preprocesadores
```python
ins_preprocesador = {'#include':'INCLUDE','define':'DEFINE','<stdio.h>':'libreria'}
ins_preprocesador_keys = ins_preprocesador.keys()
```
 - Palabras reservadas, estructuras selectivas y repetitivas

	```python
	estructura_selectiva = {'else':'ELSE','if':'IF','switch':'SWITCH','case':'CASE'}
	estructura_selectiva_key = estructura_selectiva.keys()

	estructura_repetitiva = {'for':'FOR','while':'WHILE','do':'DO'}
	estructura_repetitiva_key = estructura_repetitiva.keys()

	palabra_reservada = {'return':'RETURN','main':'MAIN','printf':'IMPRIMIR'}
	palabra_reservada_keys = palabra_reservada.keys()

	```

###### Lectura del archivo
Una vez indicado el diccionario de datos y teniendo en cuenta todos los tokens del programa se crea un archivo ***.txt*** para iniciar el formato de tabla

```python
a = file.read()

count = 0

with open('table_nam', 'w') as file:
	file.write('{:^50}{:^30}{:^40}'.format('Componente Lexico', 'Lexema', 'Valor\n\n'))
```
Esta funcion da el formato de tabla de tokens, el fwrite es para escribir en el archivo y tiene un contador para llenar la tabla respetando espacios y colocando respectivamente dependiendo si es componente lexico, lexema o valor.


Posteriormente, el programa que querramos leer desde un inicio se separa por lineas y despues por token con la funcion ***.split*** sin tomar en cuenta los espacios para identificarlos en los diccionarios previamente creados.
```python
program = a.split("\n")
for line in program:
    count = count + 1
    print("line #",count,"\n",line)
    
    ##Para leer separamos los tokens con el line split
    tokens = line.split(' ')
    print("Los tokens son ",tokens)
```
Una vez que el programa leyo token por token el archivo y los identifico por diccionarios, se llama a cada uno de estos para escribirlos respectivamente en la tabla de tokens previamente creada.

```python
 print("Line #", count, "Propiedades \n")
for token in tokens:
	if token in operadores_key:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('operador', token, operadores[token], '\n'))

	if token in tipo_dato_key:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('Tipo de dato', token, tipo_dato[token], '\n'))

	if token in simbolo_puntuacion_key:
		with open('table_nam''', "a") as file:
			file.write(
				'{:^50}{:^30}{:^30}{:^1}'.format('Simbolo de puntuacion', token, simbolo_puntuacion[token], '\n'))

	if token in identificador_key:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('Identificador', token, identificador[token], '\n'))

	if token in numero_entero_key:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('Numero entero', token, numero_entero[token], '\n'))

	if token in estructura_selectiva_key:
		with open('table_nam', 'a') as file:
			file.write(
				'{:^50}{:^30}{:^30}{:^1}'.format('Estructura selectiva', token, estructura_selectiva[token], '\n'))

	if token in estructura_repetitiva_key:
		with open('table_nam', 'a') as file:
			file.write(
				'{:^50}{:^30}{:^30}{:^1}'.format('tructura repetitivaEs', token, estructura_repetitiva[token], '\n'))

	if token in ins_preprocesador_keys:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('Pre-procesador', token, ins_preprocesador[token], '\n'))

	if token in palabra_reservada_keys:
		with open('table_nam', 'a') as file:
			file.write('{:^50}{:^30}{:^30}{:^1}'.format('Palabra reservada', token, palabra_reservada[token], '\n'))
```
Para al final dar una tabla con un formato parecido a este en el txt.
**..........Componente Lexico..........Lexema..........Valor..........**

###### Lectura del archivo
Se realizaron los automatas para definir cada token y las funciones, de igual manera se realizaron las expresiones regulares:
###### Para un *for*
![](https://raw.githubusercontent.com/MistersGentleman33/AnalisisLexico/main/AutomataFor.png)

La expresion regular para este automata es:
```c
ER= for( ((id = (id| (1-9)+)) ; (id op (id| (1-9)+) | ; (id 9++))
```

###### Para un *Tipo de Dato*
![](https://raw.githubusercontent.com/MistersGentleman33/AnalisisLexico/main/AutomataTipoDato.png)

La expresion regular para este automata es:
```c
ER= tipo de dato * ?(A-Z a-z 0-9)+ = ?(A-Z a-z 0-9)*( , | ; | ( | ) | { ) ?)+
```
###### Para un *Printf(*
![](https://raw.githubusercontent.com/MistersGentleman33/AnalisisLexico/main/AutomataPrint.png)

Tomando en cuenta que el lenguaje ∑ es:
    ∑= lenguaje = {A-Z, a-z, 1-9, { }, ( ), "", simbolos }

La expresion regular para este automata es:
```c
Printf((,?ID,? |"(a-z)+")+)
```
###### Para una llamar una libreria
![](https://raw.githubusercontent.com/MistersGentleman33/AnalisisLexico/main/AutomataLib.png)

Tomando en cuenta que el lenguaje ∑ es:
   ∑= lenguaje = {A-Z, a-z, 1-9, simbolos }

La expresion regular para este automata es:
```c
ER= # ( ( include < libreria .h >) | define ( ∑)+ ) )
```
###### Para un *if*
![](https://raw.githubusercontent.com/MistersGentleman33/AnalisisLexico/main/AutomataIf.png)

La expresion regular para este automata es:
```c
if((id op (id|valor))+ (&&| II ) ?)+
```

## Conclusion

**Acosta Cortes Gerardo Michel:** Con la realización de la práctica pude comprender mejor el funcionamiento de un analizador tanto léxico cómo sintáctico, se puede ver cómo no es algo vanal ya que se requiere ciertos conocimientos de lenguajes de programación y sobretodo el uso de autómatas para hacer un programa eficiente, es muy importante que al menos en lo teórico esto se comprenda al 100, para poder ver el funcionamiento de un compilador de manera más completa.

**Castillo Salgado Edgar Sebastian:** Hoy en dia, gracias a raiz del increible avance de las nuevas tecnologias y la ciencia,
las máquinas autómatas son un realidad con muchas de las cuales interactuamos a diario y que
contribuyen en hacer la vida mucho más sencilla en algunas actividades.
En el caso de esta practica nos facilita el realizar los diferentes Análisis que se llevan a cabo en un compilador, mediante una expresión regular con la cual armamos los diferentes automatas para la obtencion de errores en el codigo.

**Sanchez Palafox Manuel**

**Caballero Perdomo Axel Lennyn**
Como conclusión puedo decir que el desarrollar esta practica nos permitio conocer a profundidad todo el trabajo que realiza nuestro compilador o interprete, en caso de lenguajes como Python, una vez que lo programas te da un pequeño panorama de como realiza su trabajo el compilador, la parte más difícil de esta práctica fue identificar los errores sintácticos ya que como humano es fácil reconocerlos si sabes la gramática y semántica del lenguaje de programación, pero una maquina no entiende el contexto, para ella son 1's y 0's, negro o blanco no hay grises, por lo que fue para nosotros dificl hacer que entienda que era un error y que no.

## Bibliografias
[Analisis lexico y sintactico](http://www.lsi.us.es/docencia/get.php?id=7469 "Analisis lexico y sintactico")
