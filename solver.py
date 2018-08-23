# Generate paths
def generate_paths(length, height):
    '''Generates a 2-dimensional array of all possible paths number of steps being length and the type of steps on each step being height'''
    # Result is an array of all paths (which are also arrays of steps)
    result = []
    current = []
    # Setup current path to initialize all steps as 0
    for i in range(length):
        current.append(0)
    
    # This code generates the paths from incrementing the last digit and carrying.
    # ex: length = 3, height = 3
    #   000, 001, 002, 010, 011, 012, 020, 021, 022, 100, etc...
    while current[0] < height:
        result.append(current.copy())
        ptr = length - 1
        current[ptr] = current[ptr] + 1
        while (current[ptr] >= height):
            if (ptr > 0):
                current[ptr] = 0
                current[ptr - 1] = current[ptr-1] + 1
            else:
                break
            ptr = ptr - 1

    return result

def reverse(o1):
    '''This function reverses a number and returns it'''

    # Track if negative. Don't want situation of -123
    # returning 321-
    negative = False
    if (o1 < 0):
        negative = True
        o1 = o1 * -1

    # Avoid ex: 10.0 returning as 0.01
    if (o1.is_integer()):
        o1 = int(o1)

    # This part reverses the number as a string
    o1 = str(o1)
    result = ''
    for i in range(len(o1)):
        result = result + o1[len(o1) - (i + 1)]
    
    # Return number back to float also negative if need be
    result = float(result)
    if negative:
        return result * -1
    else:
        return result

def insert(o1, o2):
    ''' Inserts o2 as the last significant digit of o1'''
    # Converts whole numbers to avoid 1.0 insert 5 being 1.05
    # instead of correctly returning 15.0
    if (o1.is_integer()):
        o1 = int(o1)
    
    return float(str(o1) + str(o2))

def left_shift(o1):
    '''Shifts o1 to the left by 1'''
    if o1.is_integer():
        # Avoids 0 becoming int('') error
        return float(int(o1) // 10)
    else:
        # Returns non-int floats by leaving off last digit
        # -17.1 returns as -17.0 (-17. == -17.0)
        return float(str(o1)[:-1])


def test_path(operations, f, x):
    '''This function interprets and evaluates an operation'''
    y = x
    for i in range(len(f)):
        # Define our operator
        operator = operations[f[i]][0]
        # Some operators unary operators, so we need to see
        # if that's the case before trying to access an operand
        # that doesn't exist
        if (len(operations[f[i]]) == 2):
            operand = float(operations[f[i]][1])
        # operand = float(o[f[i]][1])
        if operator == '+':
            y = y + operand
        elif operator == '*':
            y = y * operand
        elif operator == '-':
            y = y - operand
        elif operator == '/':
            y = y / operand
        elif operator == 'i':
            y = insert(y, operand)
        elif operator == 'f':
            y = y * -1
        elif operator == 'r':
            y = reverse(y)
        elif operator == '<':
            y = left_shift(y)
    return y

def main():
    # Setup variables
    moves = int(input("# of Moves: "))
    goal = float(input("Goal: "))
    start = float(input("Starting Number: "))
    num_of_operators = int(input("# of Operators: "))
    # o = [op1, op2, op3, op4]
    operations = []
    paths = []

    # Input operators
    for i in range(num_of_operators):
        operator = input("Operator: ")
        operations.append(operator.split())

    paths = generate_paths(moves, num_of_operators)

    print(print(len(paths), 'paths generated total'))

    for i in range(len(paths)):
        if test_path(operations, paths[i], float(start)) == goal:
            print(paths[i], 'is the correct path')
            break

main()
