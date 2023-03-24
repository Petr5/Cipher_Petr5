# coding=utf-8
import random

a = 2 ** 16
b = 2 ** 17

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
low = {'А': 'а', 'Б': 'б', 'В': 'в', 'Г': 'г', 'Д': 'д', 'Е': 'е', 'Ё': 'ё', 'Ж': 'ж', 'З': 'з', 'И': 'и', 'Й': 'й',
       'К': 'к', 'Л': 'л', 'М': 'м', 'Н': 'н',
       'О': 'о', 'П': 'п', 'Р': 'р', 'С': 'с', 'Т': 'т', 'У': 'у', 'Ф': 'ф', 'Х': 'х', 'Ц': 'ц', 'Ч': 'ч', 'Ш': 'ш',
       'Щ': 'щ', 'Ъ': 'ъ', 'Ы': 'ы', 'Ь': 'ь', 'Э': 'э', 'Ю': 'ю', 'Я': 'я',
       'а': 'а', 'б': 'б', 'в': 'в', 'г': 'г', 'д': 'д', 'е': 'е', 'ё': 'ё', 'ж': 'ж', 'з': 'э', 'и': 'и', 'й': 'й',
       'к': 'к', 'л': 'л', 'м': 'м', 'н': 'н',
       'о': 'о', 'п': 'п', 'р': 'р', 'с': 'с', 'т': 'т', 'у': 'у', 'ф': 'ф', 'х': 'х', 'ц': 'ц', 'ч': 'ч', 'ш': 'ш',
       'щ': 'щ', 'ъ': 'ъ', 'ы': 'ы', 'ь': 'ь', 'э': 'э', 'ю': 'ю', 'я': 'я', ' ': ' ', ',': ',', '.': '.', '!': '!', '?': '?', '-': '-', '\n': '\n'}


print([d[low[el]] for el in message])


first_param = 100000
key = 118735


def encrypt(msg, fp, key):
    msg = [d[low[el]] for el in msg]
    ans = msg.copy()
    random.seed(fp)
    for i in range(len(ans)):
        r = random.randint(a, b)
        ans[i] = (ans[i] + r) % (len(d))


    random.seed(fp + key)
    for i in range(len(msg)):
        r = random.randint(a, b)
        ans[i] = (ans[i] + r) % (len(d))

    return ans


def decrypt(msg, fp, key):
    random.seed(fp + key)
    ans = msg.copy()
    rr = []
    for i in range(len(ans)):
        r = random.randint(a, b)
        ans[i] = (ans[i] - r) % (len(d))

    random.seed(fp)
    for i in range(len(msg)):
        r = random.randint(a, b)
        if key == 118735:
            rr.append(r)
        ans[i] = (ans[i] - r) % (len(d))
    res = [d_inv[el] for el in ans]
    return res


# print(encrypt(message, first_param, key))

# print(decrypt(encrypt(message, first_param, key), first_param, key))


def brute_decrypt(msg, fp, ll, rr):
    for kk in range(ll, rr, 1):
        ans = decrypt(msg, fp, kk)
        with open("ans.txt", "a") as f:
            f.write(f"fp {fp}  kk {kk}")
            f.write(''.join(ans) + "\n")
    # pass


enc_msg = encrypt(message, first_param, key)
brute_decrypt(enc_msg, first_param, a, b)


