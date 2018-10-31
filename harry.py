# Eric Lu pl7he CS 4740 HW3 Problem 3

from mrjob.job import MRJob
import string

class MRWordFrequency(MRJob):

    def mapper(self, _, line):
        if line:
            table = str.maketrans({}.fromkeys(string.punctuation))
            line_list = line.split(' ')
            line_list = [word.translate(table).lower() for word in line_list]
            yield "magical", line_list.count("magical")
            yield "soaring", line_list.count("soaring")
            yield "lopsided", line_list.count("lopsided")

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequency.run()