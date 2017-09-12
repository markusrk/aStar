import board

for x in board.legal_moves(board.load_file('easy-3.txt')):
    print(board.calculate_h(board.board_to_id(x)))


#print ((board.id_to_board(board.load_file('medium-1.txt'))))

#print( board.check_solution(board.load_file('easy-3.txt')))
#print('answer is here')

