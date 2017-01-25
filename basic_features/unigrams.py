from basic_features.feature import *
from conf import Conf

class F1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        p = sentence.words[head]
        return (p.token, p.pos), True


class F2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        p = sentence.words[head]
        return (p.token), True


class F3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        p = sentence.words[head]
        return (p.pos), True


class F4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        return (c.token, c.pos), True


class F5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        return (c.token), True


class F6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        return (c.pos), True


def add_unigrams(fv: FeatureVec):
    fv.add_feature_gen(F1(Conf.filter))
    fv.add_feature_gen(F2(Conf.filter))
    fv.add_feature_gen(F3(Conf.filter))
    fv.add_feature_gen(F4(Conf.filter))
    fv.add_feature_gen(F5(Conf.filter))
    fv.add_feature_gen(F6(Conf.filter))