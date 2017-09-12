
def check_solution(id):
    cars = id_to_board(id)

    if cars[0][1] == 4:
        return True
    else:
        return False


def file_to_board(id):
    cars = []
    i = 0
    while i < len(id):
        cars.append((int(id[i+0]), int(id[i+2]), int(id[i+4]), int(id[i+6])))
        i += 8
    return cars

def board_to_id(board):
    string = ""
    for car in board:
        string = string + (str(car))
    return string


def id_to_board(id):
    cars = []
    i = 0
    while i < len(id):
        cars.append((int(id[i+1]), int(id[i+4]), int(id[i+7]), int(id[i+10])))
        i += 12
    return cars


def load_file(filename):
    file = open(filename)
    id = ""
    for line in file:
        id = id + line
    id = file_to_board(id)
    id = board_to_id(id)
    return id

def legal_moves(id):
    cars = id_to_board(id)

    # Make map of where cars are present
    board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for car in cars:
        x_pos = car[1]
        y_pos = car[2]
        orientation = car[0]
        length = car[3]
        if orientation == 0:
            board[y_pos][x_pos] = 1
            board[y_pos][x_pos+1] = 1
            if length == 3:
                board[y_pos][x_pos+2] = 1
        if orientation == 1:
            board[y_pos][x_pos] = 1
            board[y_pos + 1][x_pos] = 1
            if length == 3:
                board[y_pos + 2][x_pos] = 1

    # Make list of legal moves for each car
    legal_boards = []
    for x in range(len(cars)):
        car = cars[x]
        new_cars = cars
        x_pos = car[1]
        y_pos = car[2]
        orientation = car[0]
        length = car[3]
        if orientation == 0:
            if board[y_pos][x_pos-1] == 0:
                new_cars[x][2] = new_cars[x][2]-1
                legal_boards.append(new_cars)
            if board[y_pos][x_pos+length] == 0:
                new_cars[x][2] = new_cars[x][2]+1
                legal_boards.append(new_cars)
        if orientation == 1:
            if board[y_pos-1][x_pos] == 0:
                new_cars[x][3] = new_cars[x][3]-1
                legal_boards.append(new_cars)
            if board[y_pos+length][x_pos] == 0:
                new_cars[x][3] = new_cars[x][3]+1
                legal_boards.append(new_cars)
    return legal_boards