import random


def read_field(filename):
    dic = {'*': [], 'X': []}
    with open(filename, "r") as field:
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
    if t in dic["*"] or t in dic['X']:
        return True
    else:
        return False


def ship_size(dic, t):
    if has_ship(dic, t):
        dic_boat = {t[0]: [], t[1]: []}
        for i in dic['*']:
            for j in range(2):
                if i[j] in dic_boat:
                    dic_boat[i[j]].append(i)
        boat_h, boat_v = [], []
        for i in range(len(dic_boat[t[0]])):
            if i != len(dic_boat[t[0]]) - 1 and dic_boat[t[0]][i + 1][1] -
            dic_boat[t[0]][i][1] == 1:
                boat_v.append(dic_boat[t[0]][i])
                while i != len(dic_boat[t[0]]) - 1 and dic_boat[t[0]][i + 1][1] -
                dic_boat[t[0]][i][1] == 1:
                    boat_v.append(dic_boat[t[0]][i + 1])
                    i += 1
                break
        for i in range(len(dic_boat[t[1]])):
            if i != len(dic_boat[t[1]]) - 1 and ord(dic_boat[t[1]][i + 1][0]) -
            ord(dic_boat[t[1]][i][0]) == 1:
                boat_h.append(dic_boat[t[1]][i])
                while i != len(dic_boat[t[1]]) - 1 and
                ord(dic_boat[t[1]][i + 1][0]) - ord(dic_boat[t[1]][i][0]) == 1:
                    boat_h.append(dic_boat[t[1]][i + 1])
                    i += 1
                break
        if t not in boat_v and t not in boat_h:
            return (1, 1)
        if t in boat_v:
            return (1, len(boat_v))
        return (len(boat_h), 1)


def is_valid(data):
    dic_boat = {1: [], 2: [], 3: [], 4: []}
    for i in data['*'] + data['X']:
        dic_boat[max(ship_size(data, i))].append(i)
    print(dic_boat)
    if (len(dic_boat[1]) == 4) and (len(dic_boat[2]) == 6) and
    (len(dic_boat[3]) == 6) and (len(dic_boat[4]) == 4):
        return True
    else:
        return False


def field_to_str(data):
    field = [[" "] * 10 for i in range(10)]
    for i in range(len(data['*'])):
        field[data['*'][i][1] - 1][ord(data['*'][i][0]) - 65] = '*'
    for i in range(len(data['X'])):
        field[data['X'][i][1] - 1][ord(data['*'][i][0]) - 65] = 'X'
    field = ["".join(i) for i in field]
    f = open('field_current.txt', 'w')
    f.write("\n".join(field))
    return "\n".join(field)


data = read_field('field.txt')
field_to_str(data)
