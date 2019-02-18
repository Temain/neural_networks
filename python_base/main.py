# ЗАДАНИЕ LIGHT:
#   Взять длинный текстовый файл, посчитать статистику:
#   средняя длинна предложения, средняя длинна слова, частота буквы: количество буквы ‘a’ ‘b’ ‘c’ и т.д.,
#   деленное на количество слов. Записать результат в файл.
# ЗАДАНИЕ PRO:
#   Разбить текст на предложения и использовать массив предложений для приема кросс-валидация.
#   Разбить на обучающую и тестовую k раз случайным образом и вывести статистику для каждого k.
#   Сильно ли отличается статистика между итерациями кросс-валидации (средние и std для каждого
#   параметра между обучающей и тестовой выборкой и между обучаю выборками для итераций)?
#   А для короткого файла? Кросс-валидацию можно сделать генератором, возвращающим обучающую и тестовую выборки.
#   Можно сделать класс в отдельном модуле.
#   https://en.wikipedia.org/wiki/Cross-validation_(statistics)#/media/File:K-fold_cross_validation_EN.jpg

import numpy
from python_base.text_reader import TextReader

reader = TextReader('techno.txt')
text = reader.get_text()
sentences = reader.get_sentences()
words = reader.get_words()

results = []
s_average = round(numpy.average(list(map(lambda x: len(x), sentences))))
results.append("Sentences average length: " + str(s_average))

w_average = round(numpy.average(list(map(lambda x: len(x), words))))
results.append("Words average length: " + str(w_average))

chars = {}
for char in text:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 0
results.append("Frequency of chars: ")
chars_keys = sorted(chars, key=lambda x: chars[x], reverse=True)
print(chars)
for char in chars_keys:
    freq = round(chars[char] / len(words), 2)
    results.append("'{}' : {}".format(char, freq))

with open('result.txt', 'w') as f:
    f.write("\n".join(results))
