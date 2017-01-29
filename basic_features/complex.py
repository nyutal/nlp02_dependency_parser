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
        return (abs(head - counter)), True


class FDirection(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        # if Conf.weak_root and head == 0: return False, False
        if Conf.weak_root and head == 0: return False, False
        direction = 'right' if head < counter else 'left'
        return direction, True


class FDist(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        # if Conf.weak_root and head == 0: return False, False
        return counter - head, True


class FSentenceLength(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        return len(sentence.words) - 1, True


class FModifierNeighLR1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.token, cl.token, cr.token), True


class FModifierNeighLR2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.pos, cr.pos), True


class FModifierNeighLR3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.token, cr.pos), True


class FModifierNeighLR4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.token, cl.pos, cr.pos), True


class FModifierNeighLR5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (c.pos, cl.pos, cr.token), True


class FModifierNeighLR6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        cl = sentence.words[counter - 1]
        cr = sentence.words[counter + 1]
        return (cl.pos, cr.pos), True


class FModifierNeighLR7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        cl = sentence.words[counter - 1]
        return (c.pos, cl.pos), True


class FModifierNeighLR8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if counter == len(sentence.words) - 1: return False, False
        c = sentence.words[counter]
        cr = sentence.words[counter + 1]
        return (c.pos, cr.pos), True


class FHeadNeighLR1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.token, cl.token, cr.token), True


class FHeadNeighLR2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.pos, cr.pos), True


class FHeadNeighLR3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.token, cr.pos), True


class FHeadNeighLR4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.token, cl.pos, cr.pos), True


class FHeadNeighLR5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (c.pos, cl.pos, cr.token), True


class FHeadNeighLR6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head in [0, len(sentence.words) - 1]: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        cr = sentence.words[head + 1]
        return (cl.pos, cr.pos), True


class FHeadNeighLR7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head == 0: return False, False
        c = sentence.words[head]
        cl = sentence.words[head - 1]
        return (c.pos, cl.pos), True


class FHeadNeighLR8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if head == len(sentence.words) - 1: return False, False
        c = sentence.words[head]
        cr = sentence.words[head + 1]
        return (c.pos, cr.pos), True


class FAbsDistWithPos(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        # if Conf.weak_root and head == 0: return False, False
        return (sentence.words[counter].pos, abs(head - counter)), True


class FDirectionWithPos(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        # if Conf.weak_root and head == 0: return False, False
        if head < counter: return 'right', True
        return (sentence.words[counter].pos, 'left'), True


class FDistWithPos(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        # if Conf.weak_root and head == 0: return False, False
        return (sentence.words[counter].pos, counter - head), True


class FSentenceLengthWithPos(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        return (sentence.words[counter].pos, len(sentence.words) - 1), True


class FLengthWithPos(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        return (sentence.words[counter].pos, len(sentence)), True


class FInBetween1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 2): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 3): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 4): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 5): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 6): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 5].pos if head < counter else sentence.words[counter + 5].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 7): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 6].pos if head < counter else sentence.words[counter + 6].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 8): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 7].pos if head < counter else sentence.words[counter + 7].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 9): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 8].pos if head < counter else sentence.words[counter + 8].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween9(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 10): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 9].pos if head < counter else sentence.words[counter + 9].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween10(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 11): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 10].pos if head < counter else sentence.words[counter + 10].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween11(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 12): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 11].pos if head < counter else sentence.words[counter + 11].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween12(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 13): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 12].pos if head < counter else sentence.words[counter + 12].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FInBetween13(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 14): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos = sentence.words[counter - 13].pos if head < counter else sentence.words[counter + 13].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos, hpos), True


class FDigit1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        if not c.token[0].isdigit(): return False, False
        return c.pos, True


class FDigit2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if not c.token[0].isdigit(): return False, False
        return (c.pos, h.pos), True


class FCapital1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        if not c.token[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": return False, False
        return c.pos, True


class FCapital2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if not c.token[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": return False, False
        return (c.pos, h.pos), True


class FPrefix1_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 2: return None, False
        return (c.token[0:2], c.pos), True


class FPrefix1_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 2: return None, False
        return (c.token[0:2], c.pos, h.pos), True


class FPrefix2_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[0:3], c.pos), True


class FPrefix2_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[0:3], c.pos, h.pos), True


class FPrefix3_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 4: return None, False
        return (c.token[0:4], c.pos), True


class FPrefix3_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 4: return None, False
        return (c.token[0:4], c.pos, h.pos), True


class FSuffix1_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 2: return None, False
        return (c.token[-2:], c.pos), True


class FSuffix1_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 2: return None, False
        return (c.token[-2:], c.pos, h.pos), True


class FSuffix2_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[-3:], c.pos), True


class FSuffix2_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[-3:], c.pos, h.pos), True


class FSuffix3_1(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[-3:], c.pos), True


class FSuffix3_2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        h = sentence.words[head]
        if len(c.token) < 3: return None, False
        return (c.token[-3:], c.pos, h.pos), True


class F7Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.token, p.pos, c.token, c.pos), True


class F8Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.pos, c.token, c.pos), True


class F9Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.token, c.token, c.pos), True


class F10Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.token, p.pos, c.pos), True


class F11Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.token, p.pos, c.token), True


class F12Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.token, c.token), True


class F13Direction(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        c = sentence.words[counter]
        p = sentence.words[head]
        direction = 'right' if head < counter else 'left'
        return (direction, p.pos, c.pos), True


class FInBetweenAll2(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 3): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, hpos), True


class FInBetweenAll3(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 4): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, hpos), True


class FInBetweenAll4(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 5): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        mpos4 = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, mpos4, hpos), True


class FInBetweenAll5(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 6): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        mpos4 = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        mpos5 = sentence.words[counter - 5].pos if head < counter else sentence.words[counter + 5].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, mpos4, mpos5, hpos), True


class FInBetweenAll6(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 7): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        mpos4 = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        mpos5 = sentence.words[counter - 5].pos if head < counter else sentence.words[counter + 5].pos
        mpos6 = sentence.words[counter - 6].pos if head < counter else sentence.words[counter + 6].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, mpos4, mpos5, mpos6, hpos), True


class FInBetweenAll7(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 8): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        mpos4 = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        mpos5 = sentence.words[counter - 5].pos if head < counter else sentence.words[counter + 5].pos
        mpos6 = sentence.words[counter - 6].pos if head < counter else sentence.words[counter + 6].pos
        mpos7 = sentence.words[counter - 7].pos if head < counter else sentence.words[counter + 7].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, mpos4, mpos5, mpos6, mpos7, hpos), True


class FInBetweenAll8(FeatureGenerator):
    def get_hash_valid(self, sentence, head, counter):
        if Conf.weak_root and head == 0: return False, False
        if (abs(head - counter) < 9): return False, False
        cpos = sentence.words[counter].pos
        hpos = sentence.words[head].pos
        mpos1 = sentence.words[counter - 1].pos if head < counter else sentence.words[counter + 1].pos
        mpos2 = sentence.words[counter - 2].pos if head < counter else sentence.words[counter + 2].pos
        mpos3 = sentence.words[counter - 3].pos if head < counter else sentence.words[counter + 3].pos
        mpos4 = sentence.words[counter - 4].pos if head < counter else sentence.words[counter + 4].pos
        mpos5 = sentence.words[counter - 5].pos if head < counter else sentence.words[counter + 5].pos
        mpos6 = sentence.words[counter - 6].pos if head < counter else sentence.words[counter + 6].pos
        mpos7 = sentence.words[counter - 7].pos if head < counter else sentence.words[counter + 7].pos
        mpos8 = sentence.words[counter - 8].pos if head < counter else sentence.words[counter + 8].pos
        direction = 'right' if head < counter else 'left'
        return (direction, cpos, mpos1, mpos2, mpos3, mpos4, mpos5, mpos6, mpos7, mpos8, hpos), True


def add_complex(fv: FeatureVec):
    fv.add_feature_gen(FMissedBigrams1(Conf.filter))
    fv.add_feature_gen(FMissedBigrams2(Conf.filter))
    fv.add_feature_gen(FAbsDist(Conf.filter))
    fv.add_feature_gen(FDirection(Conf.filter))
    fv.add_feature_gen(FDist(Conf.filter))
    fv.add_feature_gen(FSentenceLength(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR1(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR2(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR3(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR4(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR5(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR6(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR7(Conf.filter))
    fv.add_feature_gen(FModifierNeighLR8(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR1(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR2(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR3(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR4(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR5(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR6(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR7(Conf.filter))
    fv.add_feature_gen(FHeadNeighLR8(Conf.filter))
    fv.add_feature_gen(FAbsDistWithPos(Conf.filter))
    fv.add_feature_gen(FDirectionWithPos(Conf.filter))
    fv.add_feature_gen(FDistWithPos(Conf.filter))
    fv.add_feature_gen(FSentenceLengthWithPos(Conf.filter))
    fv.add_feature_gen(FInBetween1(Conf.filter))
    fv.add_feature_gen(FInBetween2(Conf.filter))
    fv.add_feature_gen(FInBetween3(Conf.filter))
    fv.add_feature_gen(FInBetween4(Conf.filter))
    fv.add_feature_gen(FInBetween5(Conf.filter))
    fv.add_feature_gen(FInBetween6(Conf.filter))
    fv.add_feature_gen(FInBetween7(Conf.filter))
    fv.add_feature_gen(FInBetween8(Conf.filter))
    fv.add_feature_gen(FInBetween9(Conf.filter))
    fv.add_feature_gen(FInBetween10(Conf.filter))
    fv.add_feature_gen(FInBetween11(Conf.filter))
    fv.add_feature_gen(FInBetween12(Conf.filter))
    fv.add_feature_gen(FInBetween13(Conf.filter))
    # fv.add_feature_gen(FDigit1(Conf.filter))
    # fv.add_feature_gen(FDigit2(Conf.filter))
    # fv.add_feature_gen(FCapital1(Conf.filter))
    # fv.add_feature_gen(FCapital2(Conf.filter))
    # fv.add_feature_gen(FPrefix1_1(Conf.filter))
    # fv.add_feature_gen(FPrefix1_2(Conf.filter))
    # fv.add_feature_gen(FPrefix2_1(Conf.filter))
    # fv.add_feature_gen(FPrefix2_2(Conf.filter))
    # fv.add_feature_gen(FPrefix3_1(Conf.filter))
    # fv.add_feature_gen(FPrefix3_2(Conf.filter))
    # fv.add_feature_gen(FSuffix1_1(Conf.filter))
    # fv.add_feature_gen(FSuffix1_2(Conf.filter))
    # fv.add_feature_gen(FSuffix2_1(Conf.filter))
    # fv.add_feature_gen(FSuffix2_2(Conf.filter))
    # fv.add_feature_gen(FSuffix3_1(Conf.filter))
    # fv.add_feature_gen(FSuffix3_2(Conf.filter))
    fv.add_feature_gen(F7Direction(Conf.filter))
    fv.add_feature_gen(F8Direction(Conf.filter))
    fv.add_feature_gen(F9Direction(Conf.filter))
    fv.add_feature_gen(F10Direction(Conf.filter))
    fv.add_feature_gen(F11Direction(Conf.filter))
    fv.add_feature_gen(F12Direction(Conf.filter))
    fv.add_feature_gen(F13Direction(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll2(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll3(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll4(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll5(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll6(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll7(Conf.filter))
    # fv.add_feature_gen(FInBetweenAll8(Conf.filter))
