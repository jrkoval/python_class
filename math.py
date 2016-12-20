def mean(x):
    sum=0
    for num in x:
        sum = sum + num
    return(sum)/len(x)

def median(x):
    x.sort()
    if len(x)%2 == 0:
        print(x[int(len(x)/2)])
        print("minus 1" )
        print(x[int(len(x)/2) -1])
        res = ((x[int(len(x)/2)] + x[int(len(x)/2) -1]))/2
        return(res)
    else:
        return(x[int(len(x)/2) + 1])

print(mean([1,2,3,4,5]))
print(median([1,2,3,4,5,6,7,8,9,10]))
