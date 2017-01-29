from sentence import *
from corpus import *


class DataParser(object):

    def __init__(self):
        pass

    def parse(self, in_file, max_samples=0, is_competition=False):
        newSententence = True
        sentences = []
        sid = 0
        sentence = Sentence(sid)
        with open(in_file) as f:
            for line in f:
                if not line.strip():
                    if sentence.get_sentence_length() > 0:
                        sentences.append(sentence)
                        # print(sentence.getSentence())

                    else:
                        print('drop empty sentence')
                        exit(-1)
                    sid += 1
                    if(sid == max_samples):
                        print('quit after max_samples:', max_samples)
                        break
                    sentence = Sentence(sid)
                    continue
                tabs = line.split('\t')
                if not is_competition:
                    sentence.append(Word(int(tabs[0]), tabs[1], tabs[3], int(tabs[6])))
                else:
                    sentence.append(Word(int(tabs[0]), tabs[1], tabs[3], int(-1)))
        corpus = Corpus(sentences, in_file)
        return corpus



if __name__ == '__main__':
    pass



