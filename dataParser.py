from sentence import *


class DataParser(object):

    def __init__(self):
        pass

    def parse(self, inFile):
        newSententence = True
        sentences = []
        sentence = Sentence()
        with open(inFile) as f:
            for line in f:
                if not line.strip():
                    if sentence.get_length() > 0:
                        sentences.append(sentence)
                        print(sentence.getSentence())
                    else:
                        print('drop empty sentence')
                    sentence = Sentence()
                    continue
                tabs = line.split('\t')
                sentence.append(Word(tabs[0], tabs[1], tabs[3], tabs[6]))

class Trainer(object):

    def __init__(self):
        pass

    # Make a prediction with weights
    def predict(self, row, weights):
        activation = weights[0]
        for i in range(len(row) - 1):
            activation += weights[i + 1] * row[i]
        return 1.0 if activation >= 0.0 else 0.0

    # Estimate Perceptron weights using stochastic gradient descent
    def train_weights(self, train, l_rate, n_epoch):
        weights = [0.0 for i in range(len(train[0]))]
        for epoch in range(n_epoch):
            sum_error = 0.0
            for row in train:
                prediction = self.predict(row, weights)
                error = row[-1] - prediction
                sum_error += error**2
                weights[0] = weights[0] + l_rate * error
                for i in range(len(row)-1):
                    weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
        return weights


if __name__ == '__main__':

    dp = DataParser()
    dp.parse('HW2-files/train.labeled')

