import re


def expression():
    expression = re.compile("(int [a-zA-Z]+ = [0-9]+|float [a-zA-Z]+ = [0-9]+.[0-9]+"
                            "|double [a-zA-Z]+ = [0-9]+.[0-9]+|char [a-zA-Z]+ = [\"|\'][a-zA-Z]+[\"|\'])")
    text = """ asdasd s"""
    text2 = "asdasdasd"
    expression2 = re.compile("(int [a-zA-Z]+ = [0-9]+|float [a-zA-Z]+ = [0-9]+.[0-9]+"
                             "|double [a-zA-Z]+ = [0-9]+.[0-9]+|char [a-zA-Z]+ = [\"|\'][a-zA-Z]+[\"|\'])")

    lista = expression.findall(text)
    lista2 = expression2.findall(text)

    if bool(l:
        print("esta vacia")
    else:
        print("No esta vaia1")
        print(lista)


def main():
    expression()


#    file(expression)


if __name__ == "__main__":
    main()
