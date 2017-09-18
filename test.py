import board
from a import A
import Node
from Nonogram import Nonogram


print(Nonogram.id_to_table( Nonogram.table_to_id([1],[[1]])))


#print (Nonogram.rerun([[0]], [1,2], 2, [[0,4],[4,0],[2,0]], [1,1], 10, 0, 4))




#block_sizes = [1,1,1,1]
#line_size = 7

#alternatives = Nonogram.generate_line_alternatives(line_size, 0, block_sizes)
#for alternative in alternatives:
#    print(Nonogram.pos_to_table(alternative,block_sizes,line_size))
#print (Nonogram.load_file("Nonogram_boards/nono-cat.txt"))


#node = Node.Node(board.load_file('easy-3.txt'),True)
#print(node)



#a = A
#print(a.run(a))


#print(len(board.generate_successors(board.load_file('medium-1.txt'))))
#for x in board.generate_successors(board.load_file('medium-1.txt')):
#    print(board.calculate_h(board.board_to_id(x)))


#print ((board.id_to_board(board.load_file('medium-1.txt'))))

#print( board.check_solution(board.load_file('easy-3.txt')))
#print('answer is here')

