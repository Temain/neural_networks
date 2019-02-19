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

from python_base.statistic import Statistic
from python_base.text_reader import TextReader

reader = TextReader('techno.txt')
text = reader.get_text()
sentences = reader.get_sentences()
words = reader.get_words()

results = [
    "Sentences average length: {}".format(Statistic.average(sentences)),
    "Words average length: ".format(Statistic.average(words))
]

chars = Statistic.frequency(text)
results.append("Frequency of chars: ")
chars_keys = sorted(chars, key=lambda x: chars[x], reverse=True)
for char in chars_keys:
    freq = round(chars[char] / len(words), 2)
    results.append("'{}' : {}".format(char, freq))

k = 5
generator = Statistic.cross_valid(k, sentences)
test, train = next(generator)
print(test)
test, train = next(generator)
print(test)

with open('result.txt', 'w') as f:
    f.write("\n".join(results))
