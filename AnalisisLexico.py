import sys


def leer_archivo(archivo_entrada):  # Lectura del archivo, cada linea la guarda en una lista
    with open(archivo_entrada) as archivo:
        archivo = archivo.readlines()

    return archivo


def main():
    # Variables Flags
    archivo_entrada = sys.argv[1]
    #tabla_simbolos = sys.argv[2]
    #archivo_errores = sys.argv[3]

    archivo = leer_archivo(archivo_entrada)
    print("Esta es una prueba de lectura de archivo: \n {} \n".format(archivo))

    for i in archivo:
        print(i)



try:
    if __name__ == "__main__":
        main()

except ValueError:
    print("\nArgumentos invalidos: %s" % sys.argv[1])

except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <nombre_archivo.c> " + " <nombre_tabla_simbolos> " + "<nombre_archivo_errores>\n")


