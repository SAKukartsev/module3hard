data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
obj = data_structure


def calculate_structure_sum(obj):
    if (type(obj) == int) or (type(obj) == float):
        return obj
    else:
        if type(obj) == str:
            return len(obj)
        else:
            if len(obj) <= 0:
                return 0
            else:
                sum_ = 0
                if type(obj) == dict:
                    obj = list(obj.items())
                for elem in obj:
                    sum_ = sum_ + calculate_structure_sum(elem)
                return sum_


print(calculate_structure_sum(obj))
