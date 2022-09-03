"""
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

txt = input("Введите текст через пробел:\n")

with open("init_text.txt", "a", encoding="utf-8") as data:
    data.write(txt)
    data.close()

with open("init_text.txt", encoding="utf-8") as data1:
    init_text = data1.read()
    data1.close()

fin_text = " ".join(filter(lambda x: "абв" not in x, init_text.split()))

with open("fin_text.txt", "a", encoding="utf-8") as data2:
    data2.write(fin_text)
    data2.close()

print(f"Исходный текст: {txt}")
print(f"Результат: {fin_text} (записан в файл fin_text.txt)")
