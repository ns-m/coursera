def number_to_string(numbers):
    strings = []
    for number in numbers:
        strings.append(str(number))
    print(strings, type(strings))

number_to_string((0,1,2,3,4,5,6))

def number_to_string2(numbers2):
    return list(map(str, numbers2))

print(number_to_string2(range(7)))