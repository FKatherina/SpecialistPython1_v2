# Посчитайте количество согласных букв в данной строке.

text = ...
text = (input("Введите текст: "))

letter_a = text.count('а')
letter_e = text.count('е')
letter_o = text.count('о')
letter_y = text.count('у')
letter_ay = text.count('ю')
letter_ey = text.count('ё')
letter_ye = text.count('э')
letter_ee = text.count('и')
letter_yy = text.count('ы')
letter_eya = text.count('я')

Summa = letter_eya+letter_yy+letter_ee+letter_ye+letter_ey+letter_e+letter_a+letter_ay+letter_y+letter_o

print("Глассных букв - ", Summa )
# Лучший вариант
s = text
count = 0
vowels = set("ёуеыаоэяию")
for letter in s:
    if letter in vowels:
        count += 1
print("Количество гласных равно:", count)
