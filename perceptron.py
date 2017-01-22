import numpy as np
import time
from basic_features.feature import *
import edmonds as ed

class Perceptron(object):

    def __init__(self):
        pass

    def train(self, corpus: Corpus, fv: FeatureVec, niter: int):
        weights = np.ones(fv.get_size())
        for i in range(niter):
            print('perceptron iteration ', i, time.asctime())
            n_sen = 0
            for s in corpus.get_sentences():

                # get y_mst
                g = {}
                for head in range(s.get_list_size()):
                    g[head] = {}
                    for counter in range(1, s.get_list_size()):
                        g[head][counter] = fv.get_weight_for_edge(s, head, counter, weights)
                # g = ed._reverse(g)
                y_mst = ed.mst(0,g)
                y_mst_f = fv.get_features_for_graph(s, y_mst)

                # get y
                y = s.get_graph()
                y_f = fv.get_features_for_graph(s, y)
                # for h in y:
                #     for m in y[h].keys():
                #         y[h][m] = fv.get_weight_for_edge(s, h, m, weights)

                if (self.compare_graphs(y, y_mst)):
                    # print('equal graphs')
                    # print(y)
                    # print(y_mst)
                    continue

                weights = weights + y_f - y_mst_f
                print(weights)

                n_sen += 1
                if n_sen % 1000 == 0:
                    print('perceptron processed ', n_sen, 'sentences')


    def compare_graphs(self, y, y_mst):
        for h in y_mst:
            if h not in y:
                return False
                if len(y_mst[h].keys()) != len(y[h].keys()):
                    return False
                for m in y_mst[h].keys():
                    if m not in y[h]:
                        return False
        return True










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
