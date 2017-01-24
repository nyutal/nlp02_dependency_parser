import time
from basic_features.feature import *
from basic_features.unigrams import *
from basic_features.bigrams import *
from basic_features.complex import *
import perceptron as pr
from conf import Conf
from dataParser import *


def train(fv: FeatureVec, trainer: pr.Perceptron, train_corpus: Corpus, out_file):
    out_file.write('start training at ' + time.asctime())
    weights = trainer.train(train_corpus, fv, Conf.train_niter)
    out_file.write('finish training at ' + time.asctime())
    return weights



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

    trainer = pr.Perceptron()

    weights = None
    if Conf.weights_src is None:
        weights = train(fv, trainer, train_corpus, out_file)
    else:
        weights = np.asarray(list(map(float, [line.strip() for line in open(Conf.weights_src)])))
    for i in weights:
        out_weight_file.write("%s\n" % i)
        # out_weight_file.writelines(weights.tostring())

    if Conf.test_file_name is not None:
        test_corpus = dp.parse(Conf.test_file_name, Conf.test_max_samples)
        out_file.write('start testing at ' + time.asctime())
        accuracy = trainer.test(test_corpus, fv, weights)
        out_file.write('finish testing at ' + time.asctime())
        out_file.write('accuracy=' + str(accuracy) + "\n")






    out_file.close()
    out_weight_file.close()


if __name__ == '__main__':
    main()
