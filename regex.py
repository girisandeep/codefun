def ismatch1(r, s):
	print "ismatch(%s, %s)" %(r,s)
	if (len(r) == len(s)) and len(r) == 0:
		return True;
	pos = 0;
	while pos < len(r):
		c = r[pos]
		if c == s[pos]:
			pos += 1
			continue;
		elif c == "*":
			l = pos;
			while l < len(s):
				if ismatch(r[pos+1:], s[l:]):
					return True;
				l += 1
		else:
			return False
	return False

def ismatch(r, s):
#	print "ismatch(%s, %s)" %(r,s)
	if len(r) == 0:
	 	if len(s) == 0:
			return True
		else:
			return False;
	elif r[0] == "*":
		i = 0;
		while i <= len(s):
			if ismatch(r[1:], s[i:]):
				return True;
			i += 1
		return False
	elif r[0] == s[0]:
		return ismatch(r[1:], s[1:])
	else:
		return False;
def assertEq(r, s):
	res = ismatch(r,s)
	print "ismatch(%s, %s) == %s" %(r,s, res)

def assertNEq(r, s):
	res = ismatch(r,s)
	print "not ismatch(%s, %s) == %s" %(r,s, not res)

assertEq("a*b*", "abc")
assertEq("a*b", "abb")
assertEq("a*b", "ab")
assertEq("a*b", "accccccb")
assertEq("a*b", "a*b")
assertEq("ab", "ab")
assertEq("*b", "ab")
assertEq("*b", "b")
assertEq("*b", "bbb")
assertNEq("*b", "bbbc")
assertEq("*", "c")
assertNEq("a*b*", "ac")
assertNEq("a*b*", "ac")
