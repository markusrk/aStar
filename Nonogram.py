

class Nonogram():
    x_dim = 0
    y_dim = 0

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

