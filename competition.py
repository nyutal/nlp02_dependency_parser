import time
from basic_features.unigrams import *
from basic_features.bigrams import *
from basic_features.complex import *
from conf import Conf
from dataParser import *
import edmonds as ed

def main():

    out_file = open(Conf.output_file_name, 'w')
    out_weight_file = open(Conf.output_weight_file_name, 'w')

    dp = DataParser()
    train_corpus = dp.parse(Conf.train_file_name, Conf.train_max_samples)

    fv = FeatureVec()
    add_unigrams(fv)
    add_bigrams(fv)
    if Conf.is_complex:
        add_complex(fv)
    fv.generate_features(train_corpus)

    out_file.write(Conf.get_conf_str() + "\n")
    out_file.write(str(fv.get_feature_gen_count()) + "\n")

    weights = np.asarray(list(map(float, [line.strip() for line in open(Conf.weights_src_comp)])))
    for i in weights:
        out_weight_file.write("%s\n" % i)

    comp_corpus = dp.parse_comp(Conf.comp_file_name, Conf.comp_max_samples)
    out_file.write('start testing at ' + time.asctime())
    comp(comp_corpus, fv, weights, out_file)
    out_file.write('finish testing at ' + time.asctime())
    out_file.close()
    out_weight_file.close()


def comp(corpus: Corpus, fv: FeatureVec, weights, out_file):
    for s in corpus.get_sentences():
        g = build_clique_graph(s, fv, weights)
        y_mst = ed.mst(0, g)
        out_file.write(str(y_mst))
        for w in s.words[1:]:
            pass # TODO: if w.head in y_mst and w.counter in y_mst[w.head]:



def build_clique_graph(s, fv, weights):
    g = {}
    for head in range(s.get_list_size()):
        g[head] = {}
        for counter in range(1, s.get_list_size()):
            g[head][counter] = fv.get_weight_for_edge(s, head, counter, weights)
    return g

if __name__ == '__main__':
    main()
