def op1(num):
    return num - 5

def op2(num):
    return num + 8

def op3(num):
    return num * -1

def op4(num):
    return num / 7

def test_path(f, x):
    y = x
    for i in range(len(f)):
        y = o[f[i]](y)
    print(y)
    return y

m = 5
n = 4
o = [op1, op2, op3, op4]
g = 3
x = 34
y = None
p = []
l = m - 1

current = [0, 0, 0, 0, 0]

while l >= 0 and current[l] < n:
    if current[l] < n:
        p.append(current.copy())
        current[l] = current[l] + 1
    else:
        for i in range(m):
            if (l + i) < m:
                current[l + i]

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


print(print(len(p), 'paths generated total'))

for i in range(len(p)):
    if test_path(p[i], x) == g:
        print(p[i], 'is the correct path')
        break
