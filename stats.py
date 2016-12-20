def mean(x):
    sum=0
    for num in x:
        sum = sum + num
    return(sum)/len(x)

def median(x):
    x.sort()
    if len(x)%2 == 0:
        #print(x[int(len(x)/2)])
        #print("minus 1" )
        #print([int(len(x)/2) -1])
        res = ((x[int(len(x)/2)] + x[int(len(x)/2) -1]))/2
        return(res)
    else:
        return(x[int(len(x)/2) + 1])
    
def mode(x1):
    freq = {}
    finals = []
    for x in x1:
        if x in freq:
            freq[x] = freq[x]+1
        else:
            freq[x] = 1
    #print(str(freq))
    for element,rank in freq.items():
        finals.append((rank,element))
    finals.sort()
    return(finals[-1][-1])
