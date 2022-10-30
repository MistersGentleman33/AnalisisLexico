import re

expression = re.compile("(int [a-zA-Z]+ = [0-9]+|float [a-zA-Z]+ = [0-9]+.[0-9]+"
                        "|double [a-zA-Z]+ = [0-9]+.[0-9]+|char [a-zA-Z]+ = [\"|\'][a-zA-Z]+[\"|\'])")
text = """Hola hermano como has estado
int asd = 10
asdasdasd = 12e12e
int a = 10 
float asd = 102.123 asdas e10rj1209eu1092je 
char asd = 'racquetball' """
print(expression.findall(text))
