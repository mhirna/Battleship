def read_field(filename):
    '''

    :param filename:
    :return:
    '''
    dic = {}
    with open (filename, "r") as field:
        field = field.readlines()
        field_l = field.split("\n")
        for i in range(1, 11):
            for j in range(1, 11):
                if field[i][j] == "*":
                    dic["*"] += (j, i)
                elif field[i][j] == "X":
                    dic["X"] += (j, i)
    return dic

def read_field_boat(dic):
    dic_boat = {}


def has_ship(dic, t):
    if t in dic["*"]:
        return True
    else:
        return False


def ship_size(dic,t):
    pass