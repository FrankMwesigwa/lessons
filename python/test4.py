

def flatten(input_array):
    result_array = []
    for element in input_array:
        if isinstance(element, int):
            result_array.append(element)
        elif isinstance(element, list):
            result_array += flatten(element)
    return result_array

print(flatten([1, [2, 3, [4]], 5, [[6]]]))
print(flatten([1, [2, 3, [4], []], [], 5, [[], [6]]]))