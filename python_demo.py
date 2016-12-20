import sys

print(sys.argv)

args = sys.args[1:]

p = int(args[0])
r = int(args[1])
t = int(args[2])
print(p*r*t/100)
