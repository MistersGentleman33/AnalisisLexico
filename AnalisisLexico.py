import sys

try:
    if __name__ == "__main__":
        archivo_entrada = sys.argv[1]
        tabla_simbolos = sys.argv[2]
        archivo_errores = sys.argv[3]

        print("\n {} {} {} ".format(archivo_entrada, tabla_simbolos, archivo_errores))

except ValueError:
    print("\nArgumentos invalidos: %s" % sys.argv[1])

except:
    print("\n[!] Use: python3 " + sys.argv[0] + " <nombre_archivo.c> " + " <nombre_tabla_simbolos> " + "<nombre_archivo_errores>\n")

