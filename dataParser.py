from sentence import *
from corpus import *


class DataParser(object):

    def __init__(self):
        pass

    def parse(self, in_file):
        newSententence = True
        sentences = []
        sentence = Sentence()
        with open(in_file) as f:
            for line in f:
                if not line.strip():
                    if sentence.get_sentence_length() > 0:
                        sentences.append(sentence)
                        # print(sentence.getSentence())
                    else:
                        print('drop empty sentence')
                        exiit(-1)
                    sentence = Sentence()
                    continue
                tabs = line.split('\t')
                sentence.append(Word(int(tabs[0]), tabs[1], tabs[3], int(tabs[6])))
        corpus = Corpus(sentences, in_file)
        return corpus



if __name__ == '__main__':
    pass



