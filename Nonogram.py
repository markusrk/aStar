import json
from copy import deepcopy

class VariableDomainEmptyException(Exception):
    pass

class DomainNotChangedException(Exception):
    pass

class Nonogram():
    x_dim = 0
    y_dim = 0
    x_segments = []
    y_segments = []

    def __init__(self,path):
        self.x_dim,self.y_dim,self.x_segments,self.y_segments = self.load_file(path)

    @staticmethod
    def id_to_table(id):
        return json.loads(id)[0], json.loads(id)[1]

    @staticmethod
    def table_to_id(row_table,column_table):
        return json.dumps([row_table,column_table])

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
                x_dim, y_dim = map(int,line.split(" "))
            elif counter <= x_dim:
                x_segments.append(list(map(int,line.split(" "))))
            else:
                y_segments.append(list(map(int,line.split(" "))))
            counter += 1
        return x_dim, y_dim, x_segments, y_segments

    # converts position and block size data to table of filled positions
    @staticmethod
    def pos_to_table(pos_list, block_size, size):
        table = [0]*size
        for x in range(0,len(pos_list)):
            for i in range(1,block_size[x]+1):
                if table[pos_list[x]+i-1] == 1:
                    raise Exception()
                table[pos_list[x]+i-1] = 1
        return table

    # reruns the domain constraint algorithm and return an updated  changed_line. This version calculates the entire line and not only one field, might be usefull later on
    @staticmethod
    def rerun(pos_ul, block_size_ul, size_ul, pos_cl, block_size_cl, size_cl, ul_cross, cl_cross):
        if len(block_size_cl) != len(pos_cl) or len(block_size_ul) != len(pos_ul):
            raise ValueError("position and block size did not have the same number of variables")
        master = None
        #check if ul has a defined value for the crossover field, if not, raise an exception indicating that
        for line_alternative in pos_ul:
            alternative = Nonogram.pos_to_table(line_alternative,block_size_ul,size_ul)
            if master is None:
                master = alternative[ul_cross]
            if master != alternative[ul_cross]:
                raise DomainNotChangedException()

        #clear cl domain from values that does not match the locked common value
        i =0
        while i < len(pos_cl):
            line = Nonogram.pos_to_table(pos_cl[i],block_size_cl,size_cl)
            if line[cl_cross] != master:
                del pos_cl[i]
            i += 1

        #if domain becomes empty raise an error
        if len(pos_cl) == 0:
            raise VariableDomainEmptyException()
        return pos_cl


    def rerun_all(self, line, table):
        queue = []
        #initialize queue
        for i in range(0,self.x_dim):
            queue.append((self.rerun(), table[line], self.x_segments, self.x_dim, self.column(table, i), self.y_segments, self.y_dim,
             i, line)
        while len(queue) != 0:
            try:
                t = queue.pop(0)
                t[0](*t[1:])
                
            except DomainNotChangedException:
                continue


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
                child = Nonogram.rerun_all(i, child)
            except VariableDomainEmptyException:
                children.remove(child)
        return children

    # Generates all possible line alternatives based on segment size informantion
    @staticmethod
    def generate_line_alternatives(size, start_pos, segment_sizes):
        no_of_filled = sum(segment_sizes)
        no_of_white = size - no_of_filled
        no_of_blocks = len(segment_sizes)
        freedom_of_first_block = size-no_of_filled-no_of_blocks+1+1

        alternatives = []
        if len(segment_sizes) == 1:
            alternatives = []
            for x in range(0, size-segment_sizes[0]+1):
                alternatives.append([x+start_pos])
            return alternatives
        else:
            for x in range(0,freedom_of_first_block):
                temp_alternatives = Nonogram.generate_line_alternatives(size - segment_sizes[0] - 1 - x, start_pos + segment_sizes[0] + 1 + x, segment_sizes[1:])
                for alternative in temp_alternatives:
                    if isinstance(alternative,int):
                        alternatives.append([x+start_pos,alternative])
                    else:
                        alternative.insert(0, x + start_pos)
                        alternatives.append(alternative)
        return alternatives






    @staticmethod
    def generate_line_alternatives_backup(size, line):
        no_of_filled = sum(line)
        no_of_white = size - no_of_filled
        no_of_blocks = len(line)
        freedom_of_first_block = size-no_of_filled-no_of_blocks+1+1

        alternatives = []
        if len(line) == 1:
            alternatives = []
            for x in range(0,size-line[0]+1):
                alternatives.append(x)
            return alternatives
        else:
            for x in range(0,freedom_of_first_block):
                temp_alternatives = Nonogram.generate_line_alternatives(size-line[0]-1-x,line[1:])
                adjusted_positions = [y + line[0]+1+x for y in temp_alternatives]
                for alternative in adjusted_positions:
                    if isinstance(alternative,int):
                        alternatives.append([x,alternative])
                    else:
                        alternatives.append(alternative.insert(0,x))
        return alternatives


    # reruns the domain constraint algorithm and return an updated  changed_line. This version calculates the entire line and not only one field, might be usefull later on
    @staticmethod
    def rerun_backup(pos_ul, block_size_ul, size_ul, pos_cl, block_size_cl, size_cl, x_cross, y_cross):
        master_line = None
        for line_alternative in pos_ul:
            alternative = Nonogram.pos_to_table(line_alternative,block_size_ul,size_ul)
            if master_line is None:
                master_line = alternative
            for i in range(0,size_ul):
                if master_line[i] != alternative[i]:
                    master_line[i] = 2
        # Todo comparison to cl to check if match
        return


