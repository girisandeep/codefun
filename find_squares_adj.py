## Print all permutation of n squares such that no one is left alone - at least touching one side

def trunc(arr, r, c):
    m = []
    i = 0
    while i < (len(arr) - r):
        j = 0
        row = []
        while j < len(arr[0]) - c:
            row.append(arr[i][j])
            j += 1
        m.append(row)
        i += 1
    return m

def printarr(arr):
    for row in arr:
        print(row)

def findTrEmptyRows(arr):
    shiftRows = 0
    toEnd = False
    l = len(arr) -1
    while l > 0:
        row = arr[l]
        l -= 1
        isRow0 = True
        for cell in row:
            if cell != 0:
                toEnd = True
                break;
        if toEnd:
            break;
        shiftRows +=1
    return shiftRows


def findTrEmptyCols(arr):
    shiftCols = 0
    toEnd = False
    col = len(arr[0]) - 1
    while col > 0:
        for row in arr:
            if row[col] != 0:
                toEnd = True
                break;
        if toEnd:
            break;
        shiftCols +=1
        col -= 1
    return shiftCols

def findEmptyRows(arr):
    shiftRows = 0
    toEnd = False
    for row in arr:
        isRow0 = True

        for cell in row:
            if cell != 0:
                toEnd = True
                break;
        if toEnd:
            break;
        shiftRows +=1
    return shiftRows

def findEmptyCols(arr):
    shiftCols = 0
    toEnd = False
    for col in range(len(arr[0])):
        for row in arr:
            if row[col] != 0:
                toEnd = True
                break;
        if toEnd:
            break;
        shiftCols +=1
    return shiftCols

def shiftrc(arr, rows, cols):
    ii = 0
    i = rows
    marr = []
    while i < len(arr):
        j = cols
        jj = 0
        r = []
        while j < len(arr[i]):
            r.append(arr[i][j])
            jj += 1
            j += 1
        marr.append(r)
        ii += 1
        i += 1
    return marr

foundpatterns = {}
def to_str(board):
    s = ""
    for r in board:
        for c in r:
            s += str(c)
        s += ";"
    return s


def ifNewThenPrint(board):
    rows = findEmptyRows(board) #2
    cols = findEmptyCols(board) #1
    nb = shiftrc(board, rows, cols)
    
    c = findTrEmptyCols(nb)
    r = findTrEmptyRows(nb)
    nnb = trunc(nb, r, c)

    s = to_str(nnb)
    if s in foundpatterns:
        return;
    else:
        print("Found!!")
        foundpatterns[s] = True;
        printarr(nnb)
    return;

def findAllPos(board):
    all1 = []
    i = 0
    for r in board:
        j = 0
        for c in r:
            if c == 1:
                all1.append((i, j))
            j += 1
        i += 1        
    poss = []
#     print("all1")
#     print(all1)
    
    if len(all1) == 0:
        i = 0
        j = 0
        while j < len(board[i]):
            poss.append((i, j))
            j += 1
    else:
        for p in all1:
            #left
            i = p[0]
            j = p[1]
            if i > 0 and board[i-1][j] == 0:
                # Up
                poss.append((i-1, j))
            if i < len(board) - 1 and board[i+1][j] == 0:
                # Down
                poss.append((i+1, j))
            if j > 0 and board[i][j-1] == 0:
                # Up
                poss.append((i, j-1))
            if j < len(board[0]) - 1 and board[i][j+1] == 0:
                # Down
                poss.append((i, j+1))
#     print("Available positions: ")
#     print(poss)
    return poss

def place(brd, n):
#     print("n = %d, === Board ===" % n)
#     printarr(brd)
    if n == 0:
        ifNewThenPrint(brd)
        return
    for pos in findAllPos(brd):
        a = pos[0]
        b = pos[1]
#         print("Trying to place at (%d, %d): " % (a, b))
        brd[a][b] = 1
        place(brd, n-1)
        brd[a][b] = 0


def createM(w, h):
    return [[0 for x in range(w)] for y in range(h)] 

def gen_perms(n):
    board = createM(n, n)
#     print("Initial Board")
#     print(board)
    place(board, n)

gen_perms(4)