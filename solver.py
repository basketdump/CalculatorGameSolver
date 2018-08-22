def reverse(o1):
    '''This function reverses an integer and returns it'''
    result = ''
    if o1 == 0:
        return 0
    else:
        while o1 > 0:
            result += str(o1 % 10)
            o1 = o1 // 10
        return int(result)

def test_path(f, x):
    '''This function interprets and evaluates an operation'''
    y = x
    for i in range(len(f)):
        if o[f[i]][0] == '+':
            y = y + int(o[f[i]][1])
        elif o[f[i]][0] == '*':
            y = y * int(o[f[i]][1])
        elif o[f[i]][0] == '-':
            y = y - int(o[f[i]][1])
        elif o[f[i]][0] == '/':
            y = y / int(o[f[i]][1])
        elif o[f[i]][0] == 'i':
            y = int(str(y) + o[f[i]][1])
        elif o[f[i]][0] == 'f':
            y = y * -1
        elif o[f[i]][0] == 'r':
            y = reverse(y)
    print(y)
    return y

# Setup variables
m = int(input("# of Moves: "))
g = int(input("Goal: "))
x = int(input("Starting Number: "))
n = int(input("# of Operators: "))
# o = [op1, op2, op3, op4]
o = []
y = None
p = []
l = m - 1


current = []

# Setup current to have # of moves
for i in range(m):
    current.append(0)

# Input operators
for i in range(n):
    operator = input("Operator: ")
    o.append(operator.split())

# Generate paths
while current[0] < n:
    # print(p)
    p.append(current.copy())
    ptr = m - 1
    current[ptr] = current[ptr] + 1
    while (current[ptr] >= n):
        if (ptr > 0):
            current[ptr] = 0
            current[ptr - 1] = current[ptr-1] + 1
        else:
            break
        ptr = ptr - 1
            


print(print(len(p), 'paths generated total'))

for i in range(len(p)):
    if test_path(p[i], x) == g:
        print(p[i], 'is the correct path')
        break
