# задача по сложению полиномов из 4-ой домашки, которую я тогда не сделала


def create_dict(poly):
    poly_dict = {}
    if poly[0] == 'x':
        poly = '1' + poly
    poly = poly.replace(' + x', ' + 1x').replace(' - x', ' - 1x').replace('-x', '-1x').replace('x ', 'x1 ')
    poly = poly.replace(' - ', ' -').replace(' + ', ' +')
    poly = poly.split()
    poly = poly[:-2]
    if 'x' not in poly[len(poly) - 1]:
        poly[len(poly) - 1] = poly[len(poly) - 1] + 'x0'
    for i in range(len(poly)):
        poly[i] = poly[i].replace('+', '').split('x')
        poly_dict[int(poly[i][1])] = int(poly[i][0])
    print(poly_dict)
    return poly_dict


def poly_sum(dict1, dict2):
    result_dict = {}
    maximum = max(max(dict1), max(dict2))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first is not None or second is not None:
            result_dict[i] = (first if first is not None else 0) + (second if second is not None else 0)
    print(result_dict)
    return result_dict


def poly_back(dict3):
    result = ''
    for i in dict3.items():
        if result == '':
            if i[1] < 0:
                result += '-' + str(abs(i[1])) + 'x' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x' + str(abs(i[0]))
        result = result.replace('x1 ', 'x ').replace('x0', '').replace('1x', 'x')
        if result[len(result) - 1] == '1' and result[len(result) - 2] == 'x':
            result = result[:-1]
    return result + ' = 0'


with open('file1.txt', 'r', encoding='utf-8') as file:
    poly1 = file.readline()

with open('file2.txt', 'r', encoding='utf-8') as file:
    poly2 = file.readline()

print(poly1)
print(poly2)

dict1 = create_dict(poly1)
dict2 = create_dict(poly2)
dict3 = poly_sum(dict1, dict2)

poly3 = poly_back(dict3)
print(poly3)

with open('file3.txt', 'w', encoding='utf-8') as file:
    file.writelines(poly3)
