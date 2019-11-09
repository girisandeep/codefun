def solve(board):
	pos = locatezero(board)

	for(num in range(1, 10)):
		if check(num, pos):
			place(num, board, pos)
			ret = solve(board)
			if ret == False:
				place(0, board, pos)
			else:
				return True
	return False


def solve_internal(board, current_position):
	for i in range(1, 10):
		if check(i, current_position):
			place(current_position, i)	


if __name__ == '__main__':
	(board, empty_positions) = load("501602904609800000827009003406107002218300005750004090074020001080063000000005370")

	#531672984649831257827549613496157832218396745753284196374928561185763429962415378
	print(solve(board, empty_positions))