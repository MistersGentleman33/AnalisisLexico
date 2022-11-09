import re
import subprocess


def pawk(args):
    echo = subprocess.run(["echo", args], check=True, capture_output=True)
    awk = subprocess.run(["python3", "pawk/pawk.py", "-F", " ", "f[0]"], input=echo.stdout, capture_output=True)
    awk_output = awk.stdout.decode("utf-8").strip()
    return awk_output


def expression():
    text = """int a = 10, b = 20"""
    ex = re.compile(r"int \w+ = [0-9]+|, [a-zA-Z]+ = [0-9]+")
    output = ex.findall(text)

    print(output)

    for i in output:
        awk_output = pawk(i)
        print(awk_output)


def main():
    expression()


#    file(expression)


if __name__ == "__main__":
    main()