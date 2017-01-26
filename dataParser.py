from corpus import *


class DataParser(object):

    def __init__(self):
        pass

    def parse(self, in_file, max_samples=0):
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
                    if sid == max_samples:
                        print('quit after max_samples:', max_samples)
                        break
                    sentence = Sentence(sid)
                    continue
                tabs = line.split('\t')
                sentence.append(Word(int(tabs[0]), tabs[1], tabs[3], int(tabs[6])))
        corpus = Corpus(sentences, in_file)
        return corpus


    def parse_comp(self, in_file, max_samples=0):
        sentences = []
        sid = 0
        sentence = Sentence(sid)
        with open(in_file) as f:
            for line in f:
                if not line.strip():
                    if sentence.get_sentence_length() > 0:
                        sentences.append(sentence)
                        print(sentence.get_sentence())

                    else:
                        print('drop empty sentence')
                        exit(-1)
                    sid += 1
                    if sid == max_samples:
                        print('quit after max_samples:', max_samples)
                        break
                    sentence = Sentence(sid)
                    continue
                tabs = line.split('\t')
                sentence.append(Word(int(tabs[0]), tabs[1], tabs[3], 0))
        corpus = Corpus(sentences, in_file)
        return corpus

if __name__ == '__main__':
    pass



