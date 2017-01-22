from basic_features.feature import *


class F1(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        p = sentence.words[sentence.words[counter].head]
        return (p.token, p.pos), True


class F2(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        p = sentence.words[sentence.words[counter].head]
        return (p.token), True


class F3(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        p = sentence.words[sentence.words[counter].head]
        return (p.pos), True


class F4(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        c = sentence.words[counter]
        return (c.token, c.pos), True


class F5(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        c = sentence.words[counter]
        return (c.token), True


class F6(FeatureGenerator):
    def get_hash_valid(self, sentence, counter):
        c = sentence.words[counter]
        return (c.pos), True
