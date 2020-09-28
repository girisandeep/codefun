from random import randint
from collections import deque
from copy import deepcopy

class Puzzle():
    def createt(self, num, size=4):
        return [num for i in range(4)]

    def create_sol(self, num=11):
        tt = []
        for i in range(num):
            tt.append(self.createt(i+1))
        for i in range(2):
            tt.append([])
        return tt

    

    def solve(self):
        def tostr(pzl):
            pzl = sorted(pzl)
            result = []
            for t in pzl:
                s = ''.join(map(str, t))
                s += '0'*(self.max - len(t))
                result.append(s)
            return ''.join(result)
        def canmove(src, dest):
            if len(src) == 0 or len(dest) == self.max:
                print("Source empty or dest full")
                return False
            if len(dest) == 0 or src[-1] == dest[-1]:
                return True
            print("Source and Dest not same")
            return False

        visited = {}
        q = deque([(self.puzzle, [])])
        while q:
            state,steps = q.popleft()
            print("==============Picking next==========")
            self.pprint(pzl=state)

            state_str = tostr(state)
            print("state_str: " + state_str)

            if state_str not in visited:
                visited[state_str] = True
            else:
                print("Already Visied")
                continue
            
            if self.is_solved(state):
                print(steps)
                return steps
            
            for i in range(len(state)):
                for j in range(len(state)):
                    if i == j:
                        continue
                    print("Trying i:%d, j:%d" %(i, j))
                    if canmove(state[i], state[j]):
                        print("Moving!")
                        newstate = deepcopy(state)
                        t = newstate[i].pop()
                        newstate[j].append(t)
                        self.pprint(pzl=newstate)
                        newsteps = deepcopy(steps)
                        newsteps.append((i, j))
                        q.append((newstate, newsteps))
        print("Exhausted.")
        return []

    '''
    The value of num of tubes will be ignore if puzzle is provided
    '''
    def __init__(self, puzzle=None, num=11):
        if puzzle:
            self.puzzle = puzzle
        else:
            self.puzzle = self.create_sol(num)
        self.max = 4
        self.tube_count = num
    
    '''
    return how many times it was successful
    '''
    def randommove(self, times=1):
        success = 0
        for _ in range(times):
            src = randint(0, self.tube_count+2 - 1)
            dest = randint(0, self.tube_count+2 - 1)
            if self.swap(src, dest):
                success += 1
        return success

    

    def move(self, src, dest):
        print("Swapping src:%d dest:%d " % (src, dest))
        src = self.puzzle[src]
        dest = self.puzzle[dest]
        if len(src) == 0 or len(dest) == self.max:
            print("Either the source is emptry or dest is full")
            return False
        if len(dest) == 0 or src[-1] == dest[-1]:
            v = src.pop()
            dest.append(v)
            return True
        print("The destination doesn't have the same ball as source")
        return False

    def pprint(self, pzl=None):
        if not pzl:
            pzl = self.puzzle
        for j in range(3,-1,-1):
            line = ""
            for i in range(len(pzl)):
                t = pzl[i]
                if len(t) > j:
                    line += str(t[j]) + "\t"
                else:
                    line += "_" + "\t"
            print(line)
        print("="*10)

    def is_solved(self, pzl=None):
        if not pzl:
            pzl = self.puzzle
        empty = 0
        for tube in pzl:
            if len(tube) == 0:
                empty += 1
                continue
            first = tube[0]
            for b in tube[1:]:
                if b != first:
                    return False
        if empty == 2:
            return True

def main():

    pzl1 = [
        [1,1,2,2],
        [1,3,2,3],
        [3,1,2,3],
        [],
        []
    ]
    pzl = [
        [1,2,3,4],
        [5,6,7,8],
        [3,9,8,10],
        [11, 3, 11, 9],
        [7, 6, 9, 10],
        [11, 5, 8, 1],
        [2, 2, 4, 3],
        [8, 5, 1, 9],
        [1, 6, 11, 4],
        [10, 4, 7, 7],
        [10, 6, 2, 5],
        [],
        []
    ]
    p = Puzzle(puzzle=pzl, num=3)
    p.solve()
    p.pprint()
if __name__ == '__main__':
    main()