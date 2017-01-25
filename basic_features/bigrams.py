from basic_features.feature import *
from conf import Conf

class F7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, p.pos, c.token, c.pos), True


class F8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.pos, c.token, c.pos), True


class F9(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, c.token, c.pos), True


class F10(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, p.pos, c.pos), True


class F11(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, p.pos, c.token), True


class F12(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, c.token), True


class F13(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.pos, c.pos), True


def add_bigrams(fv: FeatureVec):
    fv.add_feature_gen(F7(Conf.filter))
    fv.add_feature_gen(F8(Conf.filter))
    fv.add_feature_gen(F9(Conf.filter))
    fv.add_feature_gen(F10(Conf.filter))
    fv.add_feature_gen(F11(Conf.filter))
    fv.add_feature_gen(F12(Conf.filter))
    fv.add_feature_gen(F13(Conf.filter))

