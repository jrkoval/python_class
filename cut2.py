import argparse
import sys
import re
def validateExpression(fields):
    pat = '^\d+(,\d+)*$'
    if re.match(pat,fields):
        return True
    else:
        return False
def validIndexes(fields,fields_length):
    indexes = []
    fields = fields.split(',')
    for field in fields:
        if int(field) >= 0 and int(field) < fields_length:
            indexes.append(int(field))
    indexes.sort()
    return indexes

parser = argparse.ArgumentParser()
parser.add_argument('-d','-delim',type=str,dest='delim',required=True)
parser.add_argument('-f','-fields',type=str,dest='fields',default = 'all')
parser.add_argument('fname',nargs = "?")
args = parser.parse_args()
delim = args.delim
fields = args.fields
fname = args.fname
if fname:
    fobj = open(fname,"r")
else:
    fobj = sys.stdin.readlines()
#fields -->  -f 1,2,7
if validateExpression(fields):
    for line in fobj:
        components = line.split(delim)
        indexes = validIndexes(fields,len(components))
        for index in indexes:
            print(components[index],end=" ")
        print()
else:
    for line in fobj:
        print(line,end="")
    print()
