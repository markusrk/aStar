import board
from a import A
import Node
from copy import deepcopy
from Nonogram import Nonogram


#print(Nonogram.id_to_table( Nonogram.table_to_id([1],[[1]])))



#print (Nonogram.rerun([[0]], [1,2], 2, [[0,4],[4,0],[2,0]], [1,1], 10, 0, 4))

#locked_table = [[deepcopy(0) for x in range(10)] for y in range(10)]
#locked_table[5][5] = 1
#print(locked_table)

n = Nonogram('Nonogram_boards/nono-cat.txt')
x_dim, y_dim, x_segment, y_segment = Nonogram.load_file("Nonogram_boards/nono-cat.txt")
row_table, col_table = n.generate_tables()
locked_table = []
for i in range(y_dim):
    locked_table.insert(i, [])
    for j in range(x_dim):
        locked_table[i].insert(j, 0)

p = n.calculate_locked_table(locked_table,row_table,col_table)

for line in p:
    print(line)


row_table1, col_table = n.rerun_all(row_table,col_table,0,1)
#print()
#print()
#for x in range(y_dim):
#    print(p[x])
#    print(row_table1[x])
#    print((row_table[x]))
#    print(x_segment[x])


#block_sizes = [1,1]
#line_size = 7
#alternatives = Nonogram.generate_line_alternatives(line_size, 0, block_sizes)
#alternatives = [[0,2],[0,2],[2,4]]

#print(Nonogram.calculate_locked_fields(alternatives,block_sizes,line_size))

#print(alternatives)
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

