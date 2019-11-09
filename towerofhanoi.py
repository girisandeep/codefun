def towerofhanoi(n, src, target, aux):
		if n == 0:
			return;
		if n == 1:
			print("move ", n, " from ", src, " to ", target)
		else:
			towerofhanoi(n-1, src, aux, target)
			print("move ", n, " from ", src, " to ", target)
			towerofhanoi(n-1, aux, target, src)

if __name__ == '__main__':
	towerofhanoi(3, "S", "T", "A")