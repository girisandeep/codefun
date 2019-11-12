#https://en.wikipedia.org/wiki/15_puzzle

def find_blank(mat):
    for i in range(len(mat)):
        if mat[i] == 0:
            return i

class Node(object):
    def __init__(self, state, zero_idx, path = []):
        self.state = state
        self.path = path
        self.cost = calculate_distace(state)
        self.zero_idx = zero_idx

ideal_idx = [(3, 3)]

for i in range(1, 16):
    v = i - 1
    ideal_idx.append(( v/4, v%4))

import math

def abs(x):
    if x < 0:
        return -x
    return x

def abs_dist(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

def calculate_distace(mat):
    global ideal_idx
    # print(ideal_idx)
    cost = 0
    for idx in range(len(mat)):
        current_loc = (idx / 4, idx % 4)
        ideal_loc = ideal_idx[mat[idx]]
        cost += abs_dist(current_loc, ideal_loc)
        # print("%s: current location: %s, ideal_loc: %s, cost: %s" % (mat[idx], current_loc, ideal_loc, cost))
    return cost


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
        print("Ouch! mat at idx:%s is not 0" % (idx))
        return -1;
    (i, j) = toij(idx)
    # print("di: ", str(di))
    # print("(i,j) ", str((i,j)))
    (ii, jj) = add_tu((i, j), di)
    if ii < 0 or jj < 0 or ii > 3 or jj > 3:
        return (None, False, -1)
    state = copy_arr(mat)
    newidx = toidx(ii, jj)
    state[idx] = state[newidx]
    state[newidx] = 0
    return (state, True, newidx)

import sys
def print_mat(mat):
    for i in range(4):
        for j in range(4):
            idx = i*4 + j
            sys.stdout.write(str(mat[idx]) + ' ')
        print('')

def hash(mat):
    return "_".join(map(lambda x: str(x), mat))

from heapq import *

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def solve(mat):
    idx = find_blank(mat)
    n = Node(mat, idx)
    queue = []
    heappush(queue, ((n.cost,0), n))
    is_visited = {}
    while queue:
        (cost, current) = heappop(queue)
        idx = current.zero_idx
        if cost[0] == 0:
            # print("==== Found ====")
            # print_mat(current.state)
            # print("Path: ", current.path)
            return current.path
        # print_mat(current.state)
        # print("Path: ", current.path)
        for di in [LEFT, RIGHT, UP, DOWN]:
            (state, can_move, newidx) = step(current.state, idx, di)
            # print("state: %s, can_move: %s, newidx: %s" % (state, can_move, newidx))
            if can_move:
                if hash(state) not in is_visited:
                    new_path = current.path + [di]
                    n = Node(state, newidx, new_path)
                    heappush(queue, ((n.cost,len(n.path)), n))
        is_visited[hash(current.state)] = True
    return []

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

    print(" == Problem === ")
    print_mat(mat)
    print("-------------")

    # print(calculate_distace(mat))
    # mat_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"
    # mat = map(lambda x: int(x), mat_str.split())
    # print(calculate_distace(mat))

 
    soln_path = solve(mat)
    print(" == Solution === ")
    state = mat
    idx = find_blank(mat)
    print("Total Steps: ", len(soln_path))
    for di in soln_path:
        print(to_str(di), di)
        (state, can_move, idx) = step(state, idx, di)
        print_mat(state)
        print("-------------")

if __name__ == '__main__':
    main()

