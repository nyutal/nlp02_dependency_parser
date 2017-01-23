from dataParser import *
from basic_features.unigrams import *
from basic_features.bigrams import *
import perceptron as pr
from conf import Conf
import time


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
    fv.add_feature_gen(F1())
    fv.add_feature_gen(F2())
    fv.add_feature_gen(F3())
    fv.add_feature_gen(F4())
    fv.add_feature_gen(F5())
    fv.add_feature_gen(F6())
    fv.add_feature_gen(F7())
    fv.add_feature_gen(F8())
    fv.add_feature_gen(F9())
    fv.add_feature_gen(F10())
    fv.add_feature_gen(F11())
    fv.add_feature_gen(F12())
    fv.add_feature_gen(F13())

    fv.generate_features(train_corpus)
    # fv.fgArr[0].filter_features(5)

    trainer = pr.Perceptron()

    weights = None
    if Conf.weights_src is None:
        weights = train(fv, trainer, train_corpus, out_file)
    else:
        weights = np.asarray(list(map(float, [line.strip() for line in open(Conf.weights_src)])))

    test_corpus = dp.parse(Conf.test_file_name, Conf.test_max_samples)

    ##### testing #######
    out_file.write('start testing at ' + time.asctime())

    accuracy = trainer.test(test_corpus, fv, weights)

    out_file.write('finish testing at ' + time.asctime())
    ####################




    out_file.write(Conf.get_conf_str() + "\n")
    out_file.write(str(fv.get_feature_gen_count()) + "\n")

    for i in weights:
        out_weight_file.write("%s\n" % i)
    # out_weight_file.writelines(weights.tostring())
    out_file.write('accuracy=' + str(accuracy) + "\n")

    out_file.close()
    out_weight_file.close()


if __name__ == '__main__':
    main()
