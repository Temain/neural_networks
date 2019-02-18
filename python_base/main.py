# Задание light:
#   Взять длинный текстовый файл, посчитать статистику:
#   средняя длинна предложения, средняя длинна слова, частота буквы: количество буквы ‘a’ ‘b’ ‘c’ и т.д.,
#   деленное на количество слов. Записать результат в файл.
# Задание pro:
#   Разбить текст на предложения и использовать массив предложений для приема кросс-валидация.
#   Разбить на обучающую и тестовую k раз случайным образом и вывести статистику для каждого k.
#   Сильно ли отличается статистика между итерациями кросс-валидации (средние и std для каждого
#   параметра между обучающей и тестовой выборкой и между обучаю выборками для итераций)?
#   А для короткого файла? Кросс-валидацию можно сделать генератором, возвращающим обучающую и тестовую выборки.
#   Можно сделать класс в отдельном модуле.
#   https://en.wikipedia.org/wiki/Cross-validation_(statistics)#/media/File:K-fold_cross_validation_EN.jpg

import re

print("Reading file...")
with open('techno.txt', 'r') as f:
    text = f.read()

sentences = text.split('. ')
print(sentences[0])
print(len(sentences))

text_lower = text.lower()
text_clear = re.sub('[^a-zA-Z\\s]+', '', text_lower).replace('\r', '').replace('\n', '')
words_list = text_clear.split(' ')
words = sorted(set(words_list))
for index, word in enumerate(words):
    print("Index: {}, Word: {}".format(index, word))
print(len(words))
