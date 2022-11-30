from collections import deque


def brackets(line):
    dq = deque()
    for el in line:
        if el == '(':
            dq.append('(')
        try:
            if el == ')':
                dq.pop()
        except Exception as exc:
            print('bad brackets')
            return False
    if len(dq) == 0:
        return True
    else:
        return False
        

print(brackets('(()())'))
print(brackets(''))
print(brackets('(()()))'))
print(brackets('('))
print(brackets(')'))
