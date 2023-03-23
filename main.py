# coding=utf-8
import random

a = 100000
b = 1000000

message = """Отмечается тенденция к увеличению в зарубежных средствах мас-
совой информации объема материалов, содержащих предвзятую оценку
государственной политики Российской Федерации. Российские средства
массовой информации зачастую подвергаются за рубежом откровенной
дискриминации, российским журналистам создаются препятствия для
осуществления их профессиональной деятельности"""

d = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14,
     'н': 15, 'о': 16, 'п': 17, 'р': 18,
     'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'щ': 26, 'ш': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31,
     'ю': 32, 'я': 33, ' ': 34, ',': 35, '.': 36, '!': 37, '?': 38, '-': 39, '\n': 40}
d_inv = {v: k for k, v in d.items()}

print("d_inv ", d_inv)
low = {'А': 'а', 'Б': 'б', 'В': 'в', 'Г': 'г', 'Д': 'д', 'Е': 'е', 'Ё': 'ё', 'Ж': 'ж', 'З': 'э', 'И': 'и', 'Й': 'й',
       'К': 'к', 'Л': 'л', 'М': 'м', 'Н': 'н',
       'О': 'о', 'П': 'п', 'Р': 'р', 'С': 'с', 'Т': 'т', 'У': 'у', 'Ф': 'ф', 'Х': 'х', 'Ц': 'ц', 'Ч': 'ч', 'Ш': 'ш',
       'Щ': 'щ', 'Ъ': 'ъ', 'Ы': 'ы', 'Ь': 'ь', 'Э': 'э', 'Ю': 'ю', 'Я': 'я',
       'а': 'а', 'б': 'б', 'в': 'в', 'г': 'г', 'д': 'д', 'е': 'е', 'ё': 'ё', 'ж': 'ж', 'з': 'э', 'и': 'и', 'й': 'й',
       'к': 'к', 'л': 'л', 'м': 'м', 'н': 'н',
       'о': 'о', 'п': 'п', 'р': 'р', 'с': 'с', 'т': 'т', 'у': 'у', 'ф': 'ф', 'х': 'х', 'ц': 'ц', 'ч': 'ч', 'ш': 'ш',
       'щ': 'щ', 'ъ': 'ъ', 'ы': 'ы', 'ь': 'ь', 'э': 'э', 'ю': 'ю', 'я': 'я', ' ': ' ', ',': ',', '.': '.', '!': '!', '?': '?', '-': '-', '\n': '\n'}

# print low['О']
# print [el for el in message]
# print [el[1] for el in message]
# print([el for el in bytes(message, encoding='utf-8')])
# print([low[el] for el in message])
print([d[low[el]] for el in message])


# print [d[low[el]] for el in message]
first_param = 4578913
key = 1298735


def encrypt(msg, fp, key):
    msg = [d[low[el]] for el in msg]
    random.seed(fp)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] + r) % (len(d) + 1)

    random.seed(fp + key)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] + r) % (len(d) + 1)
    return msg


def decrypt(msg, fp, key):
    random.seed(fp + key)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] - r) % (len(d) + 1)
    random.seed(fp)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] - r) % (len(d) + 1)
    print(msg)
    ans = [d_inv[el ] for el in msg]
    return ans


print(encrypt(message, first_param, key))
print(decrypt(encrypt(message, first_param, key), first_param, key ))
