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
            mistakes = 0.
            print('perceptron iteration ', i, time.asctime())
            n_sen = 0
            for s in corpus.get_sentences():

                # get y_mst
                g = self.build_clique_graph(s, fv, weights)
                y_mst = ed.mst(0,g)
                y_mst_f = fv.get_features_for_graph(s, y_mst)

                # get y
                y = s.get_graph()
                y_f = fv.get_features_for_graph(s, y)


                if (self.compare_graphs(y, y_mst)):
                    # print('equal graphs')
                    # print(y)
                    # print(y_mst)
                    if not 0 in y_mst:
                        print(y)
                        print(g)
                        print(self.compare_graphs(y, y_mst))
                        raise AssertionError(y_mst)
                    continue


                weights = weights + y_f - y_mst_f
                # print(weights)
                mistakes += 1.0

                n_sen += 1
                if n_sen % 1000 == 0:
                    print('perceptron processed ', n_sen, 'sentences')
            print('perceptron iteration ', i, 'finished with', str(mistakes/n_sen) + '% difference graphs mistakes')
        return weights

    def build_clique_graph(self, s, fv, weights):
        g = {}
        for head in range(s.get_list_size()):
            g[head] = {}
            for counter in range(1, s.get_list_size()):
                g[head][counter] = fv.get_weight_for_edge(s, head, counter, weights)
        return g


    def compare_graphs(self, y, y_mst):
        if len(y_mst.keys()) != len(y.keys()):
            return False
        for h in y_mst:
            if h not in y:
                return False
                if len(y_mst[h].keys()) != len(y[h].keys()):
                    return False
                for m in y_mst[h].keys():
                    if m not in y[h]:
                        return False
        return True

    def test(self, corpus: Corpus, fv: FeatureVec, weights):
        nwords = 0.
        ncorrect = 0.
        for s in corpus.get_sentences():
            g = self.build_clique_graph(s, fv, weights)
            y_mst = ed.mst(0, g)
            for w in s.words[1:]:
                nwords += 1.0
                if w.head in y_mst and w.counter in y_mst[w.head]:
                    ncorrect += 1.0
                else:
                    print('error: (h,m)=(', w.head, w.counter, '), predicted graph:', y_mst)
        print('test: words=', str(nwords), ', correct words=', str(ncorrect), ', precision=', str(ncorrect/nwords*100) + '%')







