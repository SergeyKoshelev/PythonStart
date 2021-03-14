import sys

count = int(sys.argv[1])

for i in range(count):
    print(" " * (count - i - 1) + "#" * (i + 1))