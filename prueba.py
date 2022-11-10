import re
import subprocess

def read_file():  # Lectura del archivo, cada linea la guarda en una lista
    with open("codigo2.c") as archivo:
        archivo = archivo.read()

    return archivo

def pawk(args):
    echo = subprocess.run(["echo", args], check=True, capture_output=True)
    awk = subprocess.run(["python3", "pawk/pawk.py", "-F", " ", "f[0]"], input=echo.stdout, capture_output=True)
    awk_output = awk.stdout.decode("utf-8").strip()
    return awk_output


def main():
    file = read_file()
    print(file)
    expression_int = re.compile(
        r'int \w+, \w.+;|int \w = \w.;+|int \w+, \w+;|(int \w+ = [0-9]+|, \w+ = [0-9]+)| int \w+ = \w+\(\w+\);')
    expression_float = re.compile("float \w+ = [0-9]+.[0-9]+|, [a-zA-Z]+ = [0-9]+.[0-9]+")
    expression_double = re.compile("double \w+ = [0-9]+.[0-9]+|, [a-zA-Z] = [0-9]+.[0-9]+")
    expression_char = re.compile(
        r'char \*\w+ = (\"|\')\w+(\"|\');')

    print(expression_int.findall(file))
    print(expression_char.findall(file))


if __name__ == "__main__":
    main()
