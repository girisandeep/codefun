def minus(e1, e2):
    e = []
    i = 0;
    while i < len(e1):
        e.append(e1[i] - e2[i])
        i += 1
    return e

def eliminateLast(e1, e2):
    # ax + by = c
    # a1x + b1y = c1
    n = len (e1) - 1;
    b = e1[n]
    b1 = e2[n]
    print "Eliminating:"
    print e1;
    print e2;
    e1 = map(lambda x:x*b1, e1);
    e2 = map(lambda x:x*b, e2);
    sol = minus(e1[:-1], e2[:-1]);
    print sol;
    return sol;

def solve(list_equations):
    new_list=[]
    if len(list_equations) > 1:
        idx = 1;
        while idx < len(list_equations):
            first = list_equations[idx-1]
            second = list_equations[idx]
            new_list.append(eliminateLast(first, second));
            idx += 1
        
        solution = solve(new_list);
        print "Solution: " 
        print solution;
        e = list_equations[0]
        j = 1;
        sum = 0;
        while j < len(e)-1:
            sum += solution[j-1]*e[j]
            j += 1
        print "SUM: "
        print sum;
        z = (e[0] - sum) / e[-1];
        solution.append(z);
        return solution;
    elif len(list_equations) == 1:
        e = list_equations[0]
        return [e[0]/e[1]];

#a = [15, 1, 1]
#b = [10, 2, 3]
#e = solve([a, b]);
#print e;

# 2x + 3y+2z = 14
# 4x + 5y-z = 11
# 3x + 4y-2z = 5

print solve([[14, 2, 3, 2], [11, 4, 5, -1], [5, 3, 4, -2]]);

