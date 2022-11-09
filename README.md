#  ANALIZADOR LEXICO
![](https://sites.google.com/site/compiladoresesilval/_/rsrc/1468848842177/home/compiladores/analisis-lexico/AnalizadorLexico.jpg)

------------

# Integrantes:
## Sanchez Palafox Manuel
## Caballero Perdomo Axel Lennyn
## Acosta Cortes Gerardo Michel
## Castillo Salgado Edgar Sebastian
## 

------------


## Librerias utilizadas:
- ### sys
El **módulo** sys en Python proporciona varias funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecución de Python. Permite operar sobre el intérprete ya que proporciona acceso a las variables y funciones que interactúan fuertemente con el intérprete. Consideremos el siguiente ejemplo.

- ### re
Este módulo proporciona operaciones de coincidencia de expresiones regulares similares a las que se encuentran en Perl.

Tanto los patrones como las cadenas que se buscarán pueden ser cadenas Unicode ( str), así como cadenas de 8 bits ( bytes). Sin embargo, las cadenas Unicode y las cadenas de 8 bits no se pueden mezclar: es decir, no puede hacer coincidir una cadena Unicode con un patrón de bytes o viceversa; De manera similar, al solicitar una sustitución, la cadena de reemplazo debe ser del mismo tipo que el patrón y la cadena de búsqueda.

Las expresiones regulares utilizan el carácter de barra invertida ( '\') para indicar formas especiales o para permitir el uso de caracteres especiales sin invocar su significado especial. Esto choca con el uso de Python del mismo carácter para el mismo propósito en cadenas literales; por ejemplo, para hacer coincidir una barra invertida literal, es posible que tenga que escribir '\\\\'como cadena de patrón, porque la expresión regular debe ser \\, y cada barra invertida debe expresarse como \\dentro de una cadena literal de Python normal. Además, tenga en cuenta que cualquier secuencia de escape no válida en el uso de Python de la barra invertida en los literales de cadena ahora genera un DeprecationWarning y en el futuro se convertirá en un SyntaxError. Este comportamiento ocurrirá incluso si es una secuencia de escape válida para una expresión regular.

La solución es usar la notación de cadenas sin procesar de Python para patrones de expresiones regulares; las barras invertidas no se manejan de ninguna manera especial en un literal de cadena con el prefijo 'r'. También lo r"\n"es una cadena de dos caracteres que contiene '\'y 'n', mientras que "\n"es una cadena de un carácter que contiene una nueva línea. Por lo general, los patrones se expresarán en código Python utilizando esta notación de cadena sin procesar.

Es importante tener en cuenta que la mayoría de las operaciones con expresiones regulares están disponibles como funciones y métodos a nivel de módulo en expresiones regulares compiladas . Las funciones son atajos que no requieren que primero compiles un objeto regex, pero pierden algunos parámetros de ajuste.

- ### subprocess
El subproceso en Python es un módulo que se utiliza para ejecutar nuevos códigos y aplicaciones mediante la creación de nuevos procesos. Le permite iniciar nuevas aplicaciones directamente desde el programa de Python que está escribiendo actualmente. Entonces, si desea ejecutar programas externos desde un repositorio de git o códigos de programas C o C++ , puede usar el subproceso en Python. También puede obtener códigos de salida y canalizaciones de entrada, salida o error utilizando el subproceso en Python . 

## Desarrollo
- ### Explicacion del codigo
Primero se colocan las librerias a utilizar, las cuales ya hemos visto en el punto anterior, 
###### 
**import sys** se utiliza para dar acceso a las variables y manipularlas durante el tiempo de ejecucion del programa.
###### 
**import re** se utiliza para el procesamiento de cadenas y expresiones regulares que mas adelante nos ayudara para el analizador lexico.
###### 
**import subprocess** se utiliza para ejecutar nuevos procesos, en este programa se utiliza en la def pawk para ejecutar python3 y pawk.py como subprocesos

##### Def pawk
```python
def pawk(args, i):
    i = str(i)
    position = "f[" + i + "]"
    echo = subprocess.run(["echo", args], check=True, capture_output=True)
    awk = subprocess.run(["python3", "pawk/pawk.py", "-F", " ", position], input=echo.stdout, capture_output=True)
    awk_output = awk.stdout.decode("utf-8").strip()

    return awk_output

```
Esta funcion sirve para
###### 
##### Def write_table
```python
def write_table(list_int, list_float, list_double, list_char, table_name):
    with open(table_name, "w") as file:
        file.write("\tComponente Lexico\tLexema\tValor\n")

    for i in list_int:
        spaces = i.count(" ")
        for x in range(spaces + 1):
            awk_output = pawk(i, x)
            print(awk_output)
```
Esta funcion da el formato de tabla de tokens, el fwrite es para escribir en el archivo y tiene un contador para llenar la tabla respetando espacios y colocando respectivamente dependiendo si es componente lexico, lexema o valor.

#####Def recognize_variables
```python
def recognize_variables(file):   

    expression_int = re.compile(r"int \w+ = [0-9]+|, [a-zA-Z]+ = [0-9]+")
    expression_float = re.compile("float \w+ = [0-9]+.[0-9]+|, [a-zA-Z]+ = [0-9]+.[0-9]+")
    expression_double = re.compile("double \w+ = [0-9]+.[0-9]+|, [a-zA-Z] = [0-9]+.[0-9]+")
    expression_char = re.compile("char \*\w+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"|\']"
                                 "|, [a-zA-Z]+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"\']|char "
                                 "\w+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"|\']"
                                 "")

    return expression_int.findall(file), expression_float.findall(file), \
           expression_double.findall(file), expression_char.findall(file)
```
Esta funcion define las expresiones regulares para cada variable dependiendo del tipo de esta misma como se puede observar para el analizador existen variables int, float, double y char.
#####Def read_file
```python
def read_file(input_text):  # Lectura del archivo, cada linea la guarda en una lista
    with open(input_text) as archivo:
        archivo = archivo.read()

    return archivo
```
Esta funcion lee el archivo y guarda cada linea en una lista, como se observa recibe un archivo y genera otro con este mismo ya analizado.
#####Def main
```python
def main():
    # Variables Flags
    input_text = sys.argv[1]
    table_name = sys.argv[2]
    # errors = sys.argv[3]

    # Functions
    file = read_file(input_text)  # Variable que contiene el archivo en string
    print("Esta es una prueba de lectura de archivo: \n {} \n".format(file))
    list_int, list_float, list_double, list_char = recognize_variables(file)
    print(list_int, list_float, list_double, list_char)
    write_table(list_int, list_float, list_double, list_char, table_name)

```
Aqui se inicializan todas las variables, input_text y table_name las iguala para recibir cadenas y las demas variables solo las imprime en la tabla del txt.
#####try:
```python
try:
    if __name__ == "__main__":
        main()
```
#####except ValueError:
```python
except ValueError:
    print("\nInvalid Arguments: %s" % sys.argv[1])

```
Genera una impresion de pantalla en caso de un error.
##### except
```python
except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <code.c> " + " <name_table>.txt " + "<errors>.txt\n")
```
Genera una ultima impresion de pantalla independiente para indicar el uso del programa al momento de su compilacion.
## Conclusion

## Bibliografias
[Lib subprocess](https://www.simplilearn.com/tutorials/python-tutorial/subprocess-in-python#:~:text=Subprocess%20in%20Python%20is%20a,can%20use%20subprocess%20in%20Python "1")
[Lib re](https://docs.python.org/3/library/re.html "Lib re")
[Lib sys](https://www.geeksforgeeks.org/python-sys-module/#:~:text=The%20sys%20module%20in%20Python,interact%20strongly%20with%20the%20interpreter. "Lib sys")
