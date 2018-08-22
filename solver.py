def reverse(o1):
    '''This function reverses an integer and returns it'''
    result = ''
    while o1 > 0:
        result += o1 // 10
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
n = int(input("# of Operators: "))
# o = [op1, op2, op3, op4]
o = []
g = int(input("Goal: "))
x = int(input("Starting Number: "))
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
    if l == m - 1 and current[l] < n:
        p.append(current.copy())
        print(current)
        current[l] = current[l] + 1
    else:
        print(n)
        for i in range(m):
            if current[i + 1] >= n:
                current[i] = current[i] + 1
                for j in range(i + 1, m):
                    current[j] = 0
                break
            


print(print(len(p), 'paths generated total'))

for i in range(len(p)):
    if test_path(p[i], x) == g:
        print(p[i], 'is the correct path')
        break
