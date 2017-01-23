from dataParser import *
from basic_features.unigrams import *
from basic_features.bigrams import *
import perceptron as pr
from conf import Conf


def main():
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

    weights = trainer.train(train_corpus, fv, Conf.train_niter)

    test_corpus = dp.parse(Conf.test_file_name, Conf.test_max_samples)

    trainer.test(test_corpus, fv, weights)




if __name__ == '__main__':
    main()
