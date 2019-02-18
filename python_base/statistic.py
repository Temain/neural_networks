import numpy


class Statistic:
    @staticmethod
    def average(str_list):
        return round(numpy.average(list(map(lambda x: len(x), str_list))))

    @staticmethod
    def freq(text):
        chars = {}
        for char in text:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 0
