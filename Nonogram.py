

class Nonogram():
    x_dim = 0
    y_dim = 0
    x_segments = []
    y_segments = []

    def __init__(self,path):
        self.x_dim,self.y_dim,self.x_segments,self.y_segments = self.load_file(path)

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


    @staticmethod
    def generate_line_alternatives(size, start_pos, line):
        no_of_filled = sum(line)
        no_of_white = size - no_of_filled
        no_of_blocks = len(line)
        freedom_of_first_block = size-no_of_filled-no_of_blocks+1+1

        alternatives = []
        if len(line) == 1:
            alternatives = []
            for x in range(0,size-line[0]+1):
                alternatives.append(x+start_pos)
            return alternatives
        else:
            for x in range(0,freedom_of_first_block):
                temp_alternatives = Nonogram.generate_line_alternatives(size-line[0]-1-x,start_pos+line[0]+1+x,line[1:])
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
