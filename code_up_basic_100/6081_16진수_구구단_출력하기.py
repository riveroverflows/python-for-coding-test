from sys import stdin, stdout

_input = stdin.readline
_print = stdout.write

n = int(_input(), 16)
for i in range(1, int("F", 16) + 1):
    _print("%X" % n + "*%X" % i + "=%X" % (n * i) + "\n")
