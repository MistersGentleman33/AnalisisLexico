import sys
import re


def write_table(expression_int, expression_float, expression_double, expression_char):
    passs


def recognize_variables(file):
    # Expresiones regulares para cada variable

    expression_int = re.compile("int [a-zA-Z]+ = [0-9]+|, [a-zA-Z]+ = [0-9]+")
    expression_float = re.compile("float [a-zA-Z]+ = [0-9]+.[0-9]+|, [a-zA-Z]+ = [0-9]+.[0-9]+")
    expression_double = re.compile("double [a-zA-Z]+ = [0-9]+.[0-9]+|, [a-zA-Z] = [0-9]+.[0-9]+")
    expression_char = re.compile("char [a-zA-Z]+\[[0-9]+\] = [\"|\'][a-zA-Z]+[\"|\']"
                                 "|, [a-zA-Z]+\[[0-9]+\] = [\"|\'][a-zA-Z]+[\"\']")

    write_table(expression_int, expression_float, expression_double, expression_char)


def read_file(input_text):  # Lectura del archivo, cada linea la guarda en una lista
    with open(input_text) as archivo:
        archivo = archivo.read()

    return archivo


def main():
    # Variables Flags
    input_text = sys.argv[1]
    # symbols_table = sys.argv[2]
    # errors = sys.argv[3]

    # Functions
    file = read_file(input_text) # Variable que contiene el archivo en string
    print("Esta es una prueba de lectura de archivo: \n {} \n".format(file))
    recognize_variables(file)


try:
    if __name__ == "__main__":
        main()

except ValueError:
    print("\nInvalid Arguments: %s" % sys.argv[1])

except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <code.c> " + " <symbols_table> " + "<errors>\n")
