import numpy


class Statistic:
    @staticmethod
    def average(str_list):
        return round(numpy.average(list(map(lambda x: len(x), str_list))))

    @staticmethod
    def frequency(text):
        chars = {}
        for char in text:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 0
        return chars

    @staticmethod
    def cross_valid(k, str_list):
        i = 0
        part = 0
        print("Total:", len(str_list))
        while True:
            i = i + 1
            prev = part
            part = int((len(str_list) / k) * i)
            print("Indexes interval:", prev, part)
            yield str_list[prev:part], str_list[0:prev] + str_list[part:]
