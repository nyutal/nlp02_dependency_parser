from sentence import *

class Corpus(object):
    def __init__(self, sentences, file_name):
        self.sentences = sentences
        self.file_name = file_name

    def get_sentences(self):
        return self.sentences

    def get_corpus_file(self):
        return self.file_name
