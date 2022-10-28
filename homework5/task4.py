# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE1.txt', 'r') as file:
    data = file.read()

def encode(data):
    code = ''
    previous_char = ''
    count = 1
    for char in data:
        if char != previous_char:
            if previous_char:
                code += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    return code

            
text1 = encode(data)
print(text1)

with open('RLE2.txt', 'w') as file2:
    data2 = file2.read()

def decoding(data2:str):
    count = ''
    decode = ''
    for char in data2:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = ''
    return decode

result = decoding(text1)
print(result)