import sys

f = open(sys.argv[1], 'r')
ff = open(sys.argv[2], 'r')
res = open('out.txt', 'w')

for line in f:
    if line == ff.readline():
        res.write('1\n')
    else:
        res.write('0\n')
