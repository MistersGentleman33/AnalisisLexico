import sys
import re


def recognize_variables(file):
    expression = re.compile("(int [a-zA-Z]+ = [0-9]+|float [a-zA-Z]+ = [0-9]+.[0-9]+"
                            "|double [a-zA-Z]+ = [0-9]+.[0-9]+|char [a-zA-Z]+ = [\"|\'][a-zA-Z]+[\"|\'])")

    print(expression.findall(file))


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
    file = read_file(input_text)
    print("Esta es una prueba de lectura de archivo: \n {} \n".format(file))
    recognize_variables(file)


try:
    if __name__ == "__main__":
        main()

except ValueError:
    print("\nInvalid Arguments: %s" % sys.argv[1])

except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <code.c> " + " <symbols_table> " + "<errors>\n")
