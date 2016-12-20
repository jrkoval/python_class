x1 = [10,20,13,10,10,45,20]
def mode(x):
    freq = {}
    finals = []
    for x in x1:
        if x in freq:
            freq[x] = freq[x]+1
        else:
            freq[x] = 1
    print(str(freq))
    for element,rank in freq.items():
        finals.append((rank,element))
    finals.sort()
    print(finals[-1][-1])
