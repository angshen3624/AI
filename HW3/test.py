execfile("asi031.py")
sb = init_board("input_puzzles/easy/9_9.sudoku")
sb = init_board("input_puzzles/more/9x9/9x9.15.sudoku")
f1 = solve(sb, True, False, True, True) #FC+MCV+LCV
f2 = solve(sb, True, True, False, True) #FC+MRV+LCV
f3 = solve(sb, True, False, False, True) #FC+LCV	
f4 = solve(sb, True, False, True, False) #FC+MCV
f5 = solve(sb, True, True, False, False) #FC+MRV
f6 = solve(sb, True, False, False, False) #FC
f7 = solve(sb, False, False, False, False) #BT
f1.print_board()
f2.print_board()
f3.print_board()
f4.print_board()
f5.print_board()
f6.print_board()
f7.print_board()
