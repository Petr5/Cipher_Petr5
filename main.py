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

d = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13,
     'н': 14, 'о': 15, 'п': 16, 'р': 17,
     'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'щ': 25, 'ш': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30,
     'ю': 31, 'я': 32, ' ': 33, ',': 34, '.': 35, '!': 36, '?': 37, '-': 38, '\n': 39}
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
        msg[i] = (msg[i] + r) % (len(d))

    random.seed(fp + key)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] + r) % (len(d))
    return msg


def decrypt(msg, fp, key):
    random.seed(fp + key)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] - r) % (len(d))
    random.seed(fp)
    for i in range(len(msg)):
        r = random.randint(a, b)
        msg[i] = (msg[i] - r) % (len(d))
    print(msg)
    ans = [d_inv[el] for el in msg]

    return ans


print(encrypt(message, first_param, key))
print(decrypt(encrypt(message, first_param, key), first_param, key ))


def brute_decrypt(msg, l, r, key):
    for i in range(l, r, 1):
        ans = decrypt(msg, l, key)
        with open("ans.txt", "a") as f:
            f.write(''.join(ans) + "\n")
    # pass


brute_decrypt(encrypt(message, first_param, key), a, b, key)

