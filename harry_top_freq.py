# Eric Lu pl7he CS 4740 HW3 Problem 4

from mrjob.job import MRJob
import string
import operator

results = {}

class MRAllWordFrequency(MRJob):

    def mapper(self, _, line):
        if line:
            table = str.maketrans({}.fromkeys(string.punctuation))
            line_list = line.split(' ')
            line_list = [word.translate(table).lower() for word in line_list]
            if "" in line_list:
                line_list = line_list.remove("")
            if line_list:
                for word in line_list:
                    yield word, line_list.count(word)

    def reducer(self, key, values):
        global results
        results[key] = sum(values)

if __name__ == '__main__':
    MRAllWordFrequency.run()
    results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
    for item in results:
        print(item)