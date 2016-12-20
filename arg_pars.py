import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', '-principal', type=int, dest='principal', default=120, help="principal amount")
parser.add_argument('-r', '-rate', type=int, dest='rate', default=2, help="rate amount")
parser.add_argument('-t', '-time', type=int, dest='time', default=3, help="time amount")

args = parser.parse_args()

print(args.principal, end=" ")
print(args.rate, end=" ")
print(args.time, end=" ")
print()
