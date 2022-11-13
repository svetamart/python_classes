# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('RLE1.txt', 'r') as file:
#     data = file.readlines()

text = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(f'Исходные данные: {text}')

def encode(text):
    code = ''
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
            if count == 9:
                code += str(count) + text[i]
                count = 1
        elif text[i] != text[i + 1]:
            code += str(count) + text[i]
            count = 1
    if count > 1 or text[len(text) - 2] != text[-1]:
        code += str(count) + text[-1]
    return code

encoded = encode(text)        
print(f'Сжатый файл: {encoded}')

with open('RLE2.txt', 'w') as data:
    data.write(encoded)

with open('RLE2.txt', 'r') as data:
    new_text_file = data.readlines()

for_decoding = ''.join(new_text_file)

def decoding(for_decoding):
    count = ''
    decode = ''
    for i in range(0, len(for_decoding), 2):
        count = for_decoding[i] 
        decode += for_decoding[i + 1] * int(count)
    return decode

result = decoding(for_decoding)
print(f'Восстановленные данные: {result}')