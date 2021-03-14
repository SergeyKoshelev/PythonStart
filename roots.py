import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

descr = b ** 2 - 4 * a * c;
x1 = int((-b - (descr ** 0.5).real)/2/a);
x2 = int((-b + (descr ** 0.5).real)/2/a);
print(x1, x2, sep='\n');
