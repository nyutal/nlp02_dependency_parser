import time
from basic_features.unigrams import *
from basic_features.bigrams import *
from basic_features.complex import *
from conf import Conf
from dataParser import *

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
        # out_weight_file.writelines(weights.tostring())

    if Conf.test_file_name is not None:
        test_corpus = dp.parse(Conf.comp_file_name, Conf.comp_max_samples)
        out_file.write('start testing at ' + time.asctime())
        test(test_corpus, fv, weights)
        out_file.write('finish testing at ' + time.asctime())

    out_file.close()
    out_weight_file.close()


def test(self, corpus: Corpus, fv: FeatureVec, weights):
    nwords = 0.
    ncorrect = 0.
    for s in corpus.get_sentences():
        g = self.build_clique_graph(s, fv, weights)
        y_mst = ed.mst(0, g)
        for w in s.words[1:]:
            nwords += 1.0
            if w.head in y_mst and w.counter in y_mst[w.head]:
                ncorrect += 1.0
                # else:
                #     print('error: (h,m)=(', w.head, w.counter, '), predicted graph:', y_mst)
    print('test: words=', str(nwords), ', correct words=', str(ncorrect), ', precision=',
          str(ncorrect / nwords * 100) + '%')
    return ncorrect / nwords


if __name__ == '__main__':
    main()
