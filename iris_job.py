# Eric Lu pl7he CS 4740 HW3 Problem 2
from mrjob.job import MRJob

count = 0

class MRMinSepalLength(MRJob):

    def mapper(self, _, line):
        if line:
            sepal_length = line.split(',')[0]
            yield "sepal_length", float(sepal_length)

    def reducer(self, key, values):
        yield 'min_' + key, min(values)

class MRMaxPetalWidth(MRJob):

    def mapper(self, _, line):
        if line:
            petal_width = line.split(',')[3]
            yield "petal_width", float(petal_width)

    def reducer(self, key, values):
        yield 'max_' + key, max(values)

class MRAvgSepalWidthSetosa(MRJob):

    def mapper(self, _, line):
        if line:
            global count
            count += 1
            l = line.split(',')
            if l[-1] == 'Iris-setosa':
                yield "setosa_sepal_width", float(l[1])

    def reducer(self, key, values):
        global count
        yield 'avg_' + key, sum(values)/count
        count = 0

class MRAvgSepalPetalLengthDiffNonSetosa(MRJob):

    def mapper(self, _, line):
        if line:
            global count
            count += 1
            l = line.split(',')
            if l[-1] != 'Iris-setosa':
                yield "sepal_petal_length_diff", float(l[0]) - float(l[2])

    def reducer(self, key, values):
        global count
        yield 'avg_' + key, sum(values) / count
        count = 0

if __name__ == '__main__':
    MRMinSepalLength().run()
    MRMaxPetalWidth().run()
    MRAvgSepalWidthSetosa().run()
    MRAvgSepalPetalLengthDiffNonSetosa().run()