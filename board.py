from copy import deepcopy

class Board:
    filename = ''

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def is_solution(id):
        cars = Board.id_to_board(id)

        if cars[0][1] == 4:
            return True
        else:
            return False

    @staticmethod
    def calculate_h(id):
        cars = Board.id_to_board(id)
        board = Board.make_taken_board(cars)
        h = 4-cars[0][1]
        for i in range(cars[0][1]+2,5):
            if board[2][i] == 1:
                h += 1
        return h

    @staticmethod
    def file_to_board(id):
        cars = []
        i = 0
        while i < len(id):
            cars.append([int(id[i+0]), int(id[i+2]), int(id[i+4]), int(id[i+6])])
            i += 8
        return cars

    @staticmethod
    def board_to_id(board):
        string = ""
        for car in board:
            string = string + (str(car))
        return string

    @staticmethod
    def id_to_board(id):
        cars = []
        i = 0
        while i < len(id):
            cars.append([int(id[i+1]), int(id[i+4]), int(id[i+7]), int(id[i+10])])
            i += 12
        return cars

    @staticmethod
    def make_root_node(filename):
        file = open(filename)
        id = ""
        for line in file:
            id = id + line
        id = Board.file_to_board(id)
        id = Board.board_to_id(id)
        return id

    @staticmethod
    def generate_successors(id):
        cars = Board.id_to_board(id)

        # Make map of where cars are present
        board = Board.make_taken_board(cars)


        # Make list of legal moves for each car
        legal_boards = []
        for x in range(len(cars)):
            car = cars[x]
            new_cars = deepcopy(cars)
            x_pos = car[1]
            y_pos = car[2]
            orientation = car[0]
            length = car[3]

            # check freedom in x direction
            if orientation == 0:
                if x_pos > 0 and board[y_pos][x_pos-1] == 0:
                    new_cars[x][1] = new_cars[x][1]-1
                    legal_boards.append(deepcopy(new_cars))
                    new_cars[x][1] = new_cars[x][1] + 1
                if x_pos+length < 6 and board[y_pos][x_pos+length] == 0:
                    new_cars[x][1] = new_cars[x][1]+1
                    legal_boards.append(deepcopy(new_cars))
                    new_cars[x][1] = new_cars[x][1] - 1

            # check freedom in y direction
            if orientation == 1:
                if y_pos > 0 and board[y_pos-1][x_pos] == 0 :
                    new_cars[x][2] = new_cars[x][2]-1
                    legal_boards.append(deepcopy(new_cars))
                    new_cars[x][2] = new_cars[x][2] + 1
                if y_pos+length < 6 and board[y_pos+length][x_pos] == 0:
                    new_cars[x][2] = new_cars[x][2]+1
                    legal_boards.append(deepcopy(new_cars))
                    new_cars[x][2] = new_cars[x][2] - 1

        # convert to strings
        strings_of_successors = []
        for board in legal_boards:
            strings_of_successors.append(Board.board_to_id(board))
        return strings_of_successors

    @staticmethod
    def make_taken_board(cars):
        board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
        for car in cars:
            x_pos = car[1]
            y_pos = car[2]
            orientation = car[0]
            length = car[3]
            if orientation == 0:
                board[y_pos][x_pos] = 1
                board[y_pos][x_pos + 1] = 1
                if length == 3:
                    board[y_pos][x_pos + 2] = 1
            if orientation == 1:
                board[y_pos][x_pos] = 1
                board[y_pos + 1][x_pos] = 1
                if length == 3:
                    board[y_pos + 2][x_pos] = 1

        return board

    @staticmethod
    def arc_cost(board1, board2):
        return 1