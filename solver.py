def reverse(o1):
    result = ''
    while o1 > 0:
        result += o1 // 10
        o1 = o1 // 10
    return int(result)

def test_path(f, x):
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
        elif o[f[i]][0] == 'f':
            y = y * -1
        elif o[f[i]][0] == 'r':
            y = reverse(y)
    print(y)
    return y

m = 5
n = 5
# o = [op1, op2, op3, op4]
o = []
g = 4
x = 25
y = None # + 5 / 4 * 3 f + 1
p = []
l = m - 1


current = [0, 0, 0, 0, 0]

for i in range(n):
    operator = input("Operator: ")
    o.append(operator.split())

while l >= 0 and current[l] < n:
    if current[l] < n:
        p.append(current.copy())
        current[l] = current[l] + 1
    else:
        for i in range(m):
            if (l + i) < m:
                current[l + i]
'''
while current[0] < n:
    while current[1] < n:
        while current[2] < n:
            while current[3] < n:
                while current[4] < n:
                    p.append(current.copy())
                    current[4] = current[4] + 1
                current[3] = current[3] + 1
                current[4] = 0
            current[2] = current[2] + 1
            current[3] = 0
            current[4] = 0
        current[1] = current[1] + 1
        current[2] = 0
        current[3] = 0
        current[4] = 0
    current[0] = current[0] + 1
    current[1] = 0
    current[2] = 0
    current[3] = 0
    current[4] = 0
'''
print(print(len(p), 'paths generated total'))

for i in range(len(p)):
    if test_path(p[i], x) == g:
        print(p[i], 'is the correct path')
        break
