
class Word(object):

    def __init__(self, c, t, p, h):
        self.counter = c
        self.token = t
        self.pos = p
        self.head = h

    def __str__(self):
        return str(self.counter + ' ' + self.token + ' ' + self.pos + ' ' + self.head)


class Sentence(object):

    def __init__(self):
        self.words = []
        self.words.append(Word(0, "", "", -1))

    def get_length(self):
        return len(self.words)-1

    def append(self, w):
        self.words.append(w)

    def getSentence(self):
        return ' '.join(list(map(lambda x: x.token, self.words[1:])))

