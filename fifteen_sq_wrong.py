# https://en.wikipedia.org/wiki/15_puzzle
# This is inefficient/wrong solution using the backtracking or depth first approach
# It leads to the stack overflow.

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

solution = range(1,16)
solution.append(0)

# find
def find_blank(mat):
    for i in range(len(mat)):
        if mat[i] == 0:
            return i

def hash(mat):
    return "_".join(map(lambda x: str(x), mat))

def toidx(i, j):
    return i*4 + j

def toij(i):
    return (i/4, i%4)

def copy_arr(mat):
    state = []
    for i in mat:
        state.append(i)
    return state

def add_tu(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

# Moves up
def step(mat, idx, di):
    if mat[idx] != 0:
        print("Ouch! mat at idx is not 0")
        return -1;
    (i, j) = toij(idx)
    print("di: ", str(di))
    print("(i,j) ", str((i,j)))
    (ii, jj) = add_tu((i, j), di)
    if ii < 0 or jj < 0 or ii > 3 or jj > 3:
        return (None, False, -1)
    state = copy_arr(mat)
    newidx = toidx(ii, jj)
    state[idx] = state[newidx]
    state[newidx] = 0
    return (state, True, newidx)

# mat is an array of 16 numbers. the 0 represents blank
# it should print steps of the movement of space: Up, Down, Left, Right
def solve_slow(mat, idx, visited, path = []):
    print("=== Problem ===")
    print_mat(mat)
    print("-------------")

    global LEFT, RIGHT, UP, DOWN, solution
    if solution == mat:
        # print(path)
        return path;
    #i = find_blank(mat)    
    for di in [LEFT, RIGHT, UP, DOWN]:
        (state, can_move, newidx) = step(mat, idx, di)
        if not can_move:
            continue
        state_str = hash(state)
        if not state_str in visited:
            visited[state_str] = True
            path.append(di)
            soln_path = solve(state, newidx, visited, path)
            if soln_path:
                return soln_path
            path.pop()
    return None

import sys
def print_mat(mat):
    for i in range(4):
        for j in range(4):
            idx = i*4 + j
            sys.stdout.write(str(mat[idx]) + ' ')
        print('')

def solve_entry(mat):
    visited = {}
    visited[hash(mat)] = True
    idx = find_blank(mat)
    soln_path = solve(mat, idx, visited)

def to_str(di):
    if di == LEFT:
        return "LEFT"
    if di == RIGHT:
        return "RIGHT"
    if di == UP:
        return "UP"
    if di == DOWN:
        return "DOWN"
    return " ERR "


def main():
    mat_str = "10 5 4 3 0 2 11 6 1 7 15 12 9 13 8 14"
    mat = map(lambda x: int(x), mat_str.split())
   

    soln_path = solve_entry(mat)
    print(" == Solution === ")
    state = mat
    idx = find_blank(mat)
    for di in soln_path:
        (state, can_move, idx) = step(state, idx, di)
        print_mat(state)
        print("-------------")

if __name__ == '__main__':
    main()
