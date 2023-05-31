#case1
while True:
    c = input()
    stack = []
    if c == '.':
        break
    for i in c:
        if i == '.':
            break
        if i in '[(' :
            stack.append(i)
        elif i == ']' :
            if stack and stack[-1] == '[' :
                stack.pop()
            else:
                stack.append('F')
        elif i == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else:
                stack.append('F')
    if not stack:
        print('yes')
    else :
        print('no')

#case2
pairs = {')': '(', ']': '['}
while True:
    c = input()
    if c == '.':
        break
    stack = []
    for i in c:
        if i in '([':
            stack.append(i)
        elif i in ')]':
            if not stack or stack[-1] != pairs[i]:
                print('no')
                break
            stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')