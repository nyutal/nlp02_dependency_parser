from sentence import *


class DataParser(object):

    def __init__(self):
        pass

    def parse(self, inFile):
        newSententence = True
        sentences = []
        sentence = Sentence()
        with open(inFile) as f:
            for line in f:
                if not line.strip():
                    if sentence.get_length() > 0:
                        sentences.append(sentence)
                        print(sentence.getSentence())
                    else:
                        print('drop empty sentence')
                    sentence = Sentence()
                    continue
                tabs = line.split('\t')
                sentence.append(Word(tabs[0], tabs[1], tabs[3], tabs[6]))





if __name__ == '__main__':

    dp = DataParser()
    dp.parse('HW2-files/train.labeled')

