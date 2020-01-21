def rename_command_dict(name, dictionary):
    return dict((name + "_" + k, v) for k, v in dictionary.items())


def mean(num_list):
    """Calculates mean of a list"""
    i = 0
    num_sum = 0.0
    for item in num_list:
        num_sum += item
        i += 1

    return num_sum/i


def total(num_list):
    """Calculates total of a list"""
    num_sum = 0.0
    for item in num_list:
        num_sum += item
    return num_sum
