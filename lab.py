import random


def read_field(filename):
    '''
    :param filename: str
    :return: dic: dict

    Return dictionary with keys '*' and 'X' and values as lists of coordinates
    '''
    dic = {'*' : [], 'X' : []}
    with open (filename, "r") as field:
        field = field.readlines()
        field_l = [i.strip("\n") for i in field]
        for i in range(1, 11):
            for j in range(1, 11):
                if field_l[i - 1][j - 1] == "*":
                    dic["*"].append((chr(j + 96).upper(), i))
                elif field_l[i - 1][j - 1] == "X":
                    dic["X"].append((chr(j + 96).upper(), i))
    return dic


def has_ship(dic, t):
    '''
    :param dic: dict
    :param t: tuple
    :return: bool

    Return True if on selected coordinate there is a ship
    '''
    if t in dic["*"] or t in dic['X']:
        return True
    else:
        return False


def ship_size(dic,t):
    '''
    :param dic: dict
    :param t: tuple
    :return: t: tuple

    Return ship size that is situated in a coordinate
    '''
    if has_ship(dic,t):
        dic_boat = {t[0]: [], t[1]:[]}
        for i in dic['*']:
            for j in range(2):
                if i[j] in dic_boat:
                    dic_boat[i[j]].append(i)
        boat_h, boat_v = [], []
        for i in range(len(dic_boat[t[0]])):
            if  i != len(dic_boat[t[0]]) - 1 and dic_boat[t[0]][i + 1][1] - dic_boat[t[0]][i][1] == 1:
                boat_v.append(dic_boat[t[0]][i])
                while i != len(dic_boat[t[0]]) - 1 and dic_boat[t[0]][i + 1][1] - dic_boat[t[0]][i][1] == 1:
                    boat_v.append(dic_boat[t[0]][i + 1])
                    i += 1
                break
        for i in range(len(dic_boat[t[1]])):
            if i != len(dic_boat[t[1]]) - 1 and ord(dic_boat[t[1]][i + 1][0]) - ord(dic_boat[t[1]][i][0]) == 1:
                boat_h.append(dic_boat[t[1]][i])
                while i != len(dic_boat[t[1]]) - 1 and ord(dic_boat[t[1]][i + 1][0]) - ord(dic_boat[t[1]][i][0]) == 1:
                    boat_h.append(dic_boat[t[1]][i + 1])
                    i += 1
                break
        if t not in boat_v and t not in boat_h:
            return (1, 1)
        if t in boat_v:
            return (1, len(boat_v))
        return (len(boat_h), 1)


def is_valid(data):
    '''
    :param data: dict
    :return: bool

    Return True if a field is a valid battleship field
    '''
    dic_boat = {1 : [], 2 : [], 3 : [], 4 : []}
    for i in data['*'] + data['X']:
        dic_boat[max(ship_size(data, i))].append(i)
    print(dic_boat)
    if (len(dic_boat[1]) == 4) and (len(dic_boat[2]) == 6) and (len(dic_boat[3]) == 6) and (len(dic_boat[4]) == 4):
        return True
    else:
        return False


def field_to_str(data):
    '''
    :param data: dict
    :return: str

    Return a string of field and write it to a file field_current.txt
    '''
    field = [[" "] * 10 for i in range(10)]
    for i in range(len(data['*'])):
        field[data['*'][i][1] - 1][ord(data['*'][i][0]) - 65] = '*'
    for i in range(len(data['X'])):
        field[data['X'][i][1] - 1][ord(data['*'][i][0]) - 65] = 'X'
    field = ["".join(i) for i in field]
    f = open('field_current.txt', 'w')
    f.write("\n".join(field))
    return "\n".join(field)



def generate_field():
    '''
    Is supposed to return dictionary of coordinates
    However, is not working well yet
    Please, help!

    :return: data
    '''
    coords = []
    dic = {'*': []}
    for j in range(1, 13):
        coords.append([(j, i) for i in range(1, 13)])
    # size of a ship includes size around it
    ships = {4: [' ' * 6, ' **** ', ' ' * 6], 3: [' ' * 5, ' *** ', ' ' * 5] , 2: [' ' * 4, ' ** ', ' ' * 4],
             1: [' ' * 3, ' * ', ' ' * 3]}
    # create a field 12*12 not to worry about corners
    field = [["0"] * 12 for i in range(12)]
    direction = [('x', 0, r'-'), ('y', 1, r'-'), ('x', 0, r'+'), ('y', 1, r'+')]
    boat = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    times = 10
    while times > 0:
        coord = random.choice(random.choice(coords))
        dir = random.choice(direction)
        ship = ships[boat[10 - times]]
        # creating a tuple with ship size depending whether its situated on x or y
        if dir[0] == 'x':
            ship_s = (len(ships[boat[10 - times]][0]), 3)
        else:
            ship_s = (3, len(ships[boat[10 -  times]][0]))
        # choosing if to put ship up or down
        if coord[1] >= 6:
            y_func = r'+'
        else:
            y_func = r'-'
        x_func = dir[2]
        if 0 <= eval(str(coord[0]) + x_func + str(ship_s[0])) <= 12 and 0 <= eval(str(coord[1]) + y_func
                                                                                           + str(ship_s[1])) <= 12:
            empty = True
            for i in range(ship_s[0]):
                for j in range(ship_s[1]):
                    field_x = eval(str(coord[0] - 1) + x_func + str(i))
                    field_y = eval(str(coord[1] - 1) + y_func + str(j))
                    if field[field_y][field_x] != '0':
                        empty = False
            if empty:
                for i in range(ship_s[0]):
                    for j in range(ship_s[1]):
                        field_x = eval(str(coord[0] - 1) + x_func + str(i))
                        field_y = eval(str(coord[1] - 1) + y_func + str(j))
                        field[field_y][field_x] = ship[j][i]
                        if ship[j, i] == '*':
                            dic['*'].append((field_y + 1, field_x + 1))
                        coords[field_y].remove((field_y + 1, field_x + 1))
                times -= 1
    return dic


data = read_field('field.txt')
generate_field()
data = read_field('field.txt')
field_to_str(data)
