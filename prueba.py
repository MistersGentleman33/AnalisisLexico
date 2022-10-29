import re

expression = re.compile("int [a-zA-Z]+ = [0-9]+")
text = """Hola hermano como has estado
int asd = 10
asdasdasd = 12e12e
int a = 10"""

print(expression.findall(text))
