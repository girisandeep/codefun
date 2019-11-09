import sys;

def sum_of_n(n, tot):
    #print "n: " + str(n);
    #print "total: " + str(tot);
    if n == 1:
        return [(tot,)];
    else:
        i = 1;
        new_tups = [];
        while i <= tot/2:
            all_tups = sum_of_n(n-1, tot-i);
            #print "got all_tups: " + str(all_tups);
            for tup in all_tups:
                #check if i in tup
                 #tuple(list(tup).append(i));
                if not i in tup:
                    new_tup = (i,) + tup
                    new_tups.append(new_tup)
            i += 1;
        return new_tups;

if __name__ == "__main__":
    print sum_of_n(int(sys.argv[1]), int(sys.argv[2]))

