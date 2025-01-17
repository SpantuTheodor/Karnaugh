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
        return [[[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]],
                [[1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0]],
                [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]],
                [[1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0]]]
    elif number_of_variables == 4:
        return [[[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0]],
                [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
                [[1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0]],
                [[1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 0, 0]]]


def validate_string(string_to_validate, truth_table, k_map, number_of_variables):
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

                modify_truth_table(truth_table, number_of_variables, number, 1)
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

                        modify_truth_table(truth_table, number_of_variables, number, '*')
                    elif string_to_validate[index] not in ",":
                        return syntax_error()
                    index += 1
                if (not string_to_validate[index + 1:len(string_to_validate)].isspace()) and index + 1 != len(
                        string_to_validate):
                    return syntax_error()
            else:
                return syntax_error()
    else:
        return syntax_error()
    write_truth_table_in_file(truth_table, k_map, number_of_variables)


def syntax_error():
    print("Syntax error")
    return False


def modify_truth_table(truth_table, number_of_variables, line_number, value):
    if number_of_variables == 3:
        truth_table[line_number][3] = value
    else:
        truth_table[line_number][4] = value


def write_truth_table_in_file(truth_table, k_map, number_of_variables):
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
    f.close()
    fnc(truth_table, number_of_variables)
    fnd(truth_table, number_of_variables)
    modify_karnaugh_map(truth_table, k_map, number_of_variables)


def fnc(truth_table, number_of_variables):
    print()
    condition = 0
    print("FNC: ", end='')
    for line in truth_table:

        if number_of_variables == 3:
            if line[3] == 0:
                if condition != 0:
                    print(" ∧ ", end='')
                if line[0] == 0:
                    print("(A v ", end='')
                else:
                    print("(!A v ", end='')
                if line[1] == 0:
                    print("B v ", end='')
                else:
                    print("!B v ", end='')
                if line[2] == 0:
                    print("C)", end='')
                else:
                    print("!C)", end='')
                condition = 1

        if number_of_variables == 4:
            if line[4] == 0:
                if condition != 0:
                    print(" ∧ ", end='')
                if line[0] == 0:
                    print("(A v ", end='')
                else:
                    print("(!A v ", end='')
                if line[1] == 0:
                    print("B v ", end='')
                else:
                    print("!B v ", end='')
                if line[2] == 0:
                    print("C v ", end='')
                else:
                    print("!C v ", end='')
                if line[3] == 0:
                    print("D)", end='')
                else:
                    print("!D)", end='')
                condition = 1

    if condition == 0:
        print("1")
    print("\n", end='')


def fnd(truth_table, number_of_variables):
    condition = 0
    print("FND: ", end='')
    for line in truth_table:

        if number_of_variables == 3:
            if line[3] == 1:
                if condition != 0:
                    print(" v ", end='')
                if line[0] == 1:
                    print("(A ∧ ", end='')
                else:
                    print("(!A ∧ ", end='')
                if line[1] == 1:
                    print("B ∧ ", end='')
                else:
                    print("!B ∧ ", end='')
                if line[2] == 1:
                    print("C)", end='')
                else:
                    print("!C)", end='')
                condition = 1

        if number_of_variables == 4:
            if line[4] == 1:
                if condition != 0:
                    print(" v ", end='')
                if line[0] == 1:
                    print("(A ∧ ", end='')
                else:
                    print("(!A ∧ ", end='')
                if line[1] == 1:
                    print("B ∧ ", end='')
                else:
                    print("!B ∧ ", end='')
                if line[2] == 1:
                    print("C ∧ ", end='')
                else:
                    print("!C ∧ ", end='')
                if line[3] == 1:
                    print("D)", end='')
                else:
                    print("!D)", end='')
                condition = 1

    if condition == 0:
        print("0")
    print("\n")


def modify_karnaugh_map(truth_table, k_map, number_of_variables):
    # Functie ce adauga valorile de output din truth_table in KMap
    queue = []
    for index_row, map_row in enumerate(k_map, start=0):
        for index_column, map_item in enumerate(map_row, start=0):
            for table_item in truth_table:
                if number_of_variables == 3:
                    if compare_lists(map_item[0:3], table_item[0:3]):
                        map_item[3] = table_item[3]
                        if table_item[3] and index_row < 2:
                            queue.append([index_row, index_column])
                elif number_of_variables == 4:
                    if compare_lists(map_item[0:4], table_item[0:4]):
                        map_item[4] = table_item[4]
                        if table_item[4]:
                            queue.append([index_row, index_column])
    print_karnaugh_map(k_map, number_of_variables)
    karnaugh_minimization(k_map, number_of_variables, queue)


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
    return True


def print_karnaugh_map(k_map, number_of_variables):
    print("KMap: ")
    for row in k_map:
        for index, item in enumerate(row, start=1):
            print(item[number_of_variables], end=" ")
            if index % 4 == 0:
                print("\n", end="")


def karnaugh_minimization(k_map, number_of_variables, queue):
    if karnaugh_minimization_for_max(k_map, number_of_variables):
        print("K-minimization: ", 1)
        return
    if number_of_variables == 4:
        maximum_size = 8
        verified = []
    else:
        maximum_size = 4
        verified = [[2, 0], [2, 1], [2, 2], [2, 3],
                    [3, 0], [3, 1], [3, 2], [3, 3]]
    # while maximum_size:
    print(queue)
    to_print = []
    # In queue avem pozitiile din matrice etichetate cu 1 sau *
    while maximum_size:
        directional_array = change_directional_array(maximum_size, number_of_variables)
        for verified_max in range(maximum_size, 0, -1):
            for index in range(len(queue)):
                for template in directional_array:
                    condition_zero = 1
                    condition_visited = 0
                    number_visited = 0
                    for direction in template:
                        # verificam daca sunt doar valori de 1 sau * in KMap
                        if k_map[(queue[index][0] + direction[0]) % 4][(queue[index][1] + direction[1]) % 4][
                            number_of_variables] == 0:
                            condition_zero = 0
                        elif k_map[(queue[index][0] + direction[0]) % 4][(queue[index][1] + direction[1]) % 4][
                            number_of_variables] == 1:
                            # In cazul in care gasim un nod nevizitat
                            if find_list_in_list(
                                    [(queue[index][0] + direction[0]) % 4, (queue[index][1] + direction[1]) % 4],
                                    verified) == 0:
                                condition_visited = 1
                                number_visited += 1
                    if condition_zero and condition_visited and number_visited == verified_max:
                        to_print.append(minimization_result(k_map, queue[index], template, number_of_variables))
                        for aux in add_to_verified(queue[index], template):
                            verified.append(aux)

        if maximum_size == 1:
            maximum_size = 0

        maximum_size = int(maximum_size/2)
    print(to_print)
    write_to_print(to_print)


def write_to_print(to_print):
    # Eliminam minimizarile facute in plus
    for index, item in enumerate(to_print):
        print(item, end="")
        if index != len(to_print) - 1:
            print(" + ", end="")


def minimization_result(k_map, item, template, number_of_variables):
    index = 0
    result = []
    condition = 0
    to_print = ""
    wrong_indexes = set()
    # Iteram prin fiecare directie din template-ul primit ca parametru
    while index < len(template):
        # Iteram prin cele 4 coordonate din KMap
        for i in range(number_of_variables):
            if not condition:
                result.append(k_map[(item[0] + template[index][0]) % 4][
                                  (item[1] + template[index][1]) % 4][i])
            elif k_map[(item[0] + template[index][0]) % 4][
                (item[1] + template[index][1]) % 4][i] != \
                    result[i]:
                wrong_indexes.add(i)
        condition = 1
        index += 1
    for index, item in enumerate(result):
        if index not in wrong_indexes:
            if index == 0:
                if item == 0:
                    to_print += "!A"
                elif item == 1:
                    to_print += "A"
            if index == 1:
                if item == 0:
                    to_print += "!B"
                elif item == 1:
                    to_print += "B"
            if index == 2:
                if item == 0:
                    to_print += "!C"
                elif item == 1:
                    to_print += "C"
            if number_of_variables == 4:
                if index == 3:
                    if item == 0:
                        to_print += "!D"
                    elif item == 1:
                        to_print += "D"
    return to_print


def add_to_verified(item, template):
    verified = []
    for template_item in template:
        verified.append(
            [(item[0] + template_item[0]) % 4, (item[1] + template_item[1]) % 4])
    return verified


def find_list_in_list(small_list, big_list):
    for item in big_list:
        if compare_lists(small_list, item):
            return True
    return False


def karnaugh_minimization_for_max(k_maps, number_of_variables):
    for row in k_maps:
        for index in row:
            if index[number_of_variables] == 0:
                return False
    return True


def change_directional_array(maximum_size, number_of_variables):
    if number_of_variables == 4:
        if maximum_size == 8:
            return [[[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1]],
                    [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3]]]
        elif maximum_size == 4:
            return [[[0, 0], [0, 1], [1, 0], [1, 1]],
                    [[0, 0], [0, 1], [0, 2], [0, 3]],
                    [[0, 0], [1, 0], [2, 0], [3, 0]]]
        elif maximum_size == 2:
            return [[[0, 0], [0, 1]], [[0, 0], [1, 0]]]
        elif maximum_size == 1:
            return [[[0, 0]]]
    else:
        if maximum_size == 4:
            return [[[0, 0], [0, 1], [0, 2], [0, 3]],
                    [[0, 0], [0, 1], [1, 0], [1, 1]]]
        elif maximum_size == 2:
            return [[[0, 0], [0, 1]], [[0, 0], [1, 0]]]
        elif maximum_size == 1:
            return [[[0, 0]]]


def main():
    print("Number of Variables: ")
    number_of_variables = int(input())
    truth_table = define_truth_table(number_of_variables)
    k_map = define_karnaugh_map(number_of_variables)
    if truth_table:
        print("String template: sigma(x1,x2,...) /+ sigma*(y1,y2,...)")
        input_string = str(input())
        validate_string(input_string, truth_table, k_map, number_of_variables)


if __name__ == "__main__":
    main()
