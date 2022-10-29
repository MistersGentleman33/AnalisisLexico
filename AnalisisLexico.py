import sys


def leer_archivo(archivo_entrada):  # Lectura del archivo, cada linea la guarda en una lista
    with open(archivo_entrada) as archivo:
        archivo = archivo.readlines()

    return archivo


def main():
    # Variables Flags
    input_text = sys.argv[1]
    #symbols_table = sys.argv[2]
    #errors = sys.argv[3]

    file = leer_archivo(input_text)
    print("Esta es una prueba de lectura de archivo: \n {} \n".format(file))

    for i in file:
        print(i)



try:
    if __name__ == "__main__":
        main()

except ValueError:
    print("\nInvalid Arguments: %s" % sys.argv[1])

except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <code.c> " + " <symbols_table> " + "<errors>\n")


