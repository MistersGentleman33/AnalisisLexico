import sys
import re
import subprocess


def recognize_functions(file):  # Funcion para reconocer funciones void e int
    expression_F_int = re.compile(r"int \w+\(+\)|int \w+\(.+\)")
    expression_F_void = re.compile(r"void \w+\(+\)|void \w+\(.+\)")

    return expression_F_int.findall(file), expression_F_void.findall(file)


def pawk(args, i):
    i = str(i)
    position = "f[" + i + "]"
    echo = subprocess.run(["echo", args], check=True, capture_output=True)
    awk = subprocess.run(["python3", "pawk/pawk.py", "-F", " ", position], input=echo.stdout, capture_output=True)
    awk_output = awk.stdout.decode("utf-8").strip()


def write_table(list_int, list_float, list_double, list_char, table_name):
    with open(table_name, "w") as file:
        file.write("\tComponente Lexico\tLexema\tValor\n")
    '''
    for i in list_int:
        spaces = i.count(" ")
        for x in range(spaces + 1):
            awk_output = pawk(i, x)
            #print(awk_output)'''


def recognize_variables(file):  # Expresiones regulares para cada variable

    expression_int = re.compile(r"(int \w+ = [0-9]+|, [a-zA-Z]+ = [0-9]+)|(int \w+ = \w[^ ]+)|(int \w+, \w.+;)")
    expression_float = re.compile("float \w+ = [0-9]+.[0-9]+|, [a-zA-Z]+ = [0-9]+.[0-9]+")
    expression_double = re.compile("double \w+ = [0-9]+.[0-9]+|, [a-zA-Z] = [0-9]+.[0-9]+")
    expression_char = re.compile("char \*\w+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"|\']"
                                 "|, [a-zA-Z]+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"\']|char "
                                 "\w+\[[0-9]+] = [\"|\'][a-zA-Z]+[\"|\']"
                                 "")

    expression_int = expression_int.findall(file)
    expression_float = expression_float.findall(file)
    expression_double = expression_double.findall(file)
    expression_char = expression_char.findall(file)

    expression_int.remove(" ")
    expression_char.remove(" ")
    expression_double.remove(" ")
    expression_float.remove(" ")
    print(expression_int)
    return expression_int, expression_float, expression_double, expression_char

def read_file(input_text):  # Lectura del archivo, cada linea la guarda en una lista
    with open(input_text) as archivo:
        archivo = archivo.read()

    return archivo


def main():
    # Variables Flags
    input_text = sys.argv[1]
    table_name = sys.argv[2]
    # errors = sys.argv[3]

    # Functions

    file = read_file(input_text)  # Variable que contiene el archivo en string

    # print("Esta es una prueba de lectura de archivo: \n {} \n".format(file))

    list_int, list_float, list_double, list_char = recognize_variables(file)  # Variables con listas que contienen
    # los tokens encontrados para tipos de variables

    '''Variables que contienen los tokens para las funciones void e int'''
    list_f_int, list_f_void = recognize_functions(file)
    # print(list_f_int, list_f_void)

    print(list_int, list_float, list_double, list_char)
    write_table(list_int, list_float, list_double, list_char, table_name)  # Funcion que escribe la tabla de simbolos


try:
    if __name__ == "__main__":
        main()

except ValueError:
    print("\n[!] Use: python3 " + sys.argv[0] + " <code.c> " + " <name_table>.txt " + "<errors>.txt\n")
