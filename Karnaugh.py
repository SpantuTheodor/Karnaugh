truth_table = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 0],
               [0, 1, 0, 1, 0], [0, 1, 1, 0, 0],
               [0, 1, 1, 1, 0], [1, 0, 0, 0, 0],
               [1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 0, 0, 0], [1, 1, 0, 1, 0],
               [1, 1, 1, 0, 0], [1, 1, 1, 1, 0]]


def validate_string(string_to_validate):
    index = string_to_validate.find("sigma(")
    if index >= 0:
        if (not string_to_validate[0: index].isspace()) and index != 0:
            return syntax_error()
        index += 6
        while string_to_validate[index] != ")":
            if string_to_validate[index] in "0123456789":
                number = int(string_to_validate[index])
                while string_to_validate[index + 1] in "0123456789":
                    number = number * 10 + int(string_to_validate[index + 1])
                    index += 1
                if number > 15:
                    return syntax_error()
                modify_truth_table(number, 1)
            elif string_to_validate[index] not in ",":
                return syntax_error()
            index += 1
        index += 1
        index_plus = string_to_validate.find("+")
        if index_plus >= 0:
            if (not string_to_validate[index:index_plus].isspace()) and index_plus != index:
                return syntax_error()
            index = string_to_validate.find("sigma*(")
            if index >= 0:
                if (not string_to_validate[index_plus + 1:index].isspace()) and index_plus + 1 != index:
                    return syntax_error()
                index += 7
                while string_to_validate[index] != ")":
                    if string_to_validate[index] in "0123456789":
                        number = int(string_to_validate[index])
                        while string_to_validate[index + 1] in "0123456789":
                            number = number * 10 + int(string_to_validate[index + 1])
                            index += 1
                        if number > 15:
                            return syntax_error()
                        modify_truth_table(number, '*')
                    elif string_to_validate[index] not in ",":
                        return syntax_error()
                    index += 1
                if (not string_to_validate[index + 1:len(string_to_validate)].isspace()) and index + 1 != len(
                        string_to_validate):
                    return syntax_error()
            else:
                return syntax_error()
    write_truth_table_in_file()


def syntax_error():
    print("Syntax error")
    return False


def modify_truth_table(line_number, value):
    truth_table[line_number][4] = value


def write_truth_table_in_file():
    f = open("truth_table.txt", "w")
    f.write("No. A B C D O \n")
    for index in range(len(truth_table)):
        if int(index / 10) == 0:
            index_to_string = " " + str(index)
        else:
            index_to_string = str(index)
        f.write(" " + index_to_string + " " + str(truth_table[index][0]) + " " + str(truth_table[index][1]) + " " + str(
            truth_table[index][2]) + " " +
                str(truth_table[index][3]) + " " + str(truth_table[index][4]) + "\n")
    fnc()
    f.close()


def fnc():
    condition = 0
    print("FNC: ", end='')
    for index, line in enumerate(truth_table, start=0):
        if line[4] == 0:
            if index != 0:
                print(" ∧ ", end='')
            if line[0] == 0:
                print("(A v ", end='')
                condition = 1
            else:
                print("(!A v ", end='')
                condition = 1
            if line[1] == 0:
                print("B v ", end='')
                condition = 1
            else:
                print("!B v ", end='')
                condition = 1
            if line[2] == 0:
                print("C v ", end='')
                condition = 1
            else:
                print("!C v ", end='')
                condition = 1
            if line[3] == 0:
                print("D)", end='')
                condition = 1
            else:
                print("!D)", end='')
                condition = 1
    if condition == 0:
        print("1")
    print("\n")


input_string = str(input())
validate_string(input_string)
print(truth_table)
