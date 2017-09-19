import json
from copy import deepcopy


class VariableDomainEmptyException(Exception):
    pass


class DomainNotChangedException(Exception):
    pass

class ConflictingLocksException(Exception):
    pass

class NoMatchingPatternsException(Exception):
    pass

class Nonogram():
    x_dim = 7
    y_dim = 7
    x_segments = []
    y_segments = []

    def __init__(self, path):
        self.x_dim, self.y_dim, self.x_segments, self.y_segments = self.load_file(path)

    @staticmethod
    def id_to_table(id):
        return json.loads(id)[0], json.loads(id)[1]

    @staticmethod
    def table_to_id(row_table, column_table):
        return json.dumps([row_table, column_table])

    @staticmethod
    def column(matrix, i):
        return [row[i] for row in matrix]

    @staticmethod
    def load_file(path):
        file = open(path)
        counter = 0
        x_segments = []
        y_segments = []
        for line in file:
            if counter == 0:
                x_dim, y_dim = map(int, line.split(" "))
            elif counter <= y_dim:
                x_segments.append(list(map(int, line.split(" "))))
            else:
                y_segments.append(list(map(int, line.split(" "))))
            counter += 1
        return x_dim, y_dim, x_segments, y_segments

    # converts position and block size data to table of filled positions
    @staticmethod
    def pos_to_table(pos_list, block_size, size):
        table = [0] * size
        for x in range(0, len(pos_list)):
            for i in range(1, block_size[x] + 1):
                if table[pos_list[x] + i - 1] == 1:
                    raise Exception()
                table[pos_list[x] + i - 1] = 1
        return table

    @staticmethod
    def calculate_locked_fields(lines, segments, size):
        master_line = Nonogram.pos_to_table(lines[0], segments, size)
        for i in range(1, len(lines)):
            line_alternative = Nonogram.pos_to_table(lines[i], segments, size)
            for j in range(0, size):
                if master_line[j] != line_alternative[j]:
                    master_line[j] = 2
        return master_line

    def calculate_locked_table(self,locked_table, row_table, col_table):
        lr_table = []
        lc_table = []
        for i in range(0,self.y_dim):
            lr_table.insert(i,Nonogram.calculate_locked_fields(row_table[i],self.x_segments[i],self.x_dim))
        for i in range(0,self.x_dim):
            lc_table.insert(i, Nonogram.calculate_locked_fields(col_table[i], self.y_segments[i], self.y_dim))
        for i in range(0,self.y_dim):
            for j in range(0,self.x_dim):
                if lr_table[i][j] == 2:
                    locked_table[i][j] = lc_table[j][i]
                elif lc_table[j][i] == 2:
                    locked_table[i][j] = lr_table[i][j]
                elif lr_table[i][j] != lc_table[j][i] and lr_table[i][j] != 2 and lc_table[j][i] != 2:
                    raise ConflictingLocksException()
                elif lr_table[i][j] == lc_table[j][i]:
                    locked_table[i][j] = lc_table[j][i]
                else:
                    raise NoMatchingPatternsException
        return locked_table


    def rerun_all(self, row_table, col_table, line_no, orientation):
        locked_table = []
        for i in range(self.y_dim):
            locked_table.insert(i,[])
            for j in range(self.x_dim):
                locked_table[i].insert(j,0)
        locked_table = self.calculate_locked_table(locked_table, row_table, col_table)
        queue = []
        # add all columns to the queue
        if orientation == 0:
            for i in range(0, self.y_dim):
                queue.append((1, i))

        # pop a line and an orientation from the queue and check if any of the row/col alternatives break the locked_table cell values
        # if it does, then remove that alternative and set a changed flag so we can recalculate the locked table and add elements to the queue
        while queue:
            orientation, i = queue.pop(0)
            changed = False
            if orientation == 0:
                for x in range(0, len(row_table[i])):
                    line_alternative = Nonogram.pos_to_table(row_table[i][x], self.x_segments, self.x_dim)
                    for j in range(0, self.x_dim):
                        if locked_table[i][j] != 2 and locked_table[i][j] != line_alternative[j]:
                            row_table.remove[i][x]
                            changed = True
                if changed:
                    locked_line = Nonogram.calculate_locked_fields(row_table[i], self.x_segments, self.x_dim)
                    locked_table[i] = locked_line
                    for j in range(0,self.x_dim):
                        queue.append(1,j)
            if orientation == 1:
                for x in range(0, len(col_table[i])):
                    line_alternative = Nonogram.pos_to_table(col_table[i][x], self.y_segments, self.y_dim)
                    for j in range(0, self.y_dim):
                        if locked_table[j][i] != 2 and locked_table[j][i] != line_alternative[j]:
                            col_table.remove[i][x]
                            changed = True
                if changed:
                    locked_line = Nonogram.calculate_locked_fields(col_table[i], self.y_segments, self.y_dim)
                    for j in range(0,self.y_dim):
                        queue.append(0,j)
                        locked_table[j][i] = locked_line[j]

    def generate_successors(self, id):
        row_table, col_table = self.id_to_table(id)
        i = 0
        children = []
        # find first row with domain larger than 1
        while i < len(row_table):
            if len(row_table[i]) != 1:
                break
            i += 1
        # add all possible children for that row to child set.
        for j in range(0, len(row_table[i])):
            child = deepcopy(row_table)
            child[i] = row_table[i][j]
            children.append(deepcopy(child))
        # run rerun on all children
        for child in children:
            try:
                child = Nonogram.rerun_all(child, col_table, i, 0)
            except VariableDomainEmptyException:
                children.remove(child)
        return children

    # Generates row and column alternative tables
    def generate_tables(self):
        row_table = []
        col_table = []
        for i in range(0,self.y_dim):
            row_table.insert(i,Nonogram.generate_line_alternatives(self.x_dim,0,self.x_segments[i]))
        for i in range(0,self.x_dim):
            col_table.insert(i,Nonogram.generate_line_alternatives(self.y_dim, 0, self.y_segments[i]))
        return row_table, col_table

    # Generates all possible line alternatives based on segment size informantion
    @staticmethod
    def generate_line_alternatives(size, start_pos, segment_sizes):
        no_of_filled = sum(segment_sizes)
        no_of_white = size - no_of_filled
        no_of_blocks = len(segment_sizes)
        freedom_of_first_block = size - no_of_filled - no_of_blocks + 1 + 1

        alternatives = []
        if len(segment_sizes) == 1:
            alternatives = []
            for x in range(0, size - segment_sizes[0] + 1):
                alternatives.append([x + start_pos])
            return alternatives
        else:
            for x in range(0, freedom_of_first_block):
                temp_alternatives = Nonogram.generate_line_alternatives(size - segment_sizes[0] - 1 - x,
                                                                        start_pos + segment_sizes[0] + 1 + x,
                                                                        segment_sizes[1:])
                for alternative in temp_alternatives:
                    if isinstance(alternative, int):
                        alternatives.append([x + start_pos, alternative])
                    else:
                        alternative.insert(0, x + start_pos)
                        alternatives.append(alternative)
        return alternatives


