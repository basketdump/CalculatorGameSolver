# Calculator Game Algorithm

### Specifications of Game
- Let *m* be the max number of moves
- Let *n* be the number of operators available per move
- Let *o* be the available operators
- Let *g* be the goal
- Let *x* be the starting number
- Let *y* be the result
- Let *p* be the possible paths of operations
    - Length of *p* is *m*
- Let $f(m,n) = n^{m+1}$ be the number of paths

### Overarching Ideas
- Work backwards from the goal
- Bruteforce operations to starting number
- Stop when *y* == *g*

### Algorithm Steps
1. Generate all possible paths of operations
    1. *p* = [[*p1*], [*p2*], [*p3*], [*...*]]
2. Loop & execute each *p[i]* against *x* until *y* == *g*
3. Display *p[i]*