import telebot

poly1 = ''
poly2 = ''

dict1 = {}
dict2 = {}


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
        first_p = dict1.get(i)
        second_p = dict2.get(i)
        if first_p is not None or second_p is not None:
            result_dict[i] = (first_p if first_p is not None else 0) + (second_p if second_p is not None else 0)
    print(result_dict)
    return result_dict


def result_poly(dict3):
    result = ''
    for i in dict3.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x' + str(abs(i[0]))
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







