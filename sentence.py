
class Word(object):

    def __init__(self, c, t, p, h):
        self.counter = c
        self.token = t
        self.pos = p
        self.head = h

    def __str__(self):
        return str(self.counter) + ' ' + str(self.token) + ' ' + str(self.pos) + ' ' + str(self.head)


class Sentence(object):

    def __init__(self, sid: int = None):
        self.words = []
        self.words.append(Word(0, "", "", -1))
        self.sid = sid

    def get_sentence_length(self):
        return self.get_list_size()-1

    def get_list_size(self):
        return len(self.words)

    def append(self, w):
        if not w.counter == len(self.words): raise AssertionError
        self.words.append(w)

    def get_sentence(self):
        return ' '.join(list(map(lambda x: x.token, self.words[1:])))

    def set_id(self, sid: int):
        self.sid = sid

    def get_graph(self):
        g = {}
        for i in range(1, self.get_list_size()):
            if self.words[i].head not in g:
                g[self.words[i].head] = { self.words[i].counter: 0.0}
            else:
                g[self.words[i].head][i] = 0.0
        return g




