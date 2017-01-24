from basic_features.feature import *
from conf import Conf

class FMissedBigrams1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.token, c.pos), True


class FMissedBigrams2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        return (p.pos, c.token), True


class FAbsDist(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        # if Conf.weak_root and head == 0: return False, False
        return (abs(head-counter)), True


class FDirection(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        # if Conf.weak_root and head == 0: return False, False
        if head < counter: return 'right', True
        return 'left', True


class FDist(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        # if Conf.weak_root and head == 0: return False, False
        return counter - head, True


class FSentenceLength(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        return len(sentence.words)-1, True


class FLength(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        return len(sentence), True


class FModifierNeighLR1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.token, cl.token, cr.token), True


class FModifierNeighLR2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.pos, cr.pos), True


class FModifierNeighLR3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.token, cr.pos), True


class FModifierNeighLR4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.token, cl.pos, cr.pos), True


class FModifierNeighLR5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.pos, cr.token), True


class FModifierNeighLR6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (cl.pos, cr.pos), True


class FModifierNeighLR7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        return (c.pos, cl.pos), True


class FModifierNeighLR8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if counter == len(sentence.words)-1: return False, False
        c = sentence.words[counter]
        cr = sentence.words[counter + 1]
        return (c.pos, cr.pos), True


class FHeadNeighLR1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0,len(sentence.words)-1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.token, cl.token, cr.token), True


class FHeadNeighLR2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.pos, cr.pos), True


class FHeadNeighLR3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.token, cr.pos), True


class FHeadNeighLR4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.token, cl.pos, cr.pos), True


class FHeadNeighLR5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.pos, cr.token), True


class FHeadNeighLR6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (cl.pos, cr.pos), True


class FHeadNeighLR7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head == 0: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        return (c.pos,cl.pos), True


class FHeadNeighLR8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if head == len(sentence.words) - 1: return False, False
        c = sentence.words[head]
        cr = sentence.words[head + 1]
        return (c.pos,cr.pos), True




def add_complex(fv: FeatureVec):
    fv.add_feature_gen(FMissedBigrams1())
    fv.add_feature_gen(FMissedBigrams2())
    fv.add_feature_gen(FAbsDist())
    fv.add_feature_gen(FDirection())
    fv.add_feature_gen(FDist())
    fv.add_feature_gen(FSentenceLength())
    fv.add_feature_gen(FModifierNeighLR1())
    fv.add_feature_gen(FModifierNeighLR2())
    fv.add_feature_gen(FModifierNeighLR3())
    fv.add_feature_gen(FModifierNeighLR4())
    fv.add_feature_gen(FModifierNeighLR5())
    fv.add_feature_gen(FModifierNeighLR6())
    fv.add_feature_gen(FModifierNeighLR7())
    fv.add_feature_gen(FModifierNeighLR8())
    fv.add_feature_gen(FHeadNeighLR1())
    fv.add_feature_gen(FHeadNeighLR2())
    fv.add_feature_gen(FHeadNeighLR3())
    fv.add_feature_gen(FHeadNeighLR4())
    fv.add_feature_gen(FHeadNeighLR5())
    fv.add_feature_gen(FHeadNeighLR6())
    fv.add_feature_gen(FHeadNeighLR7())
    fv.add_feature_gen(FHeadNeighLR8())









