from sentence import *
from corpus import *


class FeatureGenerator(object):
    def __init__(self, parent_fv=None):
        self.hash2FeatureIdx = {}
        self.hash2Count = {}
        # self.featureIdx2hash = {}
        self.parent_fv = parent_fv
        self.filter = None

    def add_feature(self, sentence, counter):
        h, valid = self.get_hash_valid(sentence, counter)
        if not valid: return
        if h in self.hash2FeatureIdx:
            self.hash2Count[h] += 1
            # print('already exists hash:', h, ' with count: ', self.hash2Count[h])
        else:
            f_idx = self.parent_fv.add_feature(self)
            # print('adding feature ' + t + ' ' + words[i] + ' at index ' + str(featureVec.featureVecSize))
            self.hash2FeatureIdx[h] = f_idx
            # self.featureIdx2hash[f_idx] = h
            self.hash2Count[h] = 1

    def get_hash_valid(self, sentence, counter):
        print('must implement get_hash_and_valid() in' + self.__class__.__name__)
        exit(-1)

    def set_fv(self, fv):
        self.parent_fv = fv

    def filter_features(self, num):
        self.filter = num
        del_list = []
        for h in self.hash2FeatureIdx.keys():
            if self.hash2Count[h] < num:
                del_list.append(h)
        for h in del_list:
            # print(self.__class__.__name__ + ' delete ' + str(h) + ' due less counts (' + str(self.hash2Count[h]) + ') than ' + str(num))
            del self.hash2Count[h]
            del self.hash2FeatureIdx[h]


class FeatureVec(object):
    def __init__(self, fg_arr=[]):
        self.featureVecSize = -1
        self.featureIdx2Fg = {}
        # self.featureIdx2Tag = {}
        self.fgArr = fg_arr
        self.weights = []
        self.corpus = None

    def add_feature_gen(self, fg):
        fg.set_fv(self)
        self.fgArr.append(fg)

    def get_size(self):
        return self.featureVecSize + 1

    def set_weights(self, w):
        self.weights = w

    def get_weight_for_edge(self, sentence, head, counter):
        res = 0.0
        for fg in self.fgArr:
            k = fg.getFeatureIdx(sentence, head, counter)
            if k != -1:
                res += self.weights[k]
        return res

    def generate_features(self, corpus=None):
        if corpus is not None:
            self.corpus = corpus
        for s in corpus.get_sentences():
            for i in range(1, s.get_list_size()):
                for fg in self.fgArr:
                    fg.add_feature(s, i)
        print('fv contains ', self.get_size(), ' features')
        print(self.get_feature_count())

    def add_feature(self, feature_gen):
        self.featureVecSize += 1
        self.featureIdx2Fg[self.featureVecSize] = feature_gen  # in order to access specific feature
        # self.featureIdx2Tag[featureVec.featureVecSize] = t
        return self.featureVecSize

    def get_feature_gen_string(self):
        s = ''
        for fg in self.fgArr:
            s += ' ' + fg.__class__.__name__
        return s

    def get_feature_count(self):
        d = {}
        for fg in self.fgArr:
            d[fg.__class__.__name__] = len(fg.hash2FeatureIdx)
        return d

