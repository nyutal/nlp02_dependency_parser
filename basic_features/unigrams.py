from basic_features.feature import *


class F1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        p = sentence.words[head]
        return (p.token, p.pos), True


class F2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        p = sentence.words[head]
        return (p.token), True


class F3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
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
