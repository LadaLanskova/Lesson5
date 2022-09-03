"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""


def encoding_rle(ss):
    encoded_lst = []
    prev_char = ""
    count = 1
    for i in ss:
        if i != prev_char:
            if prev_char:
                encoded_lst.append(str(count))
                encoded_lst.append(":")
                encoded_lst.append(str(prev_char))
                encoded_lst.append(" ")
            count = 1
            prev_char = i
        else:
            count += 1
    else:
        encoded_lst.append(str(count))
        encoded_lst.append(":")
        encoded_lst.append(str(prev_char))
    return encoded_lst


def decoding_rle(ss1):
    decoded_lst = []
    d = len(ss1)
    for i in range(1, d, 4):
        cnt = 1
        cnt1 = int(ss1[i-1])
        while cnt1 >= cnt:
            decoded_lst.append(ss1[i+1])
            cnt += 1
    return decoded_lst


with open("source_forTask4.txt", encoding="utf-8") as data:
    my_text = list(data.read())
    data.close()

encoded_text = "".join(encoding_rle(my_text))

with open("encoded.txt", "a", encoding="utf-8") as data1:
    data1.write(encoded_text)
    data1.close()

with open("encoded.txt", encoding="utf-8") as data2:
    my_text1 = list(data2.read())
    data2.close()

decoded_text = "".join(decoding_rle(my_text1))

with open("decoded.txt", "a", encoding="utf-8") as data3:
    data3.write(decoded_text)
    data3.close()

print("Исходный текст:", "".join(my_text))
print("Сжатые данные:", encoded_text, "(записаны в файл еncoded.txt)")
print("Раскодированные данные:", decoded_text, "(записаны в файл dеcoded.txt)")
