infix = 'a*b+c'
ranks = {'+':0, '-':0, '*':1, '/':1}
stack = []
postfix = ''

for token in infix:
    if token in ranks:
        if stack:
            while True:
                if ranks[token] < ranks[stack[-1]]:
                    postfix = postfix + stack.pop()
                    if not stack:
                        stack.append(token)
                        break
                else:
                    stack.append(token)
                    break
        else:
                stack.append(token)
    else:
            postfix = postfix + token
while stack:
    postfix = postfix + stack.pop()
print(postfix)
