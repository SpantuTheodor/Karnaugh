truth_table = [[0, 0, 0, 0, "-"], [0, 0, 0, 1, "-"], [0, 0, 1, 0, "-"], [0, 0, 1, 1, "-"], [0, 1, 0, 0, "-"],
               [0, 1, 0, 1, "-"], [0, 1, 1, 0, "-"],
               [0, 1, 1, 1, "-"], [1, 0, 0, 0, "-"],
               [1, 0, 0, 1, "-"], [1, 0, 1, 0, "-"], [1, 0, 1, 1, "-"], [1, 1, 0, 0, "-"], [1, 1, 0, 1, "-"],
               [1, 1, 1, 0, "-"], [1, 1, 1, 1, "-"]]


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
                    elif string_to_validate[index] not in ",":
                        return syntax_error()
                    index += 1
                if (not string_to_validate[index + 1:len(string_to_validate)].isspace()) and index + 1 != len(string_to_validate):
                    return syntax_error()
        else:
            return syntax_error()


def syntax_error():
    print("Syntax error")
    return False


input_string = str(input())
validate_string(input_string)
