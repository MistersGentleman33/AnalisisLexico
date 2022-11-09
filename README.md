#  ANALIZADOR LEXICO

# Integrantes:
## Sanchez Palafox Manuel
## 
## 
## 


## Librerias utilizadas:
### sys
El **módulo** sys en Python proporciona varias funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecución de Python. Permite operar sobre el intérprete ya que proporciona acceso a las variables y funciones que interactúan fuertemente con el intérprete. Consideremos el siguiente ejemplo.

### re
Este módulo proporciona operaciones de coincidencia de expresiones regulares similares a las que se encuentran en Perl.

Tanto los patrones como las cadenas que se buscarán pueden ser cadenas Unicode ( str), así como cadenas de 8 bits ( bytes). Sin embargo, las cadenas Unicode y las cadenas de 8 bits no se pueden mezclar: es decir, no puede hacer coincidir una cadena Unicode con un patrón de bytes o viceversa; De manera similar, al solicitar una sustitución, la cadena de reemplazo debe ser del mismo tipo que el patrón y la cadena de búsqueda.

Las expresiones regulares utilizan el carácter de barra invertida ( '\') para indicar formas especiales o para permitir el uso de caracteres especiales sin invocar su significado especial. Esto choca con el uso de Python del mismo carácter para el mismo propósito en cadenas literales; por ejemplo, para hacer coincidir una barra invertida literal, es posible que tenga que escribir '\\\\'como cadena de patrón, porque la expresión regular debe ser \\, y cada barra invertida debe expresarse como \\dentro de una cadena literal de Python normal. Además, tenga en cuenta que cualquier secuencia de escape no válida en el uso de Python de la barra invertida en los literales de cadena ahora genera un DeprecationWarning y en el futuro se convertirá en un SyntaxError. Este comportamiento ocurrirá incluso si es una secuencia de escape válida para una expresión regular.

La solución es usar la notación de cadenas sin procesar de Python para patrones de expresiones regulares; las barras invertidas no se manejan de ninguna manera especial en un literal de cadena con el prefijo 'r'. También lo r"\n"es una cadena de dos caracteres que contiene '\'y 'n', mientras que "\n"es una cadena de un carácter que contiene una nueva línea. Por lo general, los patrones se expresarán en código Python utilizando esta notación de cadena sin procesar.

Es importante tener en cuenta que la mayoría de las operaciones con expresiones regulares están disponibles como funciones y métodos a nivel de módulo en expresiones regulares compiladas . Las funciones son atajos que no requieren que primero compiles un objeto regex, pero pierden algunos parámetros de ajuste.

### subprocess
El subproceso en Python es un módulo que se utiliza para ejecutar nuevos códigos y aplicaciones mediante la creación de nuevos procesos. Le permite iniciar nuevas aplicaciones directamente desde el programa de Python que está escribiendo actualmente. Entonces, si desea ejecutar programas externos desde un repositorio de git o códigos de programas C o C++ , puede usar el subproceso en Python. También puede obtener códigos de salida y canalizaciones de entrada, salida o error utilizando el subproceso en Python . 

## Desarrollo
### Explicacion del codigo


## Conclusion

## Bibliografias
