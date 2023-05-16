# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...
text = (input("Введите текст: "))

dot = text.count('.')
comma = text.count(',')

if dot>comma:
    print("Больше знаков '.' - ", dot )
elif comma>dot:
    print("Больше знаков ',' - ", comma)
elif comma == dot:
    print("Одинаково
