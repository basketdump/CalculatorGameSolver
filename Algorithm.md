# Calculator Game Algorithm

### Specifications of Game
- There is only one correct path
- Available operators, number of moves, and starting numbers change with each new game
- Not every operator is needed in each game
- $f(m,n) = n^{m}$ is the number of possible paths of operations

### Overarching Ideas
- Bruteforce operations
- Do not evaluate anymore once we reach goal
- Operators need to be well defined, they are not *typical* math operators
    - Multiplication *Ex: 3x meaning 3 * current number*
    - Remove digit *Ex: << meaning truncate the last digit of the current number*
    - Insert digit *Ex: 5 meaning append 5 to the end of the current number*

### Algorithm Steps
- Let *m* be the max number of moves
- Let *n* be the number of operators available per move
- Let *o* be the available operators
- Let *g* be the goal
- Let *x* be the starting number
- Let *y* be the result
- Let *p* be the possible paths of operations
    - Length of *p* is $n^{m}$
    - Length of *p[i]* is *m*

1. Generate all possible paths of operations
    1. *p* = [[*p1*], [*p2*], [*p3*], [*...*]]
2. Loop & execute each *p[i]* against *x* until *y* == *g*
3. Display *p[i]*