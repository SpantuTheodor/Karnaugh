def define_truth_table(number_of_variables):
    if number_of_variables == 3:
        return [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0],
                [1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 0]]
    elif number_of_variables == 4:
        return [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0],
                [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [1, 0, 1, 1, 0],
                [1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 0]]
    else:
        print("Syntax Error")
        return False


def define_karnaugh_map(number_of_variables):
    if number_of_variables == 3:
        return [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0],
                [1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
    elif number_of_variables == 4:
        return [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0],
                [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0],
                [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 0],
                [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 1, 0]]


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

                if number_of_variables == 3:
                    if number > 7:
                        return syntax_error()
                if number_of_variables == 4:
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

                            if number_of_variables == 3:
                                if number > 7:
                                    return syntax_error()
                            if number_of_variables == 4:
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
    if number_of_variables == 3:
        truth_table[line_number][3] = value
    else:
        truth_table[line_number][4] = value


def write_truth_table_in_file():
    f = open("truth_table.txt", "w")
    if number_of_variables == 3:
        f.write("No. A B C O \n")
        for index in range(len(truth_table)):
            index_to_string = str(index)
            f.write(
                " " + index_to_string + " " + str(truth_table[index][0]) + " " + str(truth_table[index][1]) + " " + str(
                    truth_table[index][2]) + " " + str(truth_table[index][3]) + "\n")
    else:
        f.write("No. A B C D O \n")
        for index in range(len(truth_table)):
            if int(index / 10) == 0:
                index_to_string = " " + str(index)
            else:
                index_to_string = str(index)
            f.write(
                " " + index_to_string + " " + str(truth_table[index][0]) + " " + str(truth_table[index][1]) + " " + str(
                    truth_table[index][2]) + " " +
                str(truth_table[index][3]) + " " + str(truth_table[index][4]) + "\n")
    fnc()
    fnd()
    f.close()


def fnc():
    condition = 0
    print("FNC: ", end='')
    for line in truth_table:

        if number_of_variables == 3:
            if line[3] == 0:
                if condition != 0:
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
                    print("C)", end='')
                    condition = 1
                else:
                    print("!C)", end='')
                    condition = 1

        if number_of_variables == 4:
            if line[4] == 0:
                if condition != 0:
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


def fnd():
    condition = 0
    print("FND: ", end='')
    for line in truth_table:

        if number_of_variables == 3:
            if line[3] == 1:
                if condition != 0:
                    print(" v ", end='')
                if line[0] == 1:
                    print("(A ∧ ", end='')
                    condition = 1
                else:
                    print("(!A ∧ ", end='')
                    condition = 1
                if line[1] == 1:
                    print("B ∧ ", end='')
                    condition = 1
                else:
                    print("!B ∧ ", end='')
                    condition = 1
                if line[2] == 1:
                    print("C)", end='')
                    condition = 1
                else:
                    print("!C)", end='')
                    condition = 1

        if number_of_variables == 4:
            if line[4] == 1:
                if condition != 0:
                    print(" v ", end='')
                if line[0] == 1:
                    print("(A ∧ ", end='')
                    condition = 1
                else:
                    print("(!A ∧ ", end='')
                    condition = 1
                if line[1] == 1:
                    print("B ∧ ", end='')
                    condition = 1
                else:
                    print("!B ∧ ", end='')
                    condition = 1
                if line[2] == 1:
                    print("C ∧ ", end='')
                    condition = 1
                else:
                    print("!C ∧ ", end='')
                    condition = 1
                if line[3] == 1:
                    print("D)", end='')
                    condition = 1
                else:
                    print("!D)", end='')
                    condition = 1

    if condition == 0:
        print("1")
    print("\n")


print("Number of Variables: ")
number_of_variables = int(input())
truth_table = define_truth_table(number_of_variables)
if truth_table:
    input_string = str(input())
    validate_string(input_string)
    print(truth_table)
